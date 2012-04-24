
def engdictdefine():
    fin = open('words.txt')
    words = dict()
    for line in fin:
        word = line.strip()
        words[word] = 0
    return words

def histogram(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)
    return d

def print_hist(h):
    t = h.keys()
    t.sort
    for c in t:
        print c, h[c]

def reverse_lookup(d,v):
    l = list()
    for c in d:
        if d[c] == v:
            l.append(c)
    return l

def invert_dict(d):
    inv = dict()
    for key in d:
        val = d[key]
        inv.setdefault(val, []).append(key)
    return inv


