from api import *
from datetime import datetime

HOST = "localhost"
PORT = "8080"
USER = "root%40localhost"
PASS = "dspace"

COMMUNITY  = "Entities"
COLLECTION = "Entities"
REAUTH     = 1800 - 30

if (d := DSpaceAPI.start(HOST, PORT, USER, PASS)) is None: exit(1)
if (coll := d.get_or_create_special_collection(COMMUNITY, COLLECTION)) is None: exit(2)

last = datetime.now()

for collection in d.yield_collections():
    if collection.name == COLLECTION and collection.community.name == COMMUNITY: continue

    d.log_to_screen(f"\n{collection.community.name}  ", fg = 3, bg = 4, bright = 1)
    d.log_to_screen(f"{collection.name}", fg = 7, bg = 5, bright = 1)
    d.log_to_screen("\n")

    d.log("==============================================")
    d.log(f"Community:  {collection.community.name}")
    d.log(f"Collection: {collection.name}")

    for item in d.get_items(collection, Item):
        if not item.process(d, coll):
            d.log_to_screen("FAILED; bailing out\n", fg = 3, bg = 1, bright = 1)
            d.close()
            exit(3)

        if (datetime.now() - last).total_seconds() > REAUTH:
            d.log_to_screen("\n")
            d.log_to_screen("Reauthenticated\n", fg = 7, bg = 2, bright = 1)
            last = datetime.now()
            d.reauthenticate()

d.close()
