import sys

def check_css_brackets(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_idx = content.find('<style>')
    end_idx = content.find('</style>')
    
    if start_idx == -1 or end_idx == -1:
        print('Style tags not found')
        return
        
    css = content[start_idx+7:end_idx]
    
    # Remove comments
    import re
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    
    open_brackets = 0
    line_num = content[:start_idx].count('\n') + 1
    
    for i, char in enumerate(css):
        if char == '\n':
            line_num += 1
        if char == '{':
            open_brackets += 1
        elif char == '}':
            open_brackets -= 1
            if open_brackets < 0:
                print(f'Too many closing brackets at line {line_num}')
                return
    
    if open_brackets > 0:
        print(f'Unclosed brackets: {open_brackets}')
    else:
        print('Brackets are balanced perfectly.')

check_css_brackets('index.html')
