from api import *

HOST = "localhost"
PORT = "8080"
USER = "root%40localhost"
PASS = "dspace"

COMMUNITY  = "Entities"
COLLECTION = "Entities"

if (d    := DSpaceAPI.start(HOST, PORT, USER, PASS)) is None: exit(1)
if (comm := d.find_community(COMMUNITY)) is None: exit(2)
if (coll := d.find_collection(comm, COLLECTION)) is None: exit(3)

authors = { item.fullname: item.uuid for item in d.get_items(coll, Author) }

for author in sorted(authors.keys()):
    print(author)
