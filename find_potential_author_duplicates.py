import itertools
from collections import defaultdict

from api import *

HOST = "localhost"
PORT = "8080"
USER = "root%40localhost"
PASS = "dspace"

COMMUNITY  = "Entities"
COLLECTION = "Entities"

##############################################################################

def group_key(s): return s[0:1].lower()

def to_groups(pairs):
    temp = defaultdict(lambda: len(temp))

    for a1, a2 in pairs: temp[a2] = temp[a1]

    groups = defaultdict(lambda: set())

    for a, n in temp.items():groups[n].add(a)

    return groups

##############################################################################

def get_authors_from_database():
    if (d    := DSpaceAPI.start(HOST, PORT, USER, PASS)) is None: exit(1)
    if (comm := d.find_community(COMMUNITY)) is None: exit(2)
    if (coll := d.find_collection(comm, COLLECTION)) is None: exit(3)

    return list(d.get_items(coll, Author))

def get_authors_from_file():
    items = []

    with open("names.dat", "r") as f:
        for line in f.readlines():
            author = names.tidy(line)

            if ", " in author: surname, forename = author.split(", ", 1)
            else:              surname, forename = author, ""

            items.append(Author("", surname, forename))

    return items

##############################################################################

#items   = get_authors_from_database()
items   = get_authors_from_file()

authors = defaultdict(lambda: [])

for item in items: #d.get_items(coll, Author):
    k = item.fullname[0].lower()

    authors[group_key(item.fullname)].append(item)

for i in sorted(authors.keys()):
    pairs = [ (a1, a2) for a1, a2 in itertools.combinations(authors[i], 2)
              if a1.similarity(a2) > 0.8 ]

    if len(pairs) == 0: continue

    print("#" * 75, i)
    groups = to_groups(pairs)

    for n in sorted(groups.keys()):
        if len(groups[n]) > 1:
            print(n, [ a.fullname for a in sorted(groups[n])])
