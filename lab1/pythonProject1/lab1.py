import random

def transform_word(input_word):
    while not(input_word.islower()):
        for i in P:
            if i in input_word:
                input_word = input_word.replace(i, random.choice(P[i]))
        return input_word

def convert2FA():
    for i in P:
        for j in P[i]:
            pair = (i,j[0])
            if len(j) == 2:
                ro[pair] = j[1]
            else:
                ro[pair] = F

def check_word(word):
    str = S
    for i in word:
        if i not in VT:
            print(word + ' does not exist')
            return False
        if (str[-1], i) in ro:
            str = str.replace(str[-1], i + ro[(str[-1], i)])
        else:
            print(word + ' does not exist')
            return False
    if str == word + F:
        print(word + ' belongs to the grammar')
    else:
        print(word + ' does not exist')
        return False

# a)
VN = ['S', 'A', 'B']
VT = ['a', 'b', 'c', 'd']
S = 'S'
P = {
    'S': ['bS', 'dA'],
    'A': ['aA', 'dB', 'b'],
    'B': ['cB', 'a']
}

Q = VN
Q.append('X')
sigma = VT
q0 = S
F = 'X'

ro = {}

print('b)')
for j in range(5):
    word = 'S'
    while word != word.lower():
        word = transform_word(word)
    print(word)
    print(len(word))

print()
print('c)')
convert2FA()
for i in ro:
    print(i, ' = ', ro[i])

print()
print('d)')
words_to_test = ['ddabbc', 'db', 'dadcca', 'aabb', 'dabd', 'dab', 'dd', 'bdab', 'ddbbc', 'dda']
for word in words_to_test:
    check_word(word)