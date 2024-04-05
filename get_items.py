from api import DSpaceAPI

import csv

HOST = "localhost"
PORT = "8080"
USER = "root%40localhost"
PASS = "dspace"

COMMUNITY  = "Entities"
COLLECTION = "Entities"

total = 0
d = DSpaceAPI(HOST, PORT)

if d.options() is None: exit(1)
if d.login(USER, PASS) is None: exit(2)

with open("items.csv", "w", newline = "") as f:
    writer = csv.writer(f, dialect = "unix")

    for comm_name, comm_uuid in d.get_all_communities():
        if comm_name == COMMUNITY: continue

        print(f"\n{comm_name} - {comm_uuid}")

        for coll_name, coll_uuid in d.get_collections(comm_uuid):
            items = d.get_items(coll_uuid)
            total += len(items)

            print(f"    {coll_name} - {coll_uuid}: {len(items)} {total}")

            for item in items:
                writer.writerow([ comm_name, coll_name, item.uuid, item.title, *item.authors])
