import re

with open('team.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert HTML before </main>
html_to_insert = '''
    <section id="culture" class="fade-up">
      <div class="container">
        <h2 data-tr="Takým Kültürü ve Bilgi Yönetimi" data-en="Team Culture & Knowledge Management">Takým Kültürü ve Bilgi Yönetimi</h2>
        <div class="culture-grid">
          <div class="culture-card">
            <h3 data-tr="Þeffaf Dokümantasyon" data-en="Transparent Documentation">Þeffaf Dokümantasyon</h3>
            <p data-tr="Notion üzerinden yürüttüðümüz raporlama sistemi sayesinde tüm ekip üyeleri projenin her aþamasýna hakimdir. Bilgiye eriþim engelsiz ve þeffaftýr." data-en="Thanks to our reporting system on Notion, all team members are up to date on every stage of the project. Access to information is transparent and barrier-free.">Notion üzerinden yürüttüðümüz raporlama sistemi sayesinde tüm ekip üyeleri projenin her aþamasýna hakimdir. Bilgiye eriþim engelsiz ve þeffaftýr.</p>
          </div>
          <div class="culture-card">
            <h3 data-tr="7/24 Ýletiþim" data-en="24/7 Communication">7/24 Ýletiþim</h3>
            <p data-tr="Takým içi engelsiz iletiþim aðýmýzla her an destek ve fikir alýþveriþi saðlýyoruz. Hýzlý karar alma ve proaktif çözüm üretme kültürüne sahibiz." data-en="We provide support and idea exchange at any time with our seamless internal communication network. We have a culture of rapid decision-making and proactive problem-solving.">Takým içi engelsiz iletiþim aðýmýzla her an destek ve fikir alýþveriþi saðlýyoruz. Hýzlý karar alma ve proaktif çözüm üretme kültürüne sahibiz.</p>
          </div>
        </div>
      </div>
    </section>
'''

content = content.replace('</main>', html_to_insert + '\n  </main>')

# Insert CSS before </style>
css_to_insert = '''
    #culture { padding: 5rem 0 7rem; }
    .culture-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; margin-top: 3rem; }
    .culture-card { background: var(--surface2); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 2rem; transition: all .3s ease; box-shadow: 0 4px 10px rgba(0,0,0,0.03); }
    .culture-card:hover { border-color: rgba(219, 26, 26, 0.4); transform: translateY(-5px); box-shadow: 0 8px 25px rgba(219, 26, 26, 0.12); }
    .culture-card h3 { font-family: var(--font-head); font-size: 1.2rem; margin-bottom: 1rem; color: var(--text); }
    .culture-card p { font-size: 0.95rem; color: var(--text-muted); line-height: 1.6; }
'''

content = content.replace('</style>', css_to_insert + '\n  </style>')

with open('team.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
