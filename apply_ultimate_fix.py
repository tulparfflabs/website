import glob
import re

files = glob.glob('*.html')

for f in files:
    if "google" in f: continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    # 1. Remove old hamburger HTML
    content = re.sub(r'<button class="hamburger".*?</button>', '', content, flags=re.DOTALL)
    
    # 2. Add new hamburger HTML right before <ul class="nav-links">
    new_hamburger_html = """
    <div class="hamburger-menu" id="hamburger">
        <span></span>
        <span></span>
        <span></span>
    </div>
    <ul class="nav-links" role="list">"""
    content = content.replace('<ul class="nav-links" role="list">', new_hamburger_html)
    
    # 3. Remove ALL redundant media queries and nav-links/hamburger CSS to clean the slate
    # This is tricky with regex, so we'll just append the !important overrides at the very end of <style>
    # The !important tags will override any existing junk.
    
    ultimate_css = """
    /* --- 1. MASAÜSTÜ İÇİN (Hamburger ikonunu gizle) --- */
    .hamburger-menu {
        display: none;
        cursor: pointer;
        flex-direction: column;
        gap: 5px;
    }

    /* Üç çizginin görünümü */
    .hamburger-menu span {
        width: 30px;
        height: 3px;
        background-color: #fff; /* Sitenin üst kısmı koyuysa #fff, açıksa #000 */
        border-radius: 5px;
        transition: all 0.3s;
    }
    
    nav {
       height: auto !important;
       overflow: visible !important;
    }

    /* --- 2. MOBİL İÇİN SİHİRLİ DOKUNUŞ --- */
    @media screen and (max-width: 1200px) {
        .hamburger-menu {
            display: flex !important;
            position: absolute !important;
            right: 20px !important;
            top: 15px !important;
            z-index: 1001 !important;
        }

        .nav-links { 
            display: none !important; /* Mobilde normal yan yana menüyü tamamen gizle */
            flex-direction: column !important;
            background-color: #111 !important;
            position: absolute !important;
            top: 60px !important;
            right: 15px !important;
            width: 200px !important;
            padding: 20px !important;
            border-radius: 8px !important;
            z-index: 1000 !important;
            box-shadow: 0px 8px 16px rgba(0,0,0,0.5) !important;
            gap: 0 !important;
        }

        .nav-links.aktif {
            display: flex !important; /* Butona basılınca menüyü görünür yap */
        }
        
        .nav-links li {
            width: 100% !important;
            margin: 0 !important;
        }
        
        .nav-links a { 
            padding: 12px 0 !important;
            color: white !important; 
            text-align: left !important;
            border-bottom: 1px solid #333 !important;
            display: block !important;
            width: 100% !important;
            background: transparent !important;
        }
        
        .nav-links .nav-cta {
            background-color: #DB1A1A !important;
            color: #fff !important;
            border: none !important;
            border-radius: 4px !important;
            text-align: center !important;
            margin-top: 10px !important;
        }
        
        /* Hide redundant elements */
        .search-wrap, .top-right-lang {
            display: none !important;
        }
    }
    """
    
    # Inject CSS
    if "/* --- 1. MASAÜSTÜ İÇİN" not in content:
        content = content.replace('</style>', ultimate_css + '\n  </style>')
    else:
        # replace existing ultimate css
        content = re.sub(r'/\* --- 1\. MASAÜSTÜ İÇİN.*?\}\s*\}\s*', ultimate_css, content, flags=re.DOTALL)

    # 4. Remove old toggleMenu JS
    content = re.sub(r'function toggleMenu\(\)\s*\{.*?\}', '', content, flags=re.DOTALL)
    
    # 5. Inject new JS
    ultimate_js = """
<script>
    const hamburgerMenuBtn = document.getElementById('hamburger');
    const menuKapsayici = document.querySelector('.nav-links'); 

    if(hamburgerMenuBtn && menuKapsayici) {
        hamburgerMenuBtn.addEventListener('click', () => {
            menuKapsayici.classList.toggle('aktif');
        });
    }
</script>
</body>"""
    
    # Clean up any existing ultimate JS
    content = re.sub(r'<script>\s*const hamburgerMenuBtn = document.getElementById.*?</body>', '</body>', content, flags=re.DOTALL)
    
    content = content.replace('</body>', ultimate_js)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print(f"Applied Ultimate Fix to {f}")
