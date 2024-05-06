from api import *

HOST = "localhost"
PORT = "8080"
USER = "root%40localhost"
PASS = "dspace"

COMMUNITY  = "Entities"
COLLECTION = "Entities"


d = DSpaceAPI(HOST, PORT)

if d.options() is None: exit(1)
if d.login(USER, PASS) is None: exit(2)

if (comm := d.find_community(COMMUNITY)) is None: exit(3)
if (coll := d.find_collection(comm, COLLECTION)) is None: exit(4)

print("Reading existing authors...")
authors = { item.fullname: item.uuid for item in d.get_items(coll, Author) }
print(f"Read {len(authors)} authors")

with open("author_fixes.dat") as f:
    for line in f.readlines():
        new, old = [ s.strip() for s in line.split("<-", 1) ]

        print(f"\033[1;32m{new}\033[0;37m")

        if new in authors:
            new_author_uuid = authors[new]
            print(f"    \033[33mfound\033[37m with uuid {new_author_uuid}")
        else:
            new_author_uuid = d.create_author_entity(coll, new)
            if new_author_uuid is None: break

            print(f"    \033[36mcreated\033[37m with uuid {new_author_uuid}")

        for author in [ s.strip() for s in old.split("|") ]:
            if author not in authors:
                print(f"    \033[1;31m{author}\033[0;37m not found; skipping")
                continue

            print(f"    absorbing \033[1;33m{author}\033[0;37m with uuid {authors[author]}")

            d.absorb_author(new_author_uuid, authors[author])
