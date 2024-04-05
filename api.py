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

        if resp.status_code != 200:
            print(f"Community '{comm_name}' does not exist")
            return

        match resp.json():
            case { "_embedded": { "communities": l } }:
                for c in l:
                    match c:
                        case { "name": name, "uuid": uuid } if name == comm_name:
                            print(f"Found community '{name}' with uuid {uuid}")
                            return uuid

    def find_collection(self, comm_uuid, coll_name):
        resp = requests.get(f"{self.url}/core/communities/{comm_uuid}/collections")

        if resp.status_code != 200:
            print(f"Collection '{coll_name}' does not exist")
            return

        match resp.json():
            case { "_embedded": { "collections": l } }:
                for c in l:
                    match c:
                        case { "name": name, "uuid": uuid } if name == coll_name:
                            print(f"Found collection '{name}' with uuid {uuid}")
                            return uuid

    def find_eperson(self, email):
        resp = requests.get(f"{self.url}/eperson/epersons/search/byEmail?email={email}")

        if resp.status_code != 200:
            print(f"Failed to find EPerson '{email}': {resp.status_code}")
            print(resp.json)
            return

#        match resp.json():
#            case { "_embedded": { "collections": l } }:
#                for c in l:
#                    match c:
#                        case { "name": name, "uuid": uuid } if name == COLLECTION:
#                            print(f"Found collection with uuid {uuid}")
#                            return uuid

    # create

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

    def create_eperson(self, surname, forename):
        email = f"{forename}-{surname}@somewhere.ac.uk"

        json = {"type": "eperson",
                "email": email,
                "metadata": { "eperson.firstname": [ { "value": forename, } ],
                              "eperson.lastname":  [ { "value": surname,  } ]
                              }}

        resp = self.post("eperson/epersons",
                          { "Authorization": self.auth },
                          json = json)

        match resp.status_code:
            case 201:
                uuid = resp.json()["uuid"]
                print(f"Created eperson with uuid {uuid}")
                return uuid
            case 401: print("Create eperson failed: not authorised")
            case 403: print("Create eperson failed: not permitted")
            case 422: print(f"Create eperson failed: bad email '{email}'")
            case 500: print(f"Create eperson failed: internal server error")

    # delete

    def delete_community(self, comm_uuid):
        resp = requests.delete(f"{self.url}/core/communities/{comm_uuid}")

        match resp.status_code:
            case 204: print("Delete community succeeded")
            case 401: print("Delete community failed: not authorised")
            case 403: print("Delete community failed: not permitted")
            case 404: print("Delete community failed: not found")
