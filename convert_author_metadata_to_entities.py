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

    print(f"\n\033[1;44;33m{collection.community.name}  \033[1;45;37m{collection.name}\033[0;40m")
    
    for item in d.get_items(collection, Item):
        if not item.process(d, coll):
            print("\033[1;41;33mFAILED; bailing out\033[0;40;37m")
            exit(3)

        if (datetime.now() - last).total_seconds() > REAUTH:
            last = datetime.now()
            d.reauthenticate()
