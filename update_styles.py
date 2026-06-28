import re
import sys

def get_file_content(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file_content(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

index_content = get_file_content('index.html')

style_match = re.search(r'<style>(.*?)</style>', index_content, re.DOTALL)
index_style = style_match.group(1) if style_match else ''

base_style_match = re.search(r'^(.*?)(?=#home\s*\{)', index_style, re.DOTALL | re.MULTILINE)
base_style = base_style_match.group(1) if base_style_match else index_style

media_queries_match = re.search(r'(@media\s*\(max-width.*?)', index_style, re.DOTALL | re.MULTILINE)
media_queries = media_queries_match.group(1) if media_queries_match else ''

modals_match = re.search(r'(\.modal-overlay\s*\{.*?\n  })', index_style, re.DOTALL)
modals = modals_match.group(1) if modals_match else ''

svg_match = re.search(r'<a href="[^"]*home"[^>]*>\s*(<svg.*?</svg>)\s*TULPAR<span>-FF</span>\s*</a>', index_content, re.DOTALL)
nav_svg = svg_match.group(1) if svg_match else ''

def color_adapt(css):
    css = css.replace('var(--primary)', 'var(--surface)')
    css = css.replace('var(--surface2)', 'var(--surface2)')
    css = css.replace('var(--surface3)', 'var(--surface3)')
    
    css = css.replace('rgba(232,255,71,0.18)', 'rgba(174, 226, 255, 0.4)')
    css = css.replace('rgba(232,255,71,0.08)', 'rgba(174, 226, 255, 0.3)')
    css = css.replace('rgba(232,255,71,0.4)', 'rgba(219, 26, 26, 0.8)')
    css = css.replace('rgba(232,255,71,0.06)', 'rgba(174, 226, 255, 0.3)')
    css = css.replace('rgba(232,255,71,0.2)', 'rgba(174, 226, 255, 0.8)')
    css = css.replace('rgba(232,255,71,0.25)', 'rgba(219, 26, 26, 0.4)')
    css = css.replace('rgba(232,255,71,0.12)', 'rgba(219, 26, 26, 0.15)')
    css = css.replace('rgba(232,255,71,0.35)', 'rgba(219, 26, 26, 0.3)')
    css = css.replace('rgba(232,255,71,0.3)', 'rgba(219, 26, 26, 0.4)')
    css = css.replace('rgba(232,255,71,0.04)', 'rgba(219, 26, 26, 0.05)')
    css = css.replace('rgba(232,255,71,0.15)', 'rgba(219, 26, 26, 0.4)')
    
    css = css.replace('var(--accent)', 'var(--accent2)')
    return css

specifics = {
    'contact.html': ['#contact', '.contact-grid', '.contact-info', '.contact-row', '.contact-icon', '.contact-detail', '.contact-form', '.form-group'],
    'team.html': ['#team-page', '.team-grid', '.team-card', '.team-captain-row', '.team-avatar', '.captain-tag', '.team-more', '.team-group', '.team-social', '.about-features', '.feature-card', '.feature-icon', '.feature-text'],
    'vehicle.html': ['#vehicle', '.vehicle-header', '.media-grid', '.media-card', '.media-thumb', '.media-badge', '.media-info', '.specs-grid', '.spec-item', '.spec-value', '.spec-label']
}

for file in specifics.keys():
    content = get_file_content(file)
    target_style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    if not target_style_match: continue
    target_style = target_style_match.group(1)
    
    specific_css_lines = []
    
    for line in target_style.split('\n'):
        if any(line.strip().startswith(sel) for sel in specifics[file]):
            specific_css_lines.append(line)
        elif ' { ' in line and any(sel in line for sel in specifics[file]):
            specific_css_lines.append(line)
            
    specific_css = "\n".join(specific_css_lines)
    specific_css = color_adapt(specific_css)
    
    if nav_svg:
        content = re.sub(r'<a href="[^"]*" class="nav-logo">\s*<svg.*?</svg>\s*TULPAR<span>-FF</span>\s*</a>', 
                         f'<a href="index.html#home" class="nav-logo">\n    {nav_svg}\n    TULPAR<span>-FF</span>\n  </a>', 
                         content, flags=re.DOTALL)
    
    new_style = base_style + "\n" + specific_css + "\n\n  a:focus-visible, button:focus-visible, input:focus-visible, textarea:focus-visible, select:focus-visible { outline: 2px solid var(--accent2); outline-offset: 3px; }\n\n" + media_queries
    
    content = content[:target_style_match.start(1)] + "\n" + new_style + "\n" + content[target_style_match.end(1):]
    
    content = content.replace('style="color: var(--primary) !important;"', '')
    content = content.replace('style="color: var(--text);"', '')
    content = content.replace('background: #050508;', 'background: var(--primary);')
    content = content.replace('background: rgba(10, 10, 15, 0.85);', 'background: rgba(255, 255, 255, 0.9);')
    content = content.replace('background: rgba(10,10,15,0.8);', 'background: rgba(255,255,255,0.8);')
    
    write_file_content(file, content)

print("Styles updated.")
