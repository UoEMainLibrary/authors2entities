from api import *

HOST = "localhost"
PORT = "8080"
USER = "root%40localhost"
PASS = "dspace"

COMMUNITY  = "Entities"
COLLECTION = "Entities"


d = DSpaceAPI(HOST, PORT)

if d.options() is None: exit(1)
if d.login(USER, PASS) is None: exit(2)

if (comm := d.find_community(COMMUNITY)) is None: exit(3)
if (coll := d.find_collection(comm, COLLECTION)) is None: exit(4)

print("Reading existing authors...")
authors = { item.fullname: item.uuid for item in d.get_items(coll, Author) }
print(f"Read {len(authors)} authors")

for author in sorted(authors.keys()):
    print(author)
