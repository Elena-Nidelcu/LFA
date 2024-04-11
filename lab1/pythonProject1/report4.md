# LFA lab 4  (Variant 4)

### Course: Formal Languages & Finite Automata
### Author: Nidelcu Elena

----


## Objectives:
* Write and cover what regular expressions are, what they are used for

* Below you will find 3 complex regular expressions per each variant. Take a variant depending on your number in the list of students and do the following:

    1.  Write a code that will generate valid combinations of symbols conform given regular expressions (examples will be shown).

    2. In case you have an example, where symbol may be written undefined number of times, take a limit of 5 times (to evade generation of extremely long combinations);

    3. Bonus point: write a function that will show sequence of processing regular expression (like, what you do first, second and so on)

## Implementation description

* About 2-3 sentences to explain each piece of the implementation.
  1.  task 1:
  to do this task I pass all the chars in the regex string. If it contains chars between [], I add to the word a random choice from those chars, if it has char and an '*' after it, I choose a random number between 0 and 5 and add that number of preceding char, similarly with '+', just with the difference that the number is beetween 1 and 5, if it has a number between {}, I add to the word the specified amount of chars.
  2. task 2:
  I just generated random integer from 1 to 5
  3. task 3:
  In the fuction I pass all the array and check each character. For each functional symbol, like '[]{}()*+' I describe what it is doing, and for alphanumeric characters I write: Match ... But if there is a group of characters between [], I write 'Choose one character from ...'

* Code snippets from your files.

```
# task 1
elif char == '+':
    pr_elem = regex[regex.index(char) - 1]
    word += pr_elem * random.randint(1, 5)
elif char == '{':
    curly_brace = True
    number = int(regex[regex.index(char) + 1 : regex.index('}')])
    word += random.choice(pr_group) * number

```
```
# task 2
'W' * random.randint(0, 5)
'Y' * random.randint(1, 5)
```
```
# task 3
elif char == '*':
    sequence.append("Match zero or more occurrences of the preceding element")
```

* If needed, screenshots.

## Conclusions / Screenshots / Results
In this lab, I explored the concept of regular expressions and their practical applications. For this lab, I implemented code to generate valid combinations of symbols conforming to given complex regular expressions. I limited repetitions to 5 times for patterns allowing an undefined number of repetitions to avoid generating excessively long combinations. Additionally, I implemented a function to show the sequence of processing a regular expression, providing a step-by-step explanation of how the pattern is matched.

**Results:**
![Results](E:\labs\LFA\lab1\screenshot.png)

## References
me