from dataclasses import dataclass
from collections import Counter
import Levenshtein

import regex

##############################################################################

@dataclass
class Entry:
    name:  str
    fixed: str
    pat:   str
    comm:  str

    @classmethod
    def tidy_single(cls, s):
        if any([ not c.isupper() for c in s]): return s

        if len(s) <= 3:
            return " ".join([ f"{c}." for c in s ])

        return s

    @classmethod
    def tidy(cls, s):
        for r, t in [
                ("^;",         ""),
                ("\.,",        ","),
                ("\.",         " "),
                ("[ ,;]$",     ""),   # kill junk at end
                ("\,(?!\s)",   " "),
                ("\s+",        " "),
        ]:
            s = regex.sub(r, t, s)

        for t in [ "de", "do", "da", "dos", "van", "van de", "van der", "van den" ]:
            if s.endswith(" " + t):
                s = t + " " + s[:-1-len(t)]

        s = s.replace(" ;", "; ")
        s = s.replace(" , ", " ")

        a = s.split()

        # move initials to end

        if len(a) > 1 and len(a[0]) == 1:
            i = 0

            while i < len(a) and len(a[i]) == 1: i += 1

            if i < len(a): a = a[i:] + a[:i]

        if len(a) > 1 and len(a[0]) > 1 and len(a[1]) == 1:
            a = [ a[0] + "," ] + a[1:]

        s = " ".join([ cls.tidy_single(w) for w in a ])

        s = s.replace(",,", ",")

        return s

    @classmethod
    def old_tidy(cls, s):
        for r, t in [
            ("^;",         ""),
            ("\s+",        " "),
            (" ?[.,]+",    "."),  # remove spaces before dots and commas
            ("[.,](?! )",  ". "), # ensure dots and commas are followed by a space
                ]:
            s = regex.sub(r, t, s)

        s = s.strip()

        for t in [ "de", "do", "da", "dos", "van", "van de", "van der", "van den" ]:
            if s.endswith(" " + t):
                s = t + " " + s[:-1-len(t)]

        # two or three trailing consecutive uppercase letters
        if (m := regex.search("([A-Z])([A-Z])([A-Z])\.$", s)) is not None:
            s = s[:m.start(1)] + m.group(1) + ". " + m.group(2) + ". " + m.group(3)

        if (m := regex.search("([A-Z])([A-Z])\.$", s)) is not None:
            s = s[:m.start(1)] + m.group(1) + ". " + m.group(2)

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

        # isolated dot
        s = s.replace(" . ", " ")

        return s.strip()

    @classmethod
    def encode(cls, s):
        for r, t in [
                ("(\w|['’‐-])+ ?", "A"),
                ("\w\.\s?",        "i"),
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
