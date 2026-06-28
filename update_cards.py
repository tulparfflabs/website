import re

with open('team.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_card_1 = '''<div class="culture-card">
            <h3 data-tr="Şeffaf Dokümantasyon" data-en="Transparent Documentation">Şeffaf Dokümantasyon</h3>
            <p data-tr="Notion üzerinden yürüttüğümüz raporlama sistemi sayesinde tüm ekip üyeleri projenin her aşamasına hakimdir. Bilgiye erişim engelsiz ve şeffaftır." data-en="Thanks to our reporting system on Notion, all team members are up to date on every stage of the project. Access to information is transparent and barrier-free.">Notion üzerinden yürüttüğümüz raporlama sistemi sayesinde tüm ekip üyeleri projenin her aşamasına hakimdir. Bilgiye erişim engelsiz ve şeffaftır.</p>
            <div class="hidden-content" style="display: none; margin-top: 1rem; padding-top: 1rem; border-top: 1px dashed var(--border); font-size: 0.95rem; color: var(--text-muted);" data-tr="Şeffaf Dokümantasyon Sistemi: Takım içi süreçlerimizi Notion üzerinden yönetiyoruz. Her üye, yürüttüğü çalışmaların kapsamını, karşılaştığı teknik zorlukları ve çözüm aşamalarını sade ve anlaşılır raporlar halinde paylaşıyor. Bu sayede takıma yeni katılan üyelerimiz, geçmişte yapılmış olan tüm çalışmaları inceleyerek adaptasyon süreçlerini hızlandırıyor ve projenin teknik geçmişine hızla hakim oluyorlar." data-en="Transparent Documentation System: We manage our internal team processes on Notion. Each member shares the scope of their work, technical challenges they face, and solution stages in simple and understandable reports. This allows our new team members to accelerate their adaptation processes by reviewing all past work and quickly mastering the project's technical background.">Şeffaf Dokümantasyon Sistemi: Takım içi süreçlerimizi Notion üzerinden yönetiyoruz. Her üye, yürüttüğü çalışmaların kapsamını, karşılaştığı teknik zorlukları ve çözüm aşamalarını sade ve anlaşılır raporlar halinde paylaşıyor. Bu sayede takıma yeni katılan üyelerimiz, geçmişte yapılmış olan tüm çalışmaları inceleyerek adaptasyon süreçlerini hızlandırıyor ve projenin teknik geçmişine hızla hakim oluyorlar.</div>
            <button class="blog-link" onclick="const hc = this.previousElementSibling; const isHidden = hc.style.display === 'none'; hc.style.display = isHidden ? 'block' : 'none'; this.innerHTML = isHidden ? 'Daha az göster' : 'Daha fazla';" style="background:none; border:none; padding:0; font-family:inherit; cursor:pointer; color: var(--accent2); font-weight: 600; margin-top: 1rem; display: inline-flex; align-items: center; gap: 4px;">Daha fazla</button>
          </div>'''

new_card_2 = '''<div class="culture-card">
            <h3 data-tr="7/24 İletişim" data-en="24/7 Communication">7/24 İletişim</h3>
            <p data-tr="Takım içi engelsiz iletişim ağımızla her an destek ve fikir alışverişi sağlıyoruz. Hızlı karar alma ve proaktif çözüm üretme kültürüne sahibiz." data-en="We provide support and idea exchange at any time with our seamless internal communication network. We have a culture of rapid decision-making and proactive problem-solving.">Takım içi engelsiz iletişim ağımızla her an destek ve fikir alışverişi sağlıyoruz. Hızlı karar alma ve proaktif çözüm üretme kültürüne sahibiz.</p>
            <div class="hidden-content" style="display: none; margin-top: 1rem; padding-top: 1rem; border-top: 1px dashed var(--border); font-size: 0.95rem; color: var(--text-muted);" data-tr="Erişilebilir İletişim Ağı: Mühendislik, dinamik bir süreçtir; bu nedenle takım içinde hiyerarşik engelleri kaldırdık. 7/24 açık iletişim kanallarımız sayesinde, üyelerimiz teknik bir sorun yaşadıklarında ihtiyaç duydukları desteğe anında ulaşabiliyor. Bu sayede sadece bilgi aktarımı yapmakla kalmıyor, sahada ve atölyede birbirini destekleyen güçlü bir dayanışma kültürü inşa ediyoruz." data-en="Accessible Communication Network: Engineering is a dynamic process; therefore, we have removed hierarchical barriers within the team. Thanks to our 24/7 open communication channels, our members can instantly reach the support they need when facing a technical issue. In this way, we not only transfer knowledge but also build a strong culture of solidarity that supports each other in the field and workshop.">Erişilebilir İletişim Ağı: Mühendislik, dinamik bir süreçtir; bu nedenle takım içinde hiyerarşik engelleri kaldırdık. 7/24 açık iletişim kanallarımız sayesinde, üyelerimiz teknik bir sorun yaşadıklarında ihtiyaç duydukları desteğe anında ulaşabiliyor. Bu sayede sadece bilgi aktarımı yapmakla kalmıyor, sahada ve atölyede birbirini destekleyen güçlü bir dayanışma kültürü inşa ediyoruz.</div>
            <button class="blog-link" onclick="const hc = this.previousElementSibling; const isHidden = hc.style.display === 'none'; hc.style.display = isHidden ? 'block' : 'none'; this.innerHTML = isHidden ? 'Daha az göster' : 'Daha fazla';" style="background:none; border:none; padding:0; font-family:inherit; cursor:pointer; color: var(--accent2); font-weight: 600; margin-top: 1rem; display: inline-flex; align-items: center; gap: 4px;">Daha fazla</button>
          </div>'''

# Regex replace the original cards
pattern1 = re.compile(r'<div class="culture-card">\s*<h3 data-tr="Şeffaf Dokümantasyon".*?</div>', re.DOTALL)
pattern2 = re.compile(r'<div class="culture-card">\s*<h3 data-tr="7/24 İletişim".*?</div>', re.DOTALL)

content = pattern1.sub(new_card_1, content)
content = pattern2.sub(new_card_2, content)

with open('team.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully")
