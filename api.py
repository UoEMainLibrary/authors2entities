import requests, json, sys
from datetime import datetime

from classes import *

class DSpaceAPI:
    def __init__(self, host, port):
        self.host, self.port = host, port
        self.url = f"http://{host}:{port}/server/api"
        self.auth = None

        s = datetime.now().isoformat(timespec = "seconds")
        self.logger = open(f"logs/{s}.log", "w")

    def options(self):
        resp = requests.options(self.url)

        if resp.status_code == 200:
            self.xsrf_cookie = resp.cookies["DSPACE-XSRF-COOKIE"]
            self.xsrf_token  = resp.headers["DSPACE-XSRF-TOKEN"]
            return True

    def login(self, user, password):
        if resp := requests.post(f"{self.url}/authn/login",
                             headers = { "X-XSRF-TOKEN": self.xsrf_token,
                                         "Content-Type": "application/x-www-form-urlencoded"},
                             cookies = { "DSPACE-XSRF-COOKIE": self.xsrf_cookie },
                             data = f"user={user}&password={password}"):
            self.auth = resp.headers["Authorization"]
            return True

    def reauthenticate(self):
        resp = requests.post(f"{self.url}/authn/login",
                             headers = { "X-XSRF-TOKEN": self.xsrf_token,
                                         "Authorization": self.auth },
                             cookies = { "DSPACE-XSRF-COOKIE": self.xsrf_cookie },
                             )
        self.auth = resp.headers["Authorization"]

    @classmethod
    def start(cls, host, port, user, password):
        d = cls(host, port)

        if d.options() is None:
            d.log_to_screen("Failed to set options\n", fg = 1, bright = 1)
            d.close()
            return

        if d.login(user, password) is None:
            d.log_to_screen("Failed to log in\n", fg = 1, bright = 1)
            d.close()
            return

        return d

    def close(self):
        self.logger.close()

    def log_to_screen(self, s, fg = 7, bg = 0, bright = 0):
        sys.stderr.write(f"\033[3{fg};4{bg};{bright}m{s}\033[37;40;0m")

    def log(self, s): self.logger.write(s + "\n")

    def log_resp(self, s, resp):
        self.logger.write(f"\n*** {s}: {resp.status_code}\n")
        self.logger.write(f"{resp.text}\n\n")

    ##############################################################################

    # helpers

    def get_embedded(self, url, **params):
        resp = requests.get(f"{self.url}/{url}", params = params)

        match resp.json():
            case { "_embedded": e }:
                return e

    def find_embedded(self, url, key, value):
        match self.get_embedded(url):
            case { **h }:
                if key in h:
                    for c in h[key]:
                        match c:
                            case { "name": name, "uuid": uuid } if name == value:
                                return name, uuid

    def post(self, path, headers, **opts):
        return requests.post(f"{self.url}/{path}",
                             headers = { "X-XSRF-TOKEN": self.xsrf_token,
                                         "Authorization": self.auth,
                                         **headers },
                             cookies = { "DSPACE-XSRF-COOKIE": self.xsrf_cookie },
                             **opts)

    def put(self, path, headers, **opts):
        return requests.put(f"{self.url}/{path}",
                            headers = {
                                "X-XSRF-TOKEN": self.xsrf_token,
                                "Authorization": self.auth,
                                **headers
                            },
                            cookies = { "DSPACE-XSRF-COOKIE": self.xsrf_cookie },
                            **opts)

    def delete(self, path, name):
        resp = requests.delete(f"{self.url}/{path}",
                               headers = {
                                   "X-XSRF-TOKEN": self.xsrf_token,
                                   "Authorization": self.auth,
                                   "Content-Type": "text/uri-list"
                               },
                               cookies = { "DSPACE-XSRF-COOKIE": self.xsrf_cookie })

        match resp.status_code:
            case 204: self.log(f"{name}: delete succeeded")
            case 401: self.log(f"{name}: delete not authorised")
            case 403: self.log(f"{name}: delete not permitted")
            case 404: self.log(f"{name}: delete not found")

    def patch(self, path, json):
        return requests.patch(f"{self.url}/{path}",
                             headers = {
                                 "X-XSRF-TOKEN": self.xsrf_token,
                                 "Authorization": self.auth,
                                 "Content-Type": "application/json",
                                 },
                             cookies = { "DSPACE-XSRF-COOKIE": self.xsrf_cookie },
                             json = json)

    def patch_add(self, path, items):
        json = [ { "op": "add", "path": k, "value": v } for k, v in items.items() ]

        return self.patch(path, json)

    def patch_remove(self, path, items):
        json = [ { "op": "remove", "path": k } for k in items ]

        return self.patch(path, json)

    ##############################################################################

    # get

    def get_communities(self):
        match self.get_embedded("core/communities"):
            case { "communities": l }:
                return [ Community.from_json(c) for c in l ]

    def get_collections(self, comm):
        match self.get_embedded(f"core/communities/{comm.uuid}/collections"):
            case { "collections": l }:
                return [ Collection.from_json(c, comm) for c in l ]

    def yield_collections(self):
        for comm in self.get_communities() or []:
            for coll in self.get_collections(comm) or []:
                yield coll

    def find_community(self, comm_name):
        match self.find_embedded("core/communities/search/top", "communities", comm_name):
            case name, uuid:
                return Community(name, uuid)

    def find_collection(self, comm, coll_name):
        match self.find_embedded(f"core/communities/{comm.uuid}/collections",
                                 "collections", coll_name):
            case name, uuid:
                return Collection(name, uuid, comm)

    def get_items(self, coll, cls):
        page, pages, count = 0, 1, 1

        self.log_to_screen(f"{coll.community.name}\n", fg = 3, bright = 1)
        while page < pages:
            resp = requests.get(f"{self.url}/discover/search/objects?" +
                                f"sort=dc.title&page={page}&size=20" +
                                f"&scope={coll.uuid}&dsoType=ITEM")

            match resp.json():
                case { "_embedded": { "searchResult": { "_embedded": { "objects": objects },
                                                        "page": { "totalPages": pages } } } }:
                    objs = [ cls.from_json(obj) for obj in objects ]

                    for obj in objs:
                        if obj is not None:
                            self.log_to_screen(f"\r  {coll.name}", fg = 6, bright = 1)
                            self.log_to_screen(f" {page} of {pages}/{count}", fg = 2, bright = 1)
                            count += 1
                            yield obj

            page += 1

        self.log_to_screen(f"\r  {coll.name}", fg = 6, bright = 1)
        self.log_to_screen(f" {page}/{count}                  \n", fg = 2, bright = 1)

    def get_item(self, uuid):
        match requests.get(f"{self.url}/core/items/{uuid}").json():
            case { "metadata": { "dspace.entity.type": etype,
                                 "dc.contributor.author": authors } }:
                type_places = len(etype)
                auth_places = [ h["place"] for h in authors
                                if h["authority"] is None or h["authority"][:7] != "virtual" ]

                return type_places, auth_places

        self.log_("\n*** Failed to get item metadata")

    def get_author_uuid(self, coll, name):
        params = { "scope": coll.uuid,
                   "f.entityType": f"Person,equals",
                   "f.title": f"{name},contains"
                  }

        match self.get_embedded(f"discover/search/objects", **params):
            case { "searchResult": { "_embedded": { "objects": [ ret, *rest ] } } }:
                match ret:
                    case { "_embedded": { "indexableObject": { "id": uuid } } }:
                        return uuid

    def get_workspace_item_status(self, wsitem):
        resp = requests.get(f"{self.url}/submission/workspaceitems/{wsitem}")

        if resp.status_code == 200: return True

    ##############################################################################

    # create

    def create_workspace_item(self, collection):
        resp = self.post(f"submission/workspaceitems?owningCollection={collection.uuid}",
                         { "Content-Type": "application/json" }, json = "")

        if resp.status_code == 201:
            match resp.json():
                case { "id": wsitem, "_embedded": { "item": { "uuid": uuid }}}:
                    return wsitem, uuid

        self.log_resp("Failed to create item {wsitem}", resp)

    def add_image(self, wsitem, img_path):
        resp = self.post(f"submission/workspaceitems/{wsitem}", {},
                         files = {"file": (img_path, open(img_path, 'rb').read(), 'image/png')})

        if resp.status_code == 201:
            match resp.json():
                case { "id": wsitem }: return wsitem

        self.log_resp(f"Failed to add image '{img_path}' to id {wsitem}", resp)

    def submit_workspace_item(self, wsitem):
        resp = self.post(f"workflow/workflowitems?projection=full",
                         { "Content-Type": "text/uri-list" },
                         data = f"{self.url}/submission/workspaceitems/{wsitem}")

        if resp.status_code == 201: return True

        self.log_resp(f"Failed to submit item {wsitem}", resp)

    def set_item_type_to_publication(self, item):
        resp = requests.get(f"{self.url}/core/items/{item.uuid}")

        if resp.status_code != 200:
            self.log_resp(f"Failed to get metadata from {item.uuid}", resp)
            self.log(resp.request.body)
            return False

        match resp.json():
            case { "metadata": { "dspace.entity.type": etypes } }:
                for etype in etypes:
                    if etype["value"] == "Publication": return True

        resp = self.patch_add(f"core/items/{item.uuid}",
                              { "/metadata/dspace.entity.type/-": "Publication" })

        if resp.status_code == 200: return True

        self.log_resp("Failed to add Publication metadata to {item.uuid}", resp)
        self.log(resp.request.body)

    def add_author_to_item(self, author, item):
        resp = self.post(f"core/relationships?relationshipType=1",
                         { "Content-Type": "text/uri-list" },
                         data = 
                         f"http://localhost:8080/server/api/core/items/{item}\n" +
                         f"http://localhost:8080/server/api/core/items/{author}"
                         )

        if resp.status_code == 201: return True

        self.log_resp("Failed to add relationship", resp)
        
    def create_author_entity(self, collection, author):
        if (ret := self.create_workspace_item(collection)) is None: return

        wsitem, author_uuid = ret

        if ", " in author: surname, forename = author.split(", ", 1)
        else:              surname, forename = author, ""

        if self.patch_workspace_item(wsitem, surname, forename) is None: return
        if self.add_image(wsitem, "black_pixel.png") is None: return
        if self.submit_workspace_item(wsitem) is None: return
        if self.patch_author(author_uuid, author) is None: return

        return author_uuid

    def create_collection(self, comm, name):
        json = {"name": name,
                "metadata":
                { "dc.title": [ { "language": None, "value": name }],
                  "dspace.entity.type": [ { "value": "Person" } ]}}

        if resp := self.post(f"core/collections?parent={comm.uuid}",
                             { "Authorization": self.auth },
                             json = json):
            uuid = resp.json()["uuid"]
            self.log(f"Created collection '{name}'with uuid {uuid}")
            return Collection(name, uuid, comm)

        self.log_resp(f"Failed to create collection '{name}'", resp)

    def create_community(self, name):
        json = {"type": {"value": name},
                "metadata":{"dc.title":[{"language":None,"value": name}],
                            "dc.description":[{"language":None}],
                            "dc.description.abstract":[{"language":None}],
                            "dc.rights":[{"language":None}],
                            "dc.description.tableofcontents":[{"language":None}]}}

        if resp := self.post("core/communities",
                             { "Authorization": self.auth },
                             json = json):
            uuid = resp.json()["uuid"]
            self.log(f"Created community '{name}' with uuid {uuid}")
            return Community(name, uuid)

        self.log_resp(f"Failed to create community '{name}'", resp)

    ##############################################################################

    # patch

    def patch_workspace_item(self, wsitem, surname, forename):
        items = { "/sections/personStep/person.familyName": [{ "value": surname }],
                  "/sections/personStep/person.givenName":  [{ "value": forename }],
                  "/sections/license/granted":              "true" }

        resp = self.patch_add(f"submission/workspaceitems/{wsitem}", items)
        if resp.status_code == 200: return wsitem

        self.log_resp(f"Failed to patch workspace item {wsitem}", resp)

    def remove_old_author_metadata(self, uuid, auth_places):
        items = [ f"/metadata/dc.contributor.author/{n}" for n in auth_places ]

        resp = self.patch_remove(f"core/items/{uuid}", list(reversed(items)))

        if resp.status_code == 200: return True

        self.log_resp(f"Failed to patch item {uuid}", resp)

    def patch_author(self, uuid, name):
        resp = self.patch_add(f"core/items/{uuid}",
                              { "/metadata/dc.title/-": [{ "value": name }] } )

        if resp.status_code == 200: return True

        self.log_resp(f"Failed to patch author {uuid}", resp)

    # other

    def absorb_author(self, new, old):
        resp = requests.get(f"{self.url}/core/items/{old}/relationships")

        if resp.status_code == 200:
            match resp.json():
                case { "_embedded": { "relationships": rels } }:
                    for rel in rels:
                        match rel:
                            case { "_links": { "leftItem": { "href": left },
                                               "rightItem": { "href": right }, },
                                   "id": rel_id }:
                                self.transfer_relationships(old, new, rel_id, left, right)

            return True

        self.log_resp(f"Could not find relationships for author {old}", resp)

    def transfer_relationships(self, old, new, rel_id, left, right):
        if   left.endswith(old):  s = "leftItem"
        elif right.endswith(old): s = "rightItem"
        else:
            self.log(f"uuid mismatch in relationship {rel_id}")
            return

        resp = self.put(f"core/relationships/{rel_id}/{s}",
                        { "Content-Type": "text/uri-list"},
                        data = f"{self.url}/core/items/{new}")

        if resp.status_code == 200:
            self.log(f"    {old} is now {new} in {rel_id}")
            self.delete(f"core/items/{old}", "    old author")
            return True

        self.log(f"Failed to update relationship {rel_id}", resp)

    def get_or_create_special_collection(self, comm_name, coll_name):
        if (comm := self.find_community(comm_name)) is None and\
           (comm := self.create_community(comm_name)) is None:
            return

        if (coll := self.find_collection(comm, coll_name)) is None and\
           (coll := self.create_collection(comm, coll_name)) is None:
            return

        return coll

##############################################################################
