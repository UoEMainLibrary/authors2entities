from dataclasses import dataclass
import requests, pprint, json

import names

##############################################################################

@dataclass
class Item:
    uuid:    str
    title:   str
    authors: list[tuple[str, str]]

    @classmethod
    def from_json(cls, json):
        match json:
            case { "_embedded": {
                    "indexableObject": {
                        "id": uuid, "metadata": {
                            "dc.contributor.author": authors,
                            "dc.title": titles,
                        }
                      }
                    }
                  }:

                title = " ".join([ v["value"] for v in titles ])
                return cls(uuid, title, [ (author["value"], author["authority"]) for author in authors ])

    def __lt__(self, other): return self.title < other.title

    def process(self, d, collection, authors):
        print(f"\033[1;32m{self.uuid} '\033[33m{self.title}\033[0;37m'")

        for a, auth in self.authors:
            if auth.startswith("virtual"):
                print(f"\033[35mSkipping\033[37m' {a}'")
                continue

            author = names.tidy(a)

            if a != author: print(f"\033[32mConverted\033[37m' {a}' to '{author}'")

            if author in authors:
                author_uuid = authors[author]
                if not d.add_author_to_item(author_uuid, self.uuid): return False

                print(f"\033[36mAdded\033[37m '{author}'  with id {author_uuid}")
            else:
                author_uuid = d.create_author_entity(collection, author)
                if author_uuid is None: return False
                if not d.add_author_to_item(author_uuid, self.uuid): return False
                authors[author] = author_uuid

                print(f"\033[33mCreated\033[37m '{author}' with id {author_uuid}")

        if (places := d.get_item(self.uuid)) is None: return False

        type_places, auth_places = places

        if not d.patch_item(self.uuid, type_places, auth_places): return False

        return True

@dataclass
class Author:
    uuid:     str
    surname:  str
    forename: str

    @classmethod
    def from_json(cls, json):
        match json:
            case { "_embedded": {
                    "indexableObject": {
                        "id": uuid, "metadata": {
                            "person.familyName": surname,
                            "person.givenName": forename,
                        }
                      }
                    }
                  }:
                sn = " ".join([ v["value"] for v in surname ])
                fn = " ".join([ v["value"] for v in forename ])

                return cls(uuid, sn, fn)

    def __lt__(self, other): return self.title < other.title

    @property
    def fullname(self): return f"{self.surname}, {self.forename}"

##############################################################################

@dataclass
class Community:
    name: str
    uuid: str

    @classmethod
    def from_json(cls, json):
        match json:
            case { "name": name, "uuid": uuid }: return cls(name, uuid)

@dataclass
class Collection:
    name: str
    uuid: str
    community: Community

    @classmethod
    def from_json(cls, json, comm):
        match json:
            case { "name": name, "uuid": uuid }: return cls(name, uuid, comm)

##############################################################################

class DSpaceAPI:
    def __init__(self, host, port):
        self.host, self.port = host, port
        self.url = f"http://{host}:{port}/server/api"
        self.auth = None

    def options(self):
        resp = requests.options(self.url)

        if resp.status_code != 200:
            print("Failed to set options")
            return False

        self.xsrf_cookie = resp.cookies["DSPACE-XSRF-COOKIE"]
        self.xsrf_token  = resp.headers["DSPACE-XSRF-TOKEN"]
        return True

    def post(self, path, headers, **opts):
        return requests.post(f"{self.url}/{path}",
                             headers = { "X-XSRF-TOKEN": self.xsrf_token, **headers },
                             cookies = { "DSPACE-XSRF-COOKIE": self.xsrf_cookie },
                             **opts)

    def login(self, user, password):
        if resp := self.post("authn/login",
                             { "Content-Type": "application/x-www-form-urlencoded"},
                             data = f"user={user}&password={password}"):
            self.auth = resp.headers["Authorization"]
            return True

        print("Failed to log in")

    # get

    def get_all_communities(self):
        resp = requests.get(f"{self.url}/core/communities")

        match resp.json():
            case { "_embedded": { "communities": l } }:
                return [ Community.from_json(c) for c in l ]

        return []

    def get_collections(self, comm):
        resp = requests.get(f"{self.url}/core/communities/{comm.uuid}/collections")

        match resp.json():
            case { "_embedded": { "collections": l } }:
                return [ Collection.from_json(c, comm) for c in l ]

        return []

    def get_mapped_items(self, coll):
        resp = requests.get(f"{self.url}/core/collections/{coll.uuid}/mappedItems")
        ret = []

        match resp.json():
            case { "_embedded": { "mappedItems": l } }:
                print(len(l))

    def get_items(self, coll, cls):
        ret, page, n = [], 0, -1

        while True:
            resp = requests.get(f"{self.url}/discover/search/objects?" +
                                f"sort=dc.title&page={page}&size=20" +
                                f"&scope={coll.uuid}&dsoType=ITEM")

            match resp.json():
                case { "_embedded": { "searchResult": { "_embedded": { "objects": objects },
                                                        "page": { "totalPages": n } } } }:
                    ret += [ cls.from_json(obj) for obj in objects ]

            page += 1
            if page >= n: break

        return [ obj for obj in ret if obj is not None ]

    def get_item(self, uuid):
        resp = requests.get(f"{self.url}/core/items/{uuid}",
                             headers = {
                                 "X-XSRF-TOKEN": self.xsrf_token,
                                 "Authorization": self.auth,
                                 },
                             cookies = { "DSPACE-XSRF-COOKIE": self.xsrf_cookie },
                            )

        if resp.status_code == 200:
            match resp.json():
                case { "metadata": { "dspace.entity.type": etype,
                                     "dc.contributor.author": authors } }:
                    type_places = len(etype)
                    auth_places = [ h["place"] for h in authors
                                    if h["authority"][:7] != "virtual" ]
                    return type_places, auth_places

        print("Failed to get item metadata")
        return False

    # create

    def create_workspace_item(self, collection):
        path = f"submission/workspaceitems?owningCollection={collection.uuid}"

        resp = requests.post(f"{self.url}/{path}",
                             headers = {
                                 "X-XSRF-TOKEN": self.xsrf_token,
                                 "Authorization": self.auth,
                                 "Content-Type": "application/json",
                                 },
                             cookies = { "DSPACE-XSRF-COOKIE": self.xsrf_cookie },
                             json = "")

        if resp.status_code == 201:
            match resp.json():
                case { "id": wsitem, "_embedded": { "item": { "uuid": uuid }}}:
                    return wsitem, uuid

        print(f"Failed to create item")
        print(resp)

    def get_workspace_item_status(self, wsitem):
        resp = requests.get(f"{self.url}/submission/workspaceitems/{wsitem}",
                             headers = {
                                 "X-XSRF-TOKEN": self.xsrf_token,
                                 "Authorization": self.auth,
                                 },
                             cookies = { "DSPACE-XSRF-COOKIE": self.xsrf_cookie },
                            )

        if resp.status_code == 200: return True

    def add_image(self, wsitem, img_path):
        path = f"submission/workspaceitems/{wsitem}"

        resp = requests.post(f"{self.url}/{path}",
                             headers = {
                                 "X-XSRF-TOKEN": self.xsrf_token,
                                 "Authorization": self.auth,
                                 # DO NOT include content-type header here!
                                 },
                             cookies = { "DSPACE-XSRF-COOKIE": self.xsrf_cookie },
                             files = {"file": (img_path, open(img_path, 'rb').read(), 'image/png') }
                             )

        if resp.status_code == 201:
            match resp.json():
                case { "id": wsitem }: return wsitem

        print(f"Failed to add image '{img_path}' to id {wsitem}: {resp.status_code}")
        print(resp.text)

    def submit_workspace_item(self, wsitem):
        path = f"workflow/workflowitems?projection=full"
        data = f"{self.url}/submission/workspaceitems/{wsitem}"

        resp = requests.post(f"{self.url}/{path}",
                             headers = {
                                 "X-XSRF-TOKEN": self.xsrf_token,
                                 "Authorization": self.auth,
                                 "Content-Type": "text/uri-list",
                                 },
                             cookies = { "DSPACE-XSRF-COOKIE": self.xsrf_cookie },
                             data = data)

        if resp.status_code == 201: return True

        print(f"Failed to submit item {wsitem}: {resp.status_code}")
        print(resp.text)

    def add_author_to_item(self, author, item):
        path = f"core/items/{item}"

        json = [
            {
                "op":    "add",
                "path":  "/metadata/dspace.entity.type/-",
                "value": { "value": "Publication" }
            }
        ]

        resp = requests.patch(f"{self.url}/{path}",
                             headers = {
                                 "X-XSRF-TOKEN": self.xsrf_token,
                                 "Authorization": self.auth,
                                 "Content-Type": "application/json",
                                 },
                             cookies = { "DSPACE-XSRF-COOKIE": self.xsrf_cookie },
                             json = json)

        if resp.status_code != 200:
            print(f"Failed to add Publication metadata to {item}: {resp.status_code}")
            print(resp.text)
            print(resp.request.body)
            return

        path = f"core/relationships?relationshipType=1"

        resp = requests.post(f"{self.url}/{path}",
                             headers = {
                                 "X-XSRF-TOKEN": self.xsrf_token,
                                 "Authorization": self.auth,
                                 "Content-Type": "text/uri-list",
                                 },
                             cookies = { "DSPACE-XSRF-COOKIE": self.xsrf_cookie },
                             data = 
                                 f"http://localhost:8080/server/api/core/items/{item}\n" +
                                 f"http://localhost:8080/server/api/core/items/{author}"
                             )

        if resp.status_code == 201: return True

        print(f"Failed to add relationship: {resp.status_code}")
        print(resp.text)
        
    def create_author_entity(self, collection, author):
        if (ret := self.create_workspace_item(collection)) is None: return

        wsitem, author_uuid = ret
        surname, forename = author.split(", ")

        if self.patch_author(wsitem, surname, forename) is None: return
        if self.add_image(wsitem, "black_pixel.png") is None: return
        if self.submit_workspace_item(wsitem) is None: return

        return author_uuid

    def create_collection(self, comm_uuid, name):
        json = {"name": name,
                "metadata":
                  {
                      "dc.title": [
                          {
                              "language":None,
                              "value": name,
                              "authority":None,"confidence": -1
                          }],
                      "dspace.entity.type": [ { "value": "Person" } ],
                   }
                }

        if resp := self.post(f"core/collections?parent={comm_uuid}",
                             { "Authorization": self.auth },
                             json = json):
            uuid = resp.json()["uuid"]
            print(f"Created collection '{name}'with uuid {uuid}")
            return uuid

        print(f"Failed to create collection '{name}': {resp.status_code}")
        print(resp.text)

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
            print(f"Created community '{name}' with uuid {uuid}")
            return uuid

        print(f"Failed to create community '{name}': {resp.status_code}")
        print(resp.text)

    # delete

    def delete_community(self, comm_uuid):
        resp = requests.delete(f"{self.url}/core/communities/{comm_uuid}")

        match resp.status_code:
            case 204: print("Delete community succeeded")
            case 401: print("Delete community failed: not authorised")
            case 403: print("Delete community failed: not permitted")
            case 404: print("Delete community failed: not found")

    # patch

    def patch_author(self, wsitem, surname, forename):
        path = f"submission/workspaceitems/{wsitem}"

        json = [
            {
                "op":    "add",
                "path":  "/sections/personStep/person.familyName",
                "value": [{ "value": surname }]
            },
            {
                "op":    "add",
                "path":  "/sections/personStep/person.givenName",
                "value": [{ "value": forename }]
            },
            {
                "op":    "add",
                "path":  "/sections/license/granted",
                "value": "true"
            }
        ]

        resp = requests.patch(f"{self.url}/{path}",
                             headers = {
                                 "X-XSRF-TOKEN": self.xsrf_token,
                                 "Authorization": self.auth,
                                 "Content-Type": "application/json",
                                 },
                             cookies = { "DSPACE-XSRF-COOKIE": self.xsrf_cookie },
                             json = json)

        if resp.status_code == 200: return wsitem

        print(f"Failed to patch workspace item {wsitem}: {resp.status_code}")
        print(resp.text)

    def patch_item(self, uuid, type_places, auth_places):
        path = f"core/items/{uuid}"

        json = [ { "op": "remove", "path": f"/metadata/dc.contributor.author/{n}" }
                 for n in auth_places ] + [
                { "op": "remove", "path": f"/metadata/dspace.entity.type/{1 + n}" }
                 for n in range(type_places - 1)
                ]

        json = list(reversed(json))
        
        resp = requests.patch(f"{self.url}/{path}",
                             headers = {
                                 "X-XSRF-TOKEN": self.xsrf_token,
                                 "Authorization": self.auth,
                                 "Content-Type": "application/json",
                                 },
                             cookies = { "DSPACE-XSRF-COOKIE": self.xsrf_cookie },
                             json = json)

        if resp.status_code == 200:
#            pprint.pprint(resp.json()["metadata"])
            return True

        print(f"Failed to patch item {uuid}: {resp.status_code}")
        print(resp.text)

##############################################################################
