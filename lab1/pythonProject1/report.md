# LFA lab 1  (Variant 16)

### Course: Formal Languages & Finite Automata
### Author: Nidelcu Elena

----


## Objectives:
* Discover what a language is and what it needs to have in order to be considered a formal one;

* Provide the initial setup for the evolving project that you will work on during this semester. You can deal with each laboratory work as a separate task or project to demonstrate your understanding of the given themes, but you also can deal with labs as stages of making your own big solution, your own project. Do the following:

    a. Create GitHub repository to deal with storing and updating your project;

    b. Choose a programming language. Pick one that will be easiest for dealing with your tasks, you need to learn how to solve the problem itself, not everything around the problem (like setting up the project, launching it correctly and etc.);

    c. Store reports separately in a way to make verification of your work simpler (duh)

* According to your variant number, get the grammar definition and do the following:

    a. Implement a type/class for your grammar;

    b. Add one function that would generate 5 valid strings from the language expressed by your given grammar;

    c. Implement some functionality that would convert and object of type Grammar to one of type Finite Automaton;

    d. For the Finite Automaton, please add a method that checks if an input string can be obtained via the state transition from it;
   


## Implementation description

* About 2-3 sentences to explain each piece of the implementation.
  1.  task a:
  I implemented manualy the type of the grammar by making a list of terminals, non-terminals, start element and a dictionary with rules, where the index is the non-terminal symbol, and its values are with what we are replacing this non-terminal
  2. task b:
  in this function I create a string, starting the word with start symbol 'S', looping through the dictionary, and if a non-terminal symbol is in the word, I replace this non-terminal with a random choise from the list which belongs to the index. It executes until no non-terminal symbol is left in the word
  3. task c:
  Here, I do a pairs with every index with its every value, make tuples from them, add them as an index in a new dictionary, and their value is the 2nd character from that string, and if there is no uppercase letter, I set X (final state) as value. 
  
  This algorithm works for every grammar, not only with mine!!!
  4. task d:
  Here I create a new string which will reconstruct the word. Then I check each character in the word, and if it is not in the VT list, the word does not exist. If every character is in the list, if the pair of non-terminal and the current character doesn't exist as an index in the dictionary, the word (the transition) doesn't exist. If the final word I get without that 'X' at the end is equal to the input word, the word exists, otherwise, the word does not exist.


* Code snippets from your files.

```
# task a
VN = ['S', 'A', 'B']
VT = ['a', 'b', 'c', 'd']
S = 'S'
P = {
    'S': ['bS', 'dA'],
    'A': ['aA', 'dB', 'b'],
    'B': ['cB', 'a']
}
```
```
# task b
def transform_word(input_word):
    while not(input_word.islower()):
        for i in P:
            if i in input_word:
                input_word = input_word.replace(i, random.choice(P[i]))
        return input_word
```
```
# task c
def convert2FA():
    for i in P:
        for j in P[i]:
            pair = (i,j[0])
            if len(j) == 2:
                ro[pair] = j[1]
            else:
                ro[pair] = F
```
```
# task d
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
```

* If needed, screenshots.


## Conclusions / Screenshots / Results

Working on this lab I understood better how grammar and finite automata work, by choosing python, I implemented the algorithms for creating new words according to the grammar, generating a finite automaton from that grammar and for checking whether a string belongs to a grammar or not. Finally, through testing I assured that those algorithms work. e.g. The last algorithm I tested with 10 words I new before whether they are or not in the language, and the results were correct.

**Results:**
![Results](E:\labs\LFA\lab1\screenshot.png)

## References
me