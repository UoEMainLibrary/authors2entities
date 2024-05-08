from api import *

HOST = "localhost"
PORT = "8080"
USER = "root%40localhost"
PASS = "dspace"

COMMUNITY  = "Entities"
COLLECTION = "Entities"

if (d := DSpaceAPI.start(HOST, PORT, USER, PASS)) is None: exit(1)
if (coll := d.get_or_create_special_collection(COMMUNITY, COLLECTION)) is None: exit(2)

with open("author_fixes.dat") as f:
    for line in f.readlines():
        new, old = [ s.strip() for s in line.split("<-", 1) ]

        print(f"\033[1;32m{new}\033[0;37m")

        if (new_author_uuid := d.get_author_uuid(coll, new)) is None:
            new_author_uuid = d.create_author_entity(coll, new)
            if new_author_uuid is None: break
            print(f"    \033[36mcreated\033[37m with uuid {new_author_uuid}")
        else:
            print(f"    \033[33mfound\033[37m with uuid {new_author_uuid}")

        for author in [ s.strip() for s in old.split("|") ]:
            if (author_uuid := d.get_author_uuid(coll, author)) is None:
                print(f"    \033[1;31m{author}\033[0;37m not found; skipping")
                continue

            print(f"    absorbing \033[1;33m{author}\033[0;37m with uuid {author_uuid}")

            d.absorb_author(new_author_uuid, author_uuid)
