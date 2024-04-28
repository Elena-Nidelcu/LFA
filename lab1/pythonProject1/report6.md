# LFA lab 6  

### Course: Formal Languages & Finite Automata
### Author: Nidelcu Elena

----


## Objectives:
* Get familiar with parsing, what it is and how it can be programmed.
* Get familiar with the concept of AST.
* In addition to what has been done in the 3rd lab work do the following:
    1. In case you didn't have a type that denotes the possible types of tokens you need to:
        * Have a type TokenType (like an enum) that can be used in the lexical analysis to categorize the tokens.
        * Please use regular expressions to identify the type of the token.
    2. Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
    3. Implement a simple parser program that could extract the syntactic information from the input text.

## Implementation description

* About 2-3 sentences to explain each piece of the implementation.
  1.  task a:
  I already implemented a tuple of tokens in the 3rd lab and I also used there regular expressions.
  2. task b:
  To construct an AST I used a class with token_type (the type of token (e.g., LOAD, SAVE, STRING, NUMBER, etc.)), value (the value associated with the token), lineno (the line number where the token appears) and children (the children nodes of the current node) arguments. The build_ast function traverses the token_stream and constructs the AST based on the token types. It uses instances of the ASTNode class to represent nodes in the tree structure. The print_ast function recursively traverses the AST and prints the nodes along with their values and line numbers, following a depth-first traversal approach. The data structures used are a custom ASTNode class, an assumed Token class, and a list (token_stream) to hold the tokenized input data.
  3. task c:
  Here, I used yacc library for parser. It helped me to specify the grammar of a language using production rules, to process the grammar rules and tokenizes input data according to the specified grammar, to generate a parser based on the grammar rules provided, to provide built-in mechanisms for error handling, such as syntax error detection and reporting and to create a complete parser-lexer system. I defined the grammar rules, where non-terminals are: program, command_list, command, and all my functions with '_command' adding, terminals are: name of commands, STRING and NUMBER, start symbol is 'program'. Also, I implemented a simple functionality to handle my input and to process the photo.

* Code snippets from your files.

```
# task b
class ASTNode:
    def __init__(self, token_type, children=None, value=None, lineno=None):
        self.token_type = token_type
        self.value = value
        self.lineno = lineno
        self.children = children if children is not None else []
```
```
# task c
def p_program(p):
    '''program : command_list'''
    p[0] = p[1]

def p_command_list(p):
    '''command_list : command
                    | command_list command'''
def p_command(p):
    '''command : load_command
               | save_command
               | crop_command
               | rotate_command
               | flipx_command
               | flipy_command
               | bw_command
               | resize_command
               | contrast_command
               | brightness_command'''
```

* If needed, screenshots.


## Conclusions / Screenshots / Results

Working on this lab I got familiar with parsing and the concept of AST. I implemented a basic AST data structure using a custom ASTNode class. This structure allowed me to represent the hierarchical relationships between different language constructs in a readable and organized manner. Next, I explored the use of YACC (Yet Another Compiler Compiler) library, specifically the yacc module in Ply (Python Lex-Yacc), to build a parser for a simple language. Throughout the lab, I emphasized the importance of grammars in parsing, error handling, and the integration of parsers with lexer generators for efficient tokenization. Doing this lab provided me a valuable insights into the concepts of ASTs, parsers, grammars, and their practical implementation using Python and YACC.

**Results:**
task b
```
Abstract Syntax Tree (AST):
(Program, value=None, line=None)
  (LOAD, value=load, line=1)
    (STRING, value=image.jpg, line=1)
  (CROP, value=crop, line=2)
    (NUMBER, value=100, line=2)
    (NUMBER, value=100, line=2)
    (NUMBER, value=200, line=2)
    (NUMBER, value=200, line=2)
  (CONVERT, value=convert, line=3)
    (FORMAT, value=format, line=3)
      (STRING, value=PNG, line=3)
  (SAVE, value=save, line=4)
    (STRING, value=processed_image.jpg, line=4)
```
task c
```
Load command: "image.jpg"
Crop command: 10 500 200 800
Rotate command: 90
Save command: "processed_image.jpg"
Parsed data:
[(('load', '"image.jpg"'),), (('crop', 10, 500, 200, 800),), (('rotate', 90),), (('save', '"processed_image.jpg"'),)]
```
## References
https://en.wikipedia.org/wiki/PLY_(software)
https://en.wikipedia.org/wiki/Yacc