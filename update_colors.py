import re

with open('team.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace TULPAR-FF ile Tanışın / Meet TULPAR-FF
content = content.replace(
    'data-tr="TULPAR-FF ile Tanışın" data-en="Meet TULPAR-FF">TULPAR-FF ile Tanışın',
    'data-tr="TULPAR<span style=\'color: var(--accent2);\'>-FF</span> ile Tanışın" data-en="Meet TULPAR<span style=\'color: var(--accent2);\'>-FF</span>">TULPAR<span style="color: var(--accent2);">-FF</span> ile Tanışın'
)

# 2. Replace Team Culture & Knowledge Management
content = content.replace(
    'data-tr="Takım Kültürü ve Bilgi Yönetimi" data-en="Team Culture & Knowledge Management">Takım Kültürü ve Bilgi Yönetimi',
    'data-tr="Takım Kültürü <span style=\'color: var(--accent2);\'>ve</span> Bilgi Yönetimi" data-en="Team Culture <span style=\'color: var(--accent2);\'>&amp;</span> Knowledge Management">Takım Kültürü <span style="color: var(--accent2);">ve</span> Bilgi Yönetimi'
)

# Also fix the fallback where someone might have used &amp; instead of &
content = content.replace(
    'data-tr="Takım Kültürü ve Bilgi Yönetimi" data-en="Team Culture &amp; Knowledge Management">Takım Kültürü ve Bilgi Yönetimi',
    'data-tr="Takım Kültürü <span style=\'color: var(--accent2);\'>ve</span> Bilgi Yönetimi" data-en="Team Culture <span style=\'color: var(--accent2);\'>&amp;</span> Knowledge Management">Takım Kültürü <span style="color: var(--accent2);">ve</span> Bilgi Yönetimi'
)


with open('team.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated text colors')
