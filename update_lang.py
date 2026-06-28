import re

with open('team.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_onclick = "const hc = this.previousElementSibling; const isHidden = hc.style.display === 'none'; hc.style.display = isHidden ? 'block' : 'none'; const lang = document.documentElement.lang || 'tr'; this.innerHTML = isHidden ? (lang === 'tr' ? 'Daha az göster' : 'Show less') : (lang === 'tr' ? 'Daha fazla' : 'Read more');"
new_onclick = "const hc = this.previousElementSibling; const isHidden = hc.style.display === 'none'; hc.style.display = isHidden ? 'block' : 'none'; const lang = document.documentElement.lang || 'tr'; this.innerHTML = isHidden ? (lang === 'tr' ? 'Daha az göster' : 'Show less') : (lang === 'tr' ? 'Daha fazla' : 'Read more'); this.setAttribute('data-tr', isHidden ? 'Daha az göster' : 'Daha fazla'); this.setAttribute('data-en', isHidden ? 'Show less' : 'Read more');"

content = content.replace(old_onclick, new_onclick)

with open('team.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated language logic correctly')
