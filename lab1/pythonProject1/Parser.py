from ply import lex, yacc
import PIL
from PIL import Image

# Define tokens
tokens = (
    'LOAD',
    'SAVE',
    'NUMBER',
    'CROP',
    'ROTATE',
    'FLIPX',
    'FLIPY',
    'BW',
    'RESIZE',
    'CONTRAST',
    'BRIGHTNESS',
    'STRING',
)

# Define token regular expressions
t_LOAD = r'load'
t_SAVE = r'save'
t_STRING = r'"[^"]*"'
t_CROP = r'crop'
t_ROTATE = r'rotate'
t_NUMBER = r'\d+'
t_FLIPX = r'flipx'
t_FLIPY = r'flipy'
t_BW = r'bw'
t_RESIZE = r'resize'
t_CONTRAST = r'contrast'
t_BRIGHTNESS = r'brightness'

# Ignored characters
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Grammar rules
def p_program(p):
    '''program : command_list'''
    p[0] = p[1]

def p_command_list(p):
    '''command_list : command
                    | command_list command'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]

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
    p[0] = (p[1], *p[2:])

img = Image.open("basterds.jpg")

# Define individual command rules
def p_load_command(p):
    'load_command : LOAD STRING'
    print("Load command:", p[2])
    p[0] = ('load', p[2])
    img.show()

def p_save_command(p):
    'save_command : SAVE STRING'
    print("Save command:", p[2])
    p[0] = ('save', p[2])
    img.save("rotated.jpg")

def p_crop_command(p):
    'crop_command : CROP NUMBER NUMBER NUMBER NUMBER'
    print("Crop command:", p[2], p[3], p[4], p[5])
    p[0] = ('crop', int(p[2]), int(p[3]), int(p[4]), int(p[5]))
    img = Image.open("basterds.jpg")
    img = img.crop((int(p[2]), int(p[3]), int(p[4]), int(p[5])))
    img.show()

def p_rotate_command(p):
    'rotate_command : ROTATE NUMBER'
    print("Rotate command:", p[2])
    p[0] = ('rotate', int(p[2]))
    img = Image.open("basterds.jpg")
    img = img.crop((10, 500, 200, 800))
    img_rotated = img.rotate(90, PIL.Image.NEAREST, expand=1)
    img_rotated.show()
    img_rotated.save("rotated.jpg")

def p_command_flipx(p):
    'flipx_command : FLIPX'
    print("FlipX command")
    p[0] = ('flipx',)

def p_command_flipy(p):
    'flipy_command : FLIPY'
    print("FlipY command")
    p[0] = ('flipy',)

def p_bw_command(p):
    'bw_command : BW'
    print("Black & White command")
    p[0] = ('bw',)

def p_resize_command(p):
    'resize_command : RESIZE NUMBER NUMBER'
    print("Resize command:", p[2], p[3])
    p[0] = ('resize', int(p[2]), int(p[3]))
    p[0] = ('contrast', int(p[2]))

def p_contrast_command(p):
    'contrast_command : CONTRAST NUMBER'
    print("Contrast command:", p[2])
    p[0] = ('brightness', int(p[2]))

def p_brightness_command(p):
    'brightness_command : BRIGHTNESS NUMBER'
    print("Brightness command:", p[2])

def p_error(p):
    print(f"Syntax error at token {p.value}")

# Build the parser
parser = yacc.yacc()

# Test the parser with input data
input_data = ('load "image.jpg" '
              'crop 10 500 200 800'
              'rotate 90'
              'save "processed_image.jpg"')
parsed_data = parser.parse(input_data)
print("Parsed data:")
print(parsed_data)
