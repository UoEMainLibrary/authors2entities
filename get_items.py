from api import DSpaceAPI, Author, Item

import csv

import tidy

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

"""
for coll in collections:
    if coll.name == COLLECTION and coll.community.name == COMMUNITY:
        authors = { item.fullname: item.uuid for item in d.get_items(coll, Author) }
        entity_coll = coll

if authors is None:
    print("Unable to get authors")
    exit(3)
"""

for collection in collections:
    if collection.name == COLLECTION and coll.community.name == COMMUNITY: continue

    print(f"\033[1;44;33m{collection.community.name}  \033[1;45;37m{collection.name}\033[0;40m")

    print(len(d.get_items(collection, Item)))
#    for item in d.get_items(collection, Item)[:1]:
#        if not item.process(d, entity_coll, authors): exit(4)

#    break

"""
What should happen
==================

- Loop over items one-by-one
- - Get linked authors for item
- - Create and link new author where needed
"""
