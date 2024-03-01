# LFA lab 1  (Variant 16)

### Course: Formal Languages & Finite Automata
### Author: Nidelcu Elena

----


## Objectives:
* Understand what an automaton is and what it can be used for.

* Continuing the work in the same repository and the same project, the following need to be added: 

    a. Provide a function in your grammar type/class that could classify the grammar based on Chomsky hierarchy.

    b. For this you can use the variant from the previous lab.

* According to your variant number (by universal convention it is register ID), get the finite automaton definition and do the following tasks:

    a. Implement conversion of a finite automaton to a regular grammar.

    b. Determine whether your FA is deterministic or non-deterministic.

    c. Implement some functionality that would convert an NDFA to a DFA.

    d. Represent the finite automaton graphically (Optional, and can be considered as a bonus point)

## Implementation description

* About 2-3 sentences to explain each piece of the implementation.
  1. task a (from 1st lab):
  I implemented 2 functions to count how many terminal and non-terminal symbols are there in the word (I counted how many uppercase or lowercase letters are in the word). Also, I implemented functions to check if a grammar belongs to type 3, type 2 and type 1. A grammar belongs to type 3 if the key is a single uppercase letter and if either the value is a single lowercase letter or one uppercase letter which is always in the right or always in the left, followed or preceded by one lowercase letter. A grammar is of type 2 if the key contains exactly 1 non-terminal symbol and the value contains only one or zero non-terminals. Type 1 is any grammar in which the key is not longer than the value. If all 3 functions returned false, the grammar is of type 0.
  2. task a (from 2nd lab):
  I created a dictionary P in which I stored all keys from dictionary ro as keys and as values I stored a list with a lowercase letter followed by a uppercase letter.
  3. task b:
  I checked if a grammar contains a key-value where value consists of 0 or 2 or more elements
  4. task c:
  For this I created functions for returning to what state goes a word with every terminal symbol. They return either an existing state, or through recursion return a new created state, or final state F, or dead state D. I create new state if there is a value which is not also a key. Also I added a function which returns true or false if all states that are values are also keys. I continue this process until this function will return true.
  5. task d:
  I drew a graph of DFA using networkx and matplotlib.pyplot libraries. Nodes are keys of DFA dictionary, edges are all pairs of a key and every its value. 

* Code snippets from your files.

```
# task a
def count_n(s):
    count = 0
    for i in s:
        if i.isupper():
            count = count + 1
    return count

def count_t(s):
    count = 0
    for i in s:
        if i.islower():
            count = count + 1
    return count

def check_type3():
    for i in P.keys():
        if not (i.isupper() and len(i) == 1):
            return False
    t = True
    for i in P.values():
        for j in i:
            if not ((count_n(j) == 1 and j[-1].isupper()) or count_n(j) == 0):
                t = False
    if t:
        print("Right linear")
        return True
    else:
        t = True
        for i in P.values():
            for j in i:
                if not (count_n(j) == 1 and j[0].isupper()) or count_n(j) == 0:
                    t = False
        if t:
            print('Left linear')
        return t

def check_type2():
    for i in P.keys():
        if not (i.isupper() and len(i) == 1):
            return False
    for i in P.values():
        for j in P[i]:
            if count_n(j) == 1 or count_n(j) == 0:
                return True
            else:
                return False

def check_type1():
    for i in P.keys():
        for j in P[i]:
            if len(i) > len(j):
                return False
    return True
```
```
# task a
ro = {
    ('S', 'a'): ['A'],
    ('S', 'b'): ['S'],
    ('A', 'b'): ['A', 'B'],
    ('B', 'a'): ['B'],
    ('B', 'b'): ['']
}
VN = []
VT = []

for a, b in ro.keys():
    VN.append(a)
    VT.append(b)

VN = list(set(VN))
VT = list(set(VT))

P = {}

print('a)')
for i in VN:
    P[i] = []
for i in ro:
    for j in ro[i]:
        P[i[0]].append(i[1] + j)
for i in P:
    print(i, ':', P[i])
```
```
# task b
t = True
for i in ro.values():
    if len(i) != 1:
        t = False
if t:
    print('Deterministic FA')
else:
    print('Non-deterministic FA')
```
```
# task c
def transition_a(x):
    state_a = ''
    if x in P.keys():
        for i in P[x]:
            if i[0] == 'a':
                if len(i) == 1:
                    state_a = state_a + 'F'
                else:
                    state_a = i[1] + state_a
    else:
        if x == 'D' or x == 'F':
            return 'D'
        tra = ''
        for i in x:
            tra = transition_a(i) + tra
        tra = tra.replace('D', '')
        state_a = tra
    if state_a == '':
        state_a = 'D'
    return state_a


def transition_b(x):
    state_b = ''
    if x in P.keys():
        for i in P[x]:
            if i[0] == 'b':
                if len(i) == 1:
                    state_b = state_b + 'F'
                else:
                    state_b = i[1] + state_b
    else:
        if x == 'D' or x == 'F':
            return 'D'
        trb = ''
        for i in x:
            trb = transition_b(i) + trb
        trb = trb.replace('D', '')
        state_b = trb
    if state_b == '':
        state_b = 'D'
    return state_b


def is_complete_DFA_states():
    for i in DFA.values():
        for j in i:
            if j not in DFA.keys():
                return False
    return True


def new_state():
    for i in DFA.values():
        for j in i:
            if j not in DFA.keys():
                return j
                
DFA = {}
DFA['S'] = transition_a('S'), transition_b('S')
while not(is_complete_DFA_states()):
    nst = new_state()
    if nst is not None:
        DFA[nst] = (transition_a(nst), transition_b(nst))
```
```
# Create a directed graph
G = nx.DiGraph()

# Add nodes
nodes = []
for key in DFA.keys():
    G.add_node(key)

# Add edges
edge_labels = {}
for key in DFA.keys():
    if DFA[key][0] != DFA[key][1]:
        G.add_edge(key, DFA[key][0])
        edge_labels[(key, DFA[key][0])] = 'a'
        G.add_edge(key, DFA[key][1])
        edge_labels[(key, DFA[key][1])] = 'b'
    else:
        G.add_edge(key, DFA[key][0])
        edge_labels[(key, DFA[key][0])] = 'a,b'

# Draw the graph
pos = nx.spring_layout(G)  # Position nodes using the spring layout algorithm
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold', arrows=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Display the plot
plt.show()
```
## Conclusions / Screenshots / Results

Working on this lab I understood better how to check to which type of chompsky belongs a grammar, to convert from FA to regular grammar, to check if it is a deterministic FA or not, to convert from NFA to DFA and to plot a DFA on a graph, I implemented the algorithms for reaching these objectives. Finally, through testing I assured that those algorithms work.

**Results:**
![Results](E:\labs\LFA\lab1\lab2-a.jpg)
![Results](E:\labs\LFA\lab1\lab2.jpg)
![Results](E:\labs\LFA\lab1\lab2-d.png)
## References
me