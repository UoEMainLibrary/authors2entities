import requests, pprint

HOST = "localhost"
PORT = "8080"
USER = "root%40localhost"
PASS = "dspace"

COMMUNITY  = "special community for entities"
COLLECTION = "special collection for entities"

##############################################################################

class DSpaceAPI:
    def __init__(self, host, port):
        self.host, self.port = host, port
        self.url = f"http://{HOST}:{PORT}/server/api"
        self.auth = None

    def options(self):
        resp = requests.options(self.url)

        if resp.status_code != 200: return False

        self.xsrf_cookie = resp.cookies["DSPACE-XSRF-COOKIE"]
        self.xsrf_token  = resp.headers["DSPACE-XSRF-TOKEN"]
        return True

    def post(self, path, headers, **opts):
        resp = requests.post(f"{self.url}/{path}",
                             headers = { "X-XSRF-TOKEN": self.xsrf_token, **headers },
                             cookies = { "DSPACE-XSRF-COOKIE": self.xsrf_cookie },
                             **opts)

        if resp.status_code in [ 200, 201 ]: return resp

    def login(self, user, password):
        if resp := self.post("authn/login",
                             { "Content-Type": "application/x-www-form-urlencoded"},
                             data = f"user={user}&password={password}"):
            self.auth = resp.headers["Authorization"]
            return True

    def find_community(self, name):
        resp = requests.get(f"{self.url}/core/communities/search/top")

        if resp.status_code != 200: return

        match resp.json():
            case { "_embedded": { "communities": l } }:
                for c in l:
                    match c:
                        case { "name": name, "uuid": uuid } if name == COMMUNITY:
                            print(f"Found community with uuid {uuid}")
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

    def find_collection(self, comm_uuid, name):
        resp = requests.get(f"{self.url}/core/communities/{comm_uuid}/collections")

        if resp.status_code != 200: return

        match resp.json():
            case { "_embedded": { "collections": l } }:
                for c in l:
                    match c:
                        case { "name": name, "uuid": uuid } if name == COLLECTION:
                            print(f"Found collection with uuid {uuid}")
                            return uuid

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

##############################################################################

d = DSpaceAPI(HOST, PORT)

if d.options() is None:
    print("Failed to set options")
    exit(1)

if d.login(USER, PASS) is None:
    print("Failed to log in")
    exit(2)

comm_uuid = d.find_community(COMMUNITY) or d.create_community()
coll_uuid = d.find_collection(comm_uuid, COLLECTION) or d.create_collection(comm_uuid)
