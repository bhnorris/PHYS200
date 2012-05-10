import numpy as np

def intoArray(x):
    x = x[:len(x)-1]
    x = x.split(' ')
    i = 0
    for num in x:
        x[i] = int(x[i])
        i += 1
    x = np.array(x)
    return x

def package(x):
    f = open(x)
    pkg = []
    L = -1
    for line in f:
        if line[0] == '#':
            pkg.append([])
            L += 1
        else:
            pkg[L].append(intoArray(line))
    return pkg

