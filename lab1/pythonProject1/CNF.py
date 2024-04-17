def epsilon():
    for i in P:
        for j in P[i]:
            if j == 'eps':
                P[i].remove(j)
                for k in P:
                    for l in P[k]:
                        if i in l:
                            if l == i:
                                P[k].append('eps')
                            else:
                                P[k].append(l.replace(i, ''))
def unit():
    for i in P:
        for j in P[i]:
            if j.isupper() and len(j) == 1:
                for k in P:
                    if j == k:
                        for l in P[k]:
                            P[i].append(l)
                P[i].remove(j)
def inaccessible():
    products = 'S'
    for i in P:
        products += P[i]
    inaccess = ''
    for i in P:
        if i not in products:
            inaccess += i
            inaccess += P[i]
    for i in inaccess:
        P.pop(i)
def unproductive():
    unproduct = ''
    for i in P:
        term = False
        for j in P[i]:
            if j.islower():
                term = True
        if not term:
            unproduct += i
    unproduct = unproduct.replace('S', '')
    for i in unproduct:
        P.pop(i)
    for i in P:
        for j in P[i]:
            if unproduct in j:
                P[i].remove(j)
def cnf():
    for i in P:
        for j in range(len(P[i])):
            if not ((len(P[i][j]) == 1 and P[i][j].islower()) or (len(P[i][j]) == 2 and P[i][j].isupper())):
                for k in P1:
                    if P1[k] in P[i][j]:
                        P[i][j] = P[i][j].replace(P1[k], k)

# Testing epsilon productions
P = {
    'S' : ['ADCa'],
    'A' : ['a'],
    'B' : ['eps'],
    'C' : ['ED', 'eps'],
    'D' : ['BC', 'b']
}
T = {'S': ['ADCa', 'ADa', 'ACa', 'Aa'], 'A': ['a'], 'B': [], 'C': ['ED', 'E'], 'D': ['BC', 'b', 'C', 'B']}
epsilon()
print(P)
print(P == T)

# Testing unit productions
P = {
    'S' : ['AB'],
    'A' : ['a'],
    'B' : ['C', 'b'],
    'C' : ['D'],
    'D' : ['E'],
    'E' : ['a']
}
T = {'S': ['AB'], 'A': ['a'], 'B': ['b', 'a'], 'C': ['a'], 'D': ['a'], 'E': ['a']}
unit()
unit()
print(P)
print(P == T)

# Testing inaccessible symbols
P = {
    'S' : 'AB',
    'A' : 'a',
    'B' : 'C',
    'C' : 'aB',
    'D' : 'E',
    'E' : 'a'
}
T = {'S': 'AB', 'A': 'a', 'B': 'C', 'C': 'aB'}
inaccessible()
print(P)
print(P == T)

# Testing unproductive symbols
P = {
    'S' : ['AB'],
    'A' : ['aA', 'a'],
    'B' : ['b', 'CA'],
    'C' : ['bD', 'CA']
}
T = {'S': ['AB'], 'A': ['aA', 'a'], 'B': ['b']}
unproductive()
print(P)
print(P == T)

# Testing cnf
P = {
    'S' : ['abAB'],
    'A' : ['aSaB', 'BS', 'aA', 'b'],
    'B' : ['BA', 'ababB', 'b']
}
P1 = {
    'X1' : 'abB',
    'X2' : 'AB',
    'X3' : 'aS',
    'X4': 'aB',
    'X5': 'ab',
    'X6': 'a'
}
T = {'S': ['X5X2'], 'A': ['X3X4', 'BS', 'X6A', 'b'], 'B': ['BA', 'X5X1', 'b']}
cnf()
print(P)
print(P == T)