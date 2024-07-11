from api import *

HOST = "localhost"
PORT = "8080"
USER = "root%40localhost"
PASS = "dspace"

if (d := DSpaceAPI.start(HOST, PORT, USER, PASS)) is None: exit(1)

items, authors = 0, 0

for coll in d.yield_collections():
    print(f"Community:  {coll.community.name}   Collection: {coll.name}")

    for item in d.get_items(coll, Item):
        items += 1
        authors += len(item.authors)

print(f"{items} items with {authors} authors")

