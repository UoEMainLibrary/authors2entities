import itertools
from collections import defaultdict
from difflib import SequenceMatcher

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

titles = defaultdict(lambda: [])

if (d := DSpaceAPI.start(HOST, PORT, USER, PASS)) is None: exit(1)

for coll in d.yield_collections():
    for item in d.get_items(coll, Item):
        titles[group_key(item.title)].append(item)

for i in sorted(titles.keys()):
    pairs = []

    for a1, a2 in itertools.combinations(titles[i], 2):
        t1, t2 = a1.title, a2.title
        d = SequenceMatcher(None, t1, t2).ratio()
        if d > 0.8:
            pairs.append((t1, t2))

    if len(pairs) == 0: continue

    print("#" * 75, i)

    groups = to_groups(pairs)

    for n in sorted(groups.keys()):
        if len(groups[n]) > 1:
            print(f"\n{n}\n")
            print("\n".join(sorted(groups[n])))

##############################################################################
