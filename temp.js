
    function toggleReadMore(btn) {
      const hiddenContent = btn.previousElementSibling;
      const isHidden = hiddenContent.style.display === 'none' || hiddenContent.style.display === '';
      const currentLang = document.documentElement.lang || 'tr';

      if (isHidden) {
        hiddenContent.style.display = 'block';
        btn.innerHTML = currentLang === 'tr' ? 'Daha az göster ↑' : 'Show less ↑';
      } else {
        hiddenContent.style.display = 'none';
        btn.innerHTML = currentLang === 'tr' ? 'Devamını oku →' : 'Read more →';
      }
    }

    /* SPLASH  */
    document.addEventListener('DOMContentLoaded', () => {
      const splash = document.getElementById('splash');
      if (splash && !sessionStorage.getItem('splashSeen')) {
        sessionStorage.setItem('splashSeen', 'true');
        setTimeout(() => {
          splash.classList.add('hidden');
        }, 3800);
      }
    });

    /* LANGUAGE */
    let lang = 'tr';

    function setLang(l) {
      lang = l;
      document.getElementById('btn-tr').classList.toggle('active', l === 'tr');
      document.getElementById('btn-en').classList.toggle('active', l === 'en');
      document.getElementById('btn-tr').setAttribute('aria-pressed', l === 'tr');
      document.getElementById('btn-en').setAttribute('aria-pressed', l === 'en');
      document.documentElement.lang = l === 'tr' ? 'tr' : 'en';

      document.querySelectorAll('[data-tr]').forEach(el => {
        const val = el.getAttribute('data-' + l);
        if (!val) return;
        if (val.includes('<') || val.includes('&')) el.innerHTML = val;
        else el.textContent = val;
      });

      const h1el = document.getElementById('hero-h1');
      if (h1el) h1el.innerHTML = h1el.getAttribute('data-' + l);

      document.getElementById('site-search').placeholder = l === 'tr' ? 'Ara…' : 'Search…';

      const phs = {
        'cf-name': { tr: 'Adınız', en: 'Your name' },
        'cf-email': { tr: 'siz@ornek.com', en: 'you@example.com' },
        'cf-message': { tr: 'Mesajınız…', en: 'Your message…' }
      };
      Object.entries(phs).forEach(([id, v]) => {
        const el = document.getElementById(id);
        if (el) el.placeholder = v[l];
      });
    }

    const searchData = [
      { tr: 'Biz Kimiz / Misyon', en: 'Who We Are / Mission', section: '#about', kw: 'misyon mission about drone' },
      { tr: 'Yolculuğumuz', en: 'Our Journey', section: '#journey', kw: 'yolculuk timeline tarih history 2023 2024 2025 2026' },
      { tr: 'Araç Tasarımı', en: 'Vehicle Design', section: 'vehicle.html', kw: 'araç vehicle drone uav specs' },
      { tr: 'İlerleme Güncellemeleri', en: 'Progress Updates', section: '#blog', kw: 'blog günlük build log' },
      { tr: 'Takım', en: 'Team', section: 'team.html', kw: 'takım team beyzanur muhlis nahit aylin' },
      { tr: 'Sponsorlar', en: 'Sponsors', section: '#sponsors', kw: 'sponsor destek' },
      { tr: 'İletişim', en: 'Contact', section: 'contact.html', kw: 'iletişim contact mail email' },
    ];

    function handleSearch(q) {
      const box = document.getElementById('search-results');
      if (!q.trim()) { box.classList.remove('active'); return; }
      const ql = q.toLowerCase();
      const res = searchData.filter(d => d[lang].toLowerCase().includes(ql) || d.kw.includes(ql));
      if (!res.length) {
        box.innerHTML = `<div class="search-item" style="cursor:default">${lang === 'tr' ? 'Sonuç bulunamadı' : 'No results found'}</div>`;
      } else {
        box.innerHTML = res.map(d =>
          `<div class="search-item" role="option" tabindex="0" onclick="goTo('${d.section}')" onkeydown="if(event.key==='Enter')goTo('${d.section}')"><strong>${d[lang]}</strong></div>`
        ).join('');
      }
      box.classList.add('active');
    }
    function goTo(hash) {
      if (hash.includes('.html')) { window.location.href = hash; return; }
      document.querySelector(hash)?.scrollIntoView({ behavior: 'smooth' });
      document.getElementById('search-results').classList.remove('active');
      document.getElementById('site-search').value = '';
    }

    



    const navLinks = document.querySelectorAll('.nav-links a');
    const sectionLinksObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          navLinks.forEach(l => {
            if (l.getAttribute('href') === '#' + entry.target.id) {
              l.style.background = 'transparent';
              l.style.color = 'var(--accent2)';
            } else {
              l.style.background = '';
              l.style.color = '';
            }
          });
        }
      });
    }, { threshold: 0.3 });

    document.querySelectorAll('section[id]').forEach(section => {
      sectionLinksObserver.observe(section);
    });

    const fadeObs = new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); fadeObs.unobserve(e.target); } });
    }, { threshold: 0.1 });
    document.querySelectorAll('.fade-up').forEach(el => fadeObs.observe(el));


    function openBlogModal(element) {
      const modal = document.getElementById('blog-modal');
      const currentLang = document.documentElement.lang || 'tr';

      const tag = element.querySelector('.blog-tag').innerHTML;
      const date = element.querySelector('.blog-date').innerHTML;
      const title = element.querySelector('.blog-card-title').innerHTML;

      const hiddenData = element.querySelector('.hidden-content');
      const fullText = hiddenData.getAttribute('data-' + currentLang);

      document.getElementById('modal-tag').innerHTML = tag;
      document.getElementById('modal-date').innerHTML = date;
      document.getElementById('modal-title').innerHTML = title;
      document.getElementById('modal-body').innerHTML = fullText;

      modal.classList.add('active');
      document.body.style.overflow = 'hidden';
    }

    function closeBlogModal() {
      document.getElementById('blog-modal').classList.remove('active');
      document.body.style.overflow = '';
    }

    document.getElementById('blog-modal').addEventListener('click', function (e) {
      if (e.target === this) closeBlogModal();
    });
  