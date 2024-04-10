from dataclasses import dataclass
import requests, pprint, json

@dataclass
class Item:
    uuid:    str
    title:   str
    authors: list[str]

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
                return cls(uuid, title, [ author["value"] for author in authors ])

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
        ret = []

        match resp.json():
            case { "_embedded": { "communities": l } }:
                for c in l:
                    match c:
                        case { "name": name, "uuid": uuid }:
                            ret.append((name, uuid))

        return ret

    def get_collections(self, comm_id):
        resp = requests.get(f"{self.url}/core/communities/{comm_id}/collections")
        ret = []

        match resp.json():
            case { "_embedded": { "collections": l } }:
                for c in l:
                    match c:
                        case { "name": name, "uuid": uuid }:
                            ret.append((name, uuid))

        return ret

    def get_mapped_items(self, coll_id):
        resp = requests.get(f"{self.url}/core/collections/{coll_id}/mappedItems")
        ret = []

        match resp.json():
            case { "_embedded": { "mappedItems": l } }:
                print(len(l))

    def get_items(self, coll_id):
        ret, page = [], 0

        while True:
            resp = requests.get(f"{self.url}/discover/search/objects?" +
                                f"sort=dc.date.accessioned,DESC&page={page}&size=20" +
                                f"&scope={coll_id}&dsoType=ITEM")
            match resp.json():
                case { "_embedded": { "searchResult": { "_embedded": { "objects": objects },
                                                        "page": { "totalPages": n } } } }:
                    ret += [ Item.from_json(obj) for obj in objects ]

            page += 1
            if page >= n: break

        return [ obj for obj in ret if obj is not None ]

    # find

    def find_community(self, comm_name):
        resp = requests.get(f"{self.url}/core/communities/search/top")

        if resp.status_code == 200:
            match resp.json():
                case { "_embedded": { "communities": l } }:
                    for c in l:
                        match c:
                            case { "name": name, "uuid": uuid } if name == comm_name:
                                print(f"Found community '{name}' with uuid {uuid}")
                                return uuid

            print(f"Community '{comm_name}' does not exist")

    def find_collection(self, comm_uuid, coll_name):
        resp = requests.get(f"{self.url}/core/communities/{comm_uuid}/collections")

        if resp.status_code == 200:
            match resp.json():
                case { "_embedded": { "collections": l } }:
                    for c in l:
                        match c:
                            case { "name": name, "uuid": uuid } if name == coll_name:
                                print(f"Found collection '{name}' with uuid {uuid}")
                                return uuid

        print(f"Collection '{coll_name}' does not exist")

    # create

    def create_workspace_item(self, coll_uuid):
        path = f"submission/workspaceitems?owningCollection={coll_uuid}"

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
                case { "id": wsid }:
                    print(f"Created workspace item with id {wsid}")
                    return wsid
#                case { "_embedded": { "item": { "uuid": uuid } }}:
#                       print(f"Created workspace item with uuid {uuid}")
#                       return uuid

        print(f"Failed to create item")

    def get_workspace_item_status(self, wsitem):
        resp = requests.get(f"{self.url}/submission/workspaceitems/{wsitem}",
                             headers = {
                                 "X-XSRF-TOKEN": self.xsrf_token,
                                 "Authorization": self.auth,
                                 },
                             cookies = { "DSPACE-XSRF-COOKIE": self.xsrf_cookie },
                            )

        print(resp.status_code)
        
        if resp.status_code == 200:
            print(resp.json())

    def submit_workspace_item(self, wsitem):
        path = f"workflow/workflowitems"
        data = f"{self.url}/submission/workspaceitems/{wsitem}"

        resp = requests.post(f"{self.url}/{path}",
                             headers = {
                                 "X-XSRF-TOKEN": self.xsrf_token,
                                 "Authorization": self.auth,
                                 "Content-Type": "text/uri-list",
                                 },
                             cookies = { "DSPACE-XSRF-COOKIE": self.xsrf_cookie },
                             data = data)

        if resp.status_code == 201:
            print(resp.json())
            return
#            match resp.json():
#                case { "_embedded": { "item": { "uuid": uuid } }}:
#                       print(f"Created workspace item with uuid {uuid}")
#                       return uuid

        print(f"Failed to submit item {wsitem}: {resp.status_code}")
        print(data)
        print(resp.text)

    """
    def create_collection(self, comm_uuid):
        json = {"name": COLLECTION,
                "metadata":{"dc.title":[
                    {"language":None,"value": COLLECTION,
                     "authority":None,"confidence": -1}]}
                }

        if resp := self.post(f"core/collections?parent={comm_uuid}",
                             { "Authorization": self.auth },
                             json = json):
            uuid = resp.json()["uuid"]
            print(f"Created collection with uuid {uuid}")
            return uuid

    def create_community(self):
        json = {"type": {"value":COMMUNITY},
                "metadata":{"dc.title":[{"language":None,"value": COMMUNITY}],
                            "dc.description":[{"language":None}],
                            "dc.description.abstract":[{"language":None}],
                            "dc.rights":[{"language":None}],
                            "dc.description.tableofcontents":[{"language":None}]}}

        if resp := self.post("core/communities",
                             { "Authorization": self.auth },
                             json = json):
            uuid = resp.json()["uuid"]
            print(f"Created community with uuid {uuid}")
            return uuid
    """

    # delete

    def delete_community(self, comm_uuid):
        resp = requests.delete(f"{self.url}/core/communities/{comm_uuid}")

        match resp.status_code:
            case 204: print("Delete community succeeded")
            case 401: print("Delete community failed: not authorised")
            case 403: print("Delete community failed: not permitted")
            case 404: print("Delete community failed: not found")

    # patch

    def patch_item(self, wsitem, surname, forename):
        pass
