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
for token in lexer:
    print(token)
