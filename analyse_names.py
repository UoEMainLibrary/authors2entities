from dataclasses import dataclass
from collections import Counter

import regex

##############################################################################

@dataclass
class Entry:
    name:  str
    fixed: str
    pat:   str
    comm:  str

    @classmethod
    def tidy(cls, s):
        for r, t in [
            ("\s+",        " "),
            ("[ ,;]$",     ""),   # kill junk at end
            (" ?[.,]+",    "."),  # remove spaces before dots and commas
            ("[.,](?! )",  ". "), # ensure dots and commas are followed by a space
                ]:
            s = regex.sub(r, t, s)

        for t in [ "de", "do", "da", "dos", "van", "van de", "van der", "van den" ]:
            if s.endswith(" " + t):
                s = t + " " + s[:-1-len(t)]

        # ensure trailing initials are preceded by a comma
        if "," not in s and (m := regex.search("(\w)((\s+\w\.)+$)", s)) is not None:
            s = s[:m.start(1)] + m.group(1) + "," + m.group(2)

        # add dot after single letter at end
        if regex.search("\s\w$", s): s += "."

        # "Russel. W."
        if (m := regex.search("(\w\w)\. (\w\.)$", s)) is not None:
            s = s[:m.end(1)] + ", " + m.group(2)

        # move leading initials to end
        if (m := regex.search("^((\w\. )+)(\w)", s)) is not None:
            s = s[m.start(3):] + " " + m.group(2).strip()

        # "Barbosa. Maria Regina V." -> change first dot to comma
        if "," not in s: s = regex.sub("(\w\w+)\. ", r"\1, ", s)

        # "McDougall J." -> needs comma
        if "," not in s: s = regex.sub("(\w\w+) (\w\.)", r"\1, \2", s)

        # trailing comma
        s = regex.sub(",$", ".", s)

        return s

    @classmethod
    def encode(cls, s):
        for r, t in [
                ("(\w|['’‐-])+", "A"),
                (" \w\.",        "i"),
                ]:
            s = regex.sub(r, t, s)

        for r, t in [
                (",",              "/"),
                ]:
            s = s.replace(r, t)

        return s

    @classmethod
    def make(cls, s):
        name, comm = s.split("|")
        fixed = cls.tidy(name.strip())
        code  = cls.encode(fixed)

        return cls(name, fixed, code, comm)

##############################################################################

CUTOFF = 30

with open("names.dat", "r") as f:
    entries = [ Entry.make(s.strip()) for s in f.readlines() ]

pat_counts  = Counter([ e.pat for e in entries ])
comm_counts = Counter([ e.comm for e in entries if pat_counts[e.pat] < CUTOFF ])

#for e in entries:
#    if e.fixed != e.name:
#        print(f"{e.pat}   {e.name} -> {e.fixed}")

#for e in entries:
#    if (c := pat_counts[e.pat]) < CUTOFF:
#        print(f"{e.name[:100]}\t{e.fixed}\t{e.pat}\t{c}\t{e.comm}")
#        print(f"{e.name[:100]}\t{e.fixed[:100]}\t{e.pat[:100]}\t{c}\t{e.comm}")

for k, v in pat_counts.items(): print(f"{v:8d}   {k}")

#for k, v in comm_counts.items(): print(f"{v:8d}   {k}")

#for e in entries: print(e.name)
