# LFA lab 3

### Course: Formal Languages & Finite Automata
### Author: Nidelcu Elena

----


## Objectives:
1. Understand what lexical analysis [1] is.
2. Get familiar with the inner workings of a lexer/scanner/tokenizer.
3. Implement a sample lexer and show how it works.

## Implementation description

* Define tokens

I defined a tokens tuple which contains how an identifiers, a number and a string are written, and also predefined identifiers which are used to manipulate images.
* Define regular expressions for tokens

Here I defined a regular expression for each token in the tokens tuple. e.g. declaration of a string regex means that a string may contain all characters except the '"'
* Define a rule to track line numbers

I defined a token rule t_newline in the lexer to handle newline characters (\n) in the input script. The t_newline token rule is responsible for incrementing the line number in the lexer whenever newline characters are encountered.
* Error handling rule

I defined an error handling rule t_error in the lexer to handle illegal characters encountered during tokenization. When the t_error rule is triggered, this line prints a message indicating the illegal character encountered. After printing the error message, this line instructs the lexer to skip one character (t.lexer.skip(1)) and continue tokenizing the input script. This is done to recover from the error and prevent the lexer from getting stuck on the illegal character.
* Build the lexer 

The lexer = lex.lex() line initializes and creates an instance of the lexer, enabling to use it to tokenize input strings based on the specified token rules and regular expressions. This instance will be used to tokenize input strings according to the token rules and regular expressions defined earlier in the code.
* Test the lexer

Here the lexer will tokenize the input data and generate tokens. The loop will then iterate over these tokens, printing each token's information (type, value, line number, position) to the console. This process allows to see how the lexer tokenizes the input data based on the defined token rules and regular expressions.

* Code snippets from your files.

```
# Example of one token definition
tokens = (
    'LOAD',
    )
```
```
# Example of a declaration of one regular expression
t_STRING = r'"[^"]*"'
```
```
# Define a rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
```
```
# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)
```
```
# Build the lexer
lexer = lex.lex()
```
```
# Test the lexer
lexer.input(data)
```
## Conclusions / Screenshots / Results

Working on this lab I understood better what a lexical analysis is, I got familiar with the inner workings of a lexer/scanner/tokenizer. For this, I implemented a lexer for Image processing domain specific language using Python and the ply library. The lexer was designed to tokenize a DSL script containing various operations such as loading images, applying filters, converting formats, cropping, and saving images. The lexer successfully identified and tokenized the DSL commands in the sample script, producing output that showed each token type, value, line number, and position in the input script. Regular expressions were used to define the patterns for matching tokens, ensuring accurate tokenization of different elements in the DSL script.

**Results:**
![Results](E:\GIT-LFA\LFA\lab1\lab3.png)

## References
https://en.wikipedia.org/wiki/Lexical_analysis