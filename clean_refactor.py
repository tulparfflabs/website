import glob
import re

files = glob.glob('*.html')

unified_css = """
    /* --- UNIFIED MOBILE NAVIGATION --- */
    .hamburger {
      display: none;
      flex-direction: column;
      gap: 6px;
      cursor: pointer;
      z-index: 1001;
      padding: 5px;
    }
    
    .hamburger span {
      width: 30px;
      height: 3px;
      background: var(--text);
      border-radius: 2px;
      transition: all 0.3s ease;
    }

    @media screen and (max-width: 1200px) {
      nav .nav-links,
      nav .search-wrap,
      nav .top-right-lang {
        display: none !important;
      }
      
      nav .nav-right {
        margin-right: 50px !important;
      }

      .hamburger {
        display: flex !important;
        position: absolute;
        right: 20px;
      }

      nav.open .nav-links {
        display: flex !important;
        flex-direction: column !important;
        position: absolute !important;
        top: 100% !important;
        left: 0 !important;
        right: 0 !important;
        background: rgba(255, 255, 255, 0.98) !important;
        padding: 20px 0 !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1) !important;
        gap: 15px !important;
      }

      nav.open .nav-links li {
        width: 100% !important;
        text-align: center !important;
      }

      nav.open .nav-links a {
        display: block !important;
        padding: 10px 0 !important;
        color: var(--text) !important;
      }
      
      nav.open .nav-links .nav-cta {
          margin: 0 auto !important;
          width: fit-content !important;
      }

      nav.open .hamburger span:nth-child(1) {
        transform: translateY(9px) rotate(45deg);
      }
      nav.open .hamburger span:nth-child(2) {
        opacity: 0;
      }
      nav.open .hamburger span:nth-child(3) {
        transform: translateY(-9px) rotate(-45deg);
      }
    }
"""

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. HTML FIX: Replace hamburger div
    # Match any <div class="hamburger... or id="hamburger"... up to >
    content = re.sub(
        r'<div[^>]*id="hamburger"[^>]*>[\s\S]*?</div>',
        '''<div class="hamburger" id="hamburger" onclick="document.getElementById('navbar').classList.toggle('open')">
        <span></span>
        <span></span>
        <span></span>
    </div>''',
        content
    )
    
    # Also if there's no id="hamburger" but class="hamburger-menu"
    content = re.sub(
        r'<div class="hamburger-menu"[^>]*>[\s\S]*?</div>',
        '''<div class="hamburger" id="hamburger" onclick="document.getElementById('navbar').classList.toggle('open')">
        <span></span>
        <span></span>
        <span></span>
    </div>''',
        content
    )
    
    # 2. CSS FIX
    # Remove Robust Mobile Navigation Fix v2
    content = re.sub(r'/\* --- Robust Mobile Navigation Fix v2 --- \*/[\s\S]*?(?=(/\* --- Vehicle/Blog Mobile Layout Fixes --- \*/|</style>))', '', content)
    
    # Remove @media block inside ULTIMATE CONTACT BUTTON & NAV FIX
    content = re.sub(r'@media screen and \(max-width: 1200px\) \{[\s\S]*?(?=(/\* --- 1\. MASA\w+|/\* --- UNIFIED|</style>))', '', content)
    
    # Remove all the messy appends at the end starting from /* --- 1. MASAÜSTÜ ...
    # We will search for anything that looks like /* --- 1. MASA
    content = re.sub(r'/\* --- 1\. MASA.*[\s\S]*?</style>', '</style>', content, flags=re.IGNORECASE)
    
    # Remove old unified block if we run this script multiple times
    content = re.sub(r'/\* --- UNIFIED MOBILE NAVIGATION --- \*/[\s\S]*?</style>', '</style>', content)
    
    # Insert new unified CSS right before </style>
    if '</style>' in content:
        content = content.replace('</style>', unified_css + '\n  </style>')
    
    # Ensure there are no stray empty media queries created by regex (optional, but good practice)
    content = re.sub(r'@media[^{]*\{\s*\}', '', content)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print(f'Updated {f}')
