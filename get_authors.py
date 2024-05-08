from api import *

HOST = "localhost"
PORT = "8080"
USER = "root%40localhost"
PASS = "dspace"

COMMUNITY  = "Entities"
COLLECTION = "Entities"

if (d := DSpaceAPI.start(HOST, PORT, USER, PASS)) is None: exit(1)
if (coll := d.get_or_create_special_collection(COMMUNITY, COLLECTION)) is None: exit(2)

authors = { item.fullname: item.uuid for item in d.get_items(coll, Author) }

for author in sorted(authors.keys()):
    print(author)
