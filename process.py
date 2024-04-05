from api import DSpaceAPI

import csv

import tidy

HOST = "localhost"
PORT = "8080"
USER = "root%40localhost"
PASS = "dspace"

COMMUNITY  = "Entities"
COLLECTION = "Entities"

#total = 0
#d = DSpaceAPI(HOST, PORT)

#if d.options() is None: exit(1)
#if d.login(USER, PASS) is None: exit(2)

with open("items.csv") as f:
    reader = csv.reader(f, dialect = "unix")

    for row in reader:
        item_uuid = row[2]
        for name in row[4:]:
            s = tidy.tidy(name)
            print(f"{name} -> {s} [{tidy.encode(s)}]")
        break
