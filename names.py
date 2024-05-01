import regex

def tidy_single(s):
    if any([ not c.isupper() for c in s]): return s

    if len(s) <= 3:
        return " ".join([ f"{c}." for c in s ])

    return s

def tidy(s):
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

    s = " ".join([ tidy_single(w) for w in a ])

    s = s.replace(",,", ",")

    return s

def encode(s):
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


"""
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

"""
