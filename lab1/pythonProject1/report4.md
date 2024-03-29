# LFA lab 4  (Variant )

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
  to do this task I appended step by step tokens to generated_string. If it contains chars between [], i generate a random choice from those chars, if it has char and an '*' after it, I generate 0 to 5 (random) occurrences of that char, if it's '+', 1 to 5 occurrences, if it has a number between {}, I generate that number of occurrences of that char, and if nothing is specified, I generate just that char. Examples are given below.
  2. task 2:
  I just generated random integer from 1 to 5
  3. task 3:
  In the fuction I pass all the array and check each character. For each functional symbol, like '[]{}()*+' I describe what it is doing, and for alphanumeric characters I write: Match ... But if there is a group of characters between [], I write 'Choose one character from ...'

* Code snippets from your files.

```
# task 1
random.choice(['S', 'T'])
'L'
random.choice(['X', 'Y', 'Z']) * 2

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