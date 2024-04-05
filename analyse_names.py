from dataclasses import dataclass
from collections import Counter
import Levenshtein

import regex

import .tidy

##############################################################################

@dataclass
class Entry:
    name:  str
    fixed: str
    pat:   str
    comm:  str

    @classmethod
    def make(cls, s):
        name, comm = s.split("|")
        fixed = tidy.tidy(name.strip())
        code  = tidy.encode(fixed)

        return cls(name, fixed, code, comm)

##############################################################################

CUTOFF = 8

with open("names.dat", "r") as f:
    entries = [ Entry.make(s.strip()) for s in f.readlines() ]

pat_counts  = Counter([ e.pat for e in entries ])
comm_counts = Counter([ e.comm for e in entries if pat_counts[e.pat] < CUTOFF ])

surnames = [ e.fixed.split(",")[0] for e in entries ]

#for e in entries:
#    if ";" in e.name:
#        print(f"{e.pat}   {e.name} -> {e.fixed}")

#for e in entries:
#    if (c := pat_counts[e.pat]) < CUTOFF:
#        print(f"{e.name[:100]}\t{e.fixed}\t{e.pat}\t{c}\t{e.comm}")
#        print(f"{e.name[:100]}\t{e.fixed[:100]}\t{e.pat[:100]}\t{c}\t{e.comm}")

#for k, v in pat_counts.items(): print(f"{v:8d}   {k}")

#for k, v in comm_counts.items(): print(f"{v:8d}   {k}")

#for e in entries:
#    if len([ c for c in e.pat if c == "/"]) > 1:
#    if "/" not in e.pat:
#        print(f"{e.pat}   {e.name} -> {e.fixed}")

#for e in entries:
#    for w in e.fixed.split():
#        for c in w:
#            if not regex.search("[A-Za-z.,-]", c): print(c)

#for s in sorted([ name[0] for name in surnames ]):
#    print(s)

#print(Levenshtein.ratio("Smith", "Smyth"))

#print(len(surnames))

for name in surnames: print(name)
