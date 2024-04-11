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

print('\nb)')
t = True
for i in ro.values():
    if len(i) != 1:
        t = False
if t:
    print('Deterministic FA')
else:
    print('Non-deterministic FA')

print('\nc)')
DFA = {}
DFA['S'] = transition_a('S'), transition_b('S')
while not(is_complete_DFA_states()):
    nst = new_state()
    if nst is not None:
        DFA[nst] = (transition_a(nst), transition_b(nst))

print('        a    b')
print('---------------')
for i in DFA:
    print(f"{i:<5s}", end='|  ')
    for j in DFA[i]:
        print(f"{j:<5s}", end='')
    print()

# d)
import networkx as nx
import matplotlib.pyplot as plt

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