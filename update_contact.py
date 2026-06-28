import re

with open('contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_block = '''<div class="contact-row">
              <div class="contact-icon">◎</div>
              <div class="contact-detail">
                <strong data-tr="Yarışma" data-en="Competition">Yarışma</strong>
                SUAS 2026 — Patuxent River, MD
              </div>
            </div>'''

new_block = '''<div class="contact-row">
              <div class="contact-icon"><svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20" style="margin-top: 4px;"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" /></svg></div>
              <div class="contact-detail">
                <strong data-tr="LinkedIn" data-en="LinkedIn">LinkedIn</strong>
                <a href="https://www.linkedin.com/company/tulpar-ff/posts/?feedView=all" target="_blank" style="color: inherit; text-decoration: none;">TULPAR-FF</a>
              </div>
            </div>'''

if old_block in content:
    content = content.replace(old_block, new_block)
    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated successfully')
else:
    print('Block not found')
