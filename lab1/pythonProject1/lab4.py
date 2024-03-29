import random

def generate_string_from_regex_1():
    generated_string = ''.join(random.choice(['S', 'T']) + random.choice(['U', 'V']) + 'W' * random.randint(0, 5) + 'Y' * random.randint(1, 5) + '24')
    return generated_string

def generate_string_from_regex_2():
    generated_string = ''.join('L' + random.choice(['M', 'N']) + 'OOO' + 'P' * random.randint(0, 5) + 'Q' + random.choice(['2', '3']))
    return generated_string

def generate_string_from_regex_3():
    generated_string = ''.join('R' * random.randint(0, 5) + 'S' + random.choice(['T', 'U', 'V']) + 'W' + random.choice(['X', 'Y', 'Z']) * 2)
    return generated_string

def show_processing_sequence(regex_pattern):
    sequence = []
    current_group = ''

    brackets = False
    for char in regex_pattern:
        if char == '[':
            brackets = True
            current_group = ''
        elif char == ']':
            brackets = False
            sequence.append(f"Match one element from '{current_group}' list")
            current_group = ''
        elif char == '*':
            sequence.append("Match zero or more occurrences of the preceding element")
        elif char == '+':
            sequence.append("Match one or more occurrences of the preceding element")
        elif char == '{':
            sequence.append("Specify a range of occurrences")
        elif char == '}':
            sequence.append("End of range specification")
        elif char == '(':
            sequence.append("Start of a group")
        elif char == ')':
            sequence.append("End of a group")
        elif char.isalnum() and not(brackets):
            sequence.append(f"Match '{char}'")
        else:
            current_group += char

    return sequence

regex_1 = r'[ST][UV]W*Y+24'
generated_str = generate_string_from_regex_1()
print("Generated string matching the regex:", generated_str)

sequence = show_processing_sequence(regex_1)
for step, explanation in enumerate(sequence, start=1):
    print(f"Step {step}: {explanation}")
print()

regex_2 = r'L[MN]OOOP*Q[23]'
generated_str = generate_string_from_regex_2()
print("Generated string matching the regex:", generated_str)

sequence = show_processing_sequence(regex_2)
for step, explanation in enumerate(sequence, start=1):
    print(f"Step {step}: {explanation}")
print()

regex_3 = r'R*S[TUV]W[XYZ]{2}'
generated_str = generate_string_from_regex_3()
print("Generated string matching the regex:", generated_str)

sequence = show_processing_sequence(regex_3)
for step, explanation in enumerate(sequence, start=1):
    print(f"Step {step}: {explanation}")
print()