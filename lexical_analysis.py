import re
import io

token_specs = [
    ('NUMBER', r'\d+'),
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),
    ('OPERATOR', r'[+\-*/]'),
    ('PARENTHESIS', r'[()]'),
    ('ASSIGNMENT', r'='),
    ('WHITESPACE', r'\s+')
]

def lexer(source_code):
    tokens = []
    source_code = source_code.strip()  
    
    while source_code:
        matched = False
        
        for token_type, pattern in token_specs:
            regex = re.compile('^' + pattern)
            match = regex.match(source_code)
            
            if match:
                value = match.group(0)
                tokens.append((token_type, value))
                source_code = source_code[len(value):].lstrip()
                matched = True
                break
        
        if not matched:
            raise SyntaxError(f"Invalid token: {source_code}")
    
    return tokens

source_code = '''
hello = world + I * 2
print(hello WORLD)
'''

tokens = lexer(source_code)

for token_type, value in tokens:
    print(f'Token: {token_type:<8} | Value: {value:>2}')