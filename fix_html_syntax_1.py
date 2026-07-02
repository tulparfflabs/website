import glob
import re

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Fix nav-logo
    content = content.replace('aria-label="TULPAR-FF Ana Sayfa\n', 'aria-label="TULPAR-FF Ana Sayfa">\n')
    content = content.replace('aria-label="TULPAR-FF Ana Sayfa\r\n', 'aria-label="TULPAR-FF Ana Sayfa">\n')
    content = content.replace('aria-label="TULPAR-FF Ana Sayfa<svg', 'aria-label="TULPAR-FF Ana Sayfa">\n  <svg')
    
    # Fix SVG tags
    content = content.replace('fill="none"\n', 'fill="none">\n')
    content = content.replace('fill="none"\r\n', 'fill="none">\n')
    content = content.replace('fill="none"<path', 'fill="none">\n  <path')
    
    # Fix nav-cta
    content = content.replace('data-tr="İletişim\n', 'data-tr="İletişim">İletişim</a>\n')
    content = content.replace('data-tr="İletişim\r\n', 'data-tr="İletişim">İletişim</a>\n')
    content = content.replace('data-tr="İletişim</ul', 'data-tr="İletişim">İletişim</a>\n</ul')
    
    content = content.replace('data-en="Contact\n', 'data-en="Contact">Contact</a>\n')
    content = content.replace('data-en="Contact\r\n', 'data-en="Contact">Contact</a>\n')
    content = content.replace('data-en="Contact</ul', 'data-en="Contact">Contact</a>\n</ul')
    
    # Fix lang-switcher
    content = content.replace('aria-label="Dil seçimi\n', 'aria-label="Dil seçimi">\n')
    content = content.replace('aria-label="Dil seçimi\r\n', 'aria-label="Dil seçimi">\n')
    content = content.replace('aria-label="Dil seçimi<button', 'aria-label="Dil seçimi">\n  <button')
    
    content = content.replace('onclick="setLang(\'tr\')\n', 'onclick="setLang(\'tr\')">TR</button>\n')
    content = content.replace('onclick="setLang(\'tr\')\r\n', 'onclick="setLang(\'tr\')">TR</button>\n')
    content = content.replace('onclick="setLang(\'tr\')<button', 'onclick="setLang(\'tr\')">TR</button>\n  <button')
    
    content = content.replace('onclick="setLang(\'en\')\n', 'onclick="setLang(\'en\')">EN</button>\n')
    content = content.replace('onclick="setLang(\'en\')\r\n', 'onclick="setLang(\'en\')">EN</button>\n')
    content = content.replace('onclick="setLang(\'en\')</div', 'onclick="setLang(\'en\')">EN</button>\n</div')

    # Fix search input
    content = content.replace('classList.remove(\'active\'),200)\n', 'classList.remove(\'active\'),200)">\n')
    content = content.replace('classList.remove(\'active\'),200)\r\n', 'classList.remove(\'active\'),200)">\n')
    
    # Write back
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print(f'Fixed syntax in {f}')
