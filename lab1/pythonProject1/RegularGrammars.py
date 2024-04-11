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

# a)
VN = ['S', 'A', 'B']
VT = ['a', 'b', 'c', 'd']
S = 'S'
P = {
    'S': ['bS', 'dA'],
    'A': ['aA', 'dB', 'b'],
    'B': ['cB', 'a']
}
check_type1()
Q = VN
Q.append('X')
sigma = VT
q0 = S
F = 'X'

ro = {}

# print('b)')
# for j in range(5):
#     word = 'S'
#     while word != word.lower():
#         word = transform_word(word)
#     print(word)
#     print(len(word))
#
# print()
# print('c)')
# convert2FA()
# print(ro)
# print()
# for i in ro:
#     print(i, ' = ', ro[i])
#
# print()
# print('d)')
# words_to_test = ['ddabbc', 'db', 'dadcca', 'aabb', 'dabd', 'dab', 'dd', 'bdab', 'ddbbc', 'dda']
# for word in words_to_test:
#     check_word(word)

if check_type3():
    print('Type 3')
elif check_type2():
    print('Type 2')
elif check_type1():
    print('Type 1')
else:
    print('Type 0')