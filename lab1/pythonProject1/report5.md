# LFA lab 5  (Variant 16)

### Course: Formal Languages & Finite Automata
### Author: Nidelcu Elena

----


## Objectives:
* Learn about Chomsky Normal Form (CNF);
* Get familiar with the approaches of normalizing a grammar
* Implement a method for normalizing an input grammar by the rules of CNF

    a. The implementation needs to be encapsulated in a method with an appropriate signature (also ideally in an appropriate class/type).

    b. The implemented functionality needs executed and tested.

    c. A BONUS point will be given for the student who will have unit tests that validate the functionality of the project.

    d. Also, another BONUS point would be given if the student will make the aforementioned function to accept any grammar, not only the one from the student's variant.
   


## Implementation description

* About 2-3 sentences to explain each piece of the implementation.
  1.  task a:
  I encapsulated every step of transforming CFG to CNF into appropriate function: 1. removing epsilon-productions, 2. removing unit-productions, 3. removing inaccessible symbols, 4. removing unproductive symbols, 5. CNF
  
  * First, in the epsilon() function I passed all the dictionary (grammar) and if the only value of one key is 'eps', I remove that 'eps' and pass again all the grammar and if a meet the key where I deleted the 'eps' in other key's values, I replace it with ''.
  * In the unit() function I passed all the dictionary and if I found an element of the form 'A' : 'B' (one non-terminal -> one non-terminal), I replace the value with its value where it is a key in the grammar, until the remaining form is not 'A' : 'B'.
  * In the inaccessible() function I added all the characters which are values in one string, and in the other string I stored all the keys of the dictionary which are not in the first string. Finally, I deleted all the elements from the grammar whose keys belong to the second string.
  * In the unproductive() function I store in a string all the keys which does not have a terminal symbol as production. Then, I remove from the grammar all elements whose keys are in that string, and I also remove the productions which contain that character.
  * In the CNF section I created another grammar P1 to store productions of the form 'X1' : 'abB', to help me to replace the productions which are not in the CNF. In the cnf() function I check the production, and if it is not CNF, then I find in P1 a production which matches to the current production and replace it.
  2.  task b:
  for every step I created a dict of rules to test the functions
  3.  task c:
  each time I tested created dict with according function and printing the dict after it. I stored the correct answer in another grammar and after execution of the functions I checked if they are equal.

* Code snippets from your files.

```
# task a (example of one function)
def unit():
    for i in P:
        for j in P[i]:
            if j.isupper() and len(j) == 1:
                for k in P:
                    if j == k:
                        for l in P[k]:
                            P[i].append(l)
                P[i].remove(j)
```
```
# task b (exampple of one test)
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
cnf()
print(P)
```
```
# task c (example of another test)
P = {
    'S' : ['ADCa'],
    'A' : ['a'],
    'B' : ['eps'],
    'C' : ['ED', 'eps'],
    'D' : ['BC', 'b']
}
epsilon()
print(P)
```

* If needed, screenshots.


## Conclusions / Screenshots / Results

Working on this lab I understood better how to normalize a CFG. I implemented 5 methods for every step for reaching CNF from CFG. I executed and tested functionality for removing epsilon productions, unit productions, inaccessible symbols, unproductive symbols and transforming to CNF.

## References
me