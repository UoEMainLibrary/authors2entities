from api import *

HOST = "localhost"
PORT = "8080"
USER = "root%40localhost"
PASS = "dspace"

COMMUNITY  = "Entities"
COLLECTION = "Entities"

if (d := DSpaceAPI.start(HOST, PORT, USER, PASS)) is None: exit(1)
if (coll := d.get_or_create_special_collection(COMMUNITY, COLLECTION)) is None: exit(2)

for collection in d.yield_collections():
    if collection.name == COLLECTION and collection.community.name == COMMUNITY: continue

    print(f"\n\033[1;44;33m{collection.community.name}  \033[1;45;37m{collection.name}\033[0;40m")

    items = d.get_items(collection, Item)
    n = len(items)

    for i, item in enumerate(items):
        print(f"\nItem {i + 1} of {n}")
        if not item.process(d, coll): exit(5)
