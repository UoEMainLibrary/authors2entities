import regex

def tidy_single(s):
    if any([ not c.isupper() for c in s]): return s

    if len(s) <= 3:
        return " ".join([ f"{c}." for c in s ])

    return s

def tidy(s):
    for r, t in [
            (r"^;",         ""),
            (r"\.,",        ","),
            (r"\.",         " "),
            (r"[ ,;]$",     ""),   # kill junk at end
            (r"\,(?!\s)",   " "),
            (r"\s+",        " "),
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
            (r"(\w|['’‐-])+ ?", "A"),
            (r"\w\.\s?",        "i"),
    ]:
        s = regex.sub(r, t, s)

        for r, t in [
                (",",              "/"),
        ]:
            s = s.replace(r, t)

    return s
