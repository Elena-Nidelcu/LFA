class Token:
    def __init__(self, type, value=None, lineno=None):
        self.type = type
        self.value = value
        self.lineno = lineno

    def __str__(self):
        return f"Token(type={self.type}, value={self.value}, lineno={self.lineno})"

from ply import lex

# Define tokens
tokens = (
    'LOAD',
    'SAVE',
    'FILTER',
    'IDENTIFIER',
    'STRING',
    'NUMBER',
    'CROP',
    'CONVERT',
    'FORMAT',
    'ROTATE',
    'FLIPX',
    'FLIPY',
    'BW',
    'RESIZE',
    'CONTRAST',
    'BRIGHTNESS',
    'NEGATIVE'
)

# Define regular expressions for tokens
t_LOAD = r'load'
t_SAVE = r'save'
t_FILTER = r'filter'
t_CROP = r'crop'
t_CONVERT = r'convert'
t_FORMAT = r'format'
t_ROTATE = r'rotate'
t_FLIPX = r'flipx'
t_FLIPY = r'flipy'
t_BW = r'bw'
t_RESIZE = r'resize'
t_CONTRAST = r'contrast'
t_BRIGHTNESS = r'brightness'
t_STRING = r'"[^"]*"'
t_NUMBER = r'\d+'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'

# Define a rule to ignore whitespace and tabs
t_ignore = ' \t'

# Define a rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test the lexer
data = """
load "image.jpg"
crop 100 100 200 200
convert format PNG
save "processed_image.jpg"
"""
lexer.input(data)

class ASTNode:
    def __init__(self, token_type, children=None, value=None, lineno=None):
        self.token_type = token_type
        self.value = value
        self.lineno = lineno
        self.children = children if children is not None else []

    def __str__(self):
        return f"ASTNode({self.token_type}, value={self.value}, line={self.lineno})"

def build_ast(token_stream):
    root = ASTNode("Program")
    current_node = root

    for token in token_stream:
        if token.type in {'LOAD', 'SAVE', 'FILTER', 'CROP', 'CONVERT', 'FORMAT', 'ROTATE',
                          'FLIPX', 'FLIPY', 'BW', 'RESIZE', 'CONTRAST', 'BRIGHTNESS', 'NEGATIVE'}:
            current_node.children.append(ASTNode(token.type, value=token.value, lineno=token.lineno))
            current_node = current_node.children[-1]
        elif token.type in {'IDENTIFIER', 'STRING', 'NUMBER'}:
            current_node.children.append(ASTNode(token.type, value=token.value, lineno=token.lineno))
        elif token.type == 'NEWLINE':
            current_node = root
        else:
            raise ValueError(f"Invalid token type: {token.type}")

    return root

def print_ast(node, depth=0):
    if node is None:
        return

    indent = '  ' * depth
    print(f"{indent}({node.token_type}, value={node.value}, line={node.lineno})")

    for child in node.children:
        print_ast(child, depth + 1)

# Example usage:
token_stream = [
    Token('LOAD', 'load', 1),
    Token('STRING', 'image.jpg', 1),
    Token('NEWLINE', '\n', 1),
    Token('CROP', 'crop', 2),
    Token('NUMBER', 100, 2),
    Token('NUMBER', 100, 2),
    Token('NUMBER', 200, 2),
    Token('NUMBER', 200, 2),
    Token('NEWLINE', '\n', 2),
    Token('CONVERT', 'convert', 3),
    Token('FORMAT', 'format', 3),
    Token('STRING', 'PNG', 3),
    Token('NEWLINE', '\n', 3),
    Token('SAVE', 'save', 4),
    Token('STRING', 'processed_image.jpg', 4),
    Token('NEWLINE', '\n', 4)
]

ast_root = build_ast(token_stream)
print("Abstract Syntax Tree (AST):")
print_ast(ast_root)

