from api import DSpaceAPI

import csv

import tidy

HOST = "localhost"
PORT = "8080"
USER = "root%40localhost"
PASS = "dspace"

COMMUNITY  = "Entities"
COLLECTION = "Entities"

total = 0

##############################################################################

def yield_items(d):
    with open("items.csv", "w", newline = "") as f:
        writer = csv.writer(f, dialect = "unix")

        for comm_name, comm_uuid in d.get_all_communities():
            if comm_name == COMMUNITY: continue

#        print(f"\n{comm_name} - {comm_uuid}")

            for coll_name, coll_uuid in d.get_collections(comm_uuid):
                items = d.get_items(coll_uuid)
#                total += len(items)

#            print(f"    {coll_name} - {coll_uuid}: {len(items)} {total}")

                for item in items:
                    yield comm_name, coll_name, item
#                writer.writerow([ comm_name, coll_name, item.uuid, item.title, *item.authors])

##############################################################################

def create_entities(d, entity_coll):
    for comm, coll, item in yield_items(d):
        for author in item.authors:
            surname, forename = author.split(", ")

            print(f"Item {item.uuid} has author {author}")

            # check if author already exists!!!

            if (ret := d.create_workspace_item(entity_coll)) is None: return

            wsitem, author_uuid = ret

            if d.patch_item(wsitem, surname, forename) is None: return
            if d.add_image(wsitem, "black_pixel.png") is None: return
            if d.submit_workspace_item(wsitem) is None: return
            if d.add_author_to_item(author_uuid, item.uuid) is None: return

            return

##############################################################################

d = DSpaceAPI(HOST, PORT)

if d.options() is None: exit(1)
if d.login(USER, PASS) is None: exit(2)

if (comm := d.find_community("Entities")) is None: exit(3)
if (coll := d.find_collection(comm, "Entities")) is None: exit(4)

create_entities(d, coll)
