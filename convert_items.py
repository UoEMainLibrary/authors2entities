from api import *

import csv

HOST = "localhost"
PORT = "8080"
USER = "root%40localhost"
PASS = "dspace"

COMMUNITY  = "Entities"
COLLECTION = "Entities"


d = DSpaceAPI(HOST, PORT)

if d.options() is None: exit(1)
if d.login(USER, PASS) is None: exit(2)

collections, authors, entity_coll = [], None, None

for comm in d.get_all_communities(): collections += d.get_collections(comm)

for coll in collections:
    if coll.name == COLLECTION and coll.community.name == COMMUNITY:
        authors = { item.fullname: item.uuid for item in d.get_items(coll, Author) }
        entity_coll = coll

if authors is None:
    if (comm_uuid := d.create_community(COMMUNITY)) is None: exit(3)
    if (coll_uuid := d.create_collection(comm_uuid, COLLECTION)) is None: exit(4)

    authors     = {}
    comm        = Community(COMMUNITY, comm_uuid)
    entity_coll = Collection(COLLECTION, coll_uuid, comm)

for collection in collections:
    if collection.name == COLLECTION and collection.community.name == COMMUNITY: continue

    print(f"\n\033[1;44;33m{collection.community.name}  \033[1;45;37m{collection.name}\033[0;40m")

    items = d.get_items(collection, Item)
    n = len(items)

    for i, item in enumerate(items):
        print(f"\nItem {i + 1} of {n}")
        if not item.process(d, entity_coll, authors): exit(5)
