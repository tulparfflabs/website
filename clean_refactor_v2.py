import glob
import re

files = glob.glob('*.html')

unified_css = """
    /* --- UNIFIED MOBILE NAVIGATION --- */
    .hamburger {
      display: none;
      flex-direction: column;
      justify-content: space-between;
      width: 30px;
      height: 21px;
      cursor: pointer;
      z-index: 1001;
    }
    
    .hamburger span {
      display: block;
      width: 100%;
      height: 3px;
      background: var(--text);
      border-radius: 2px;
      transition: all 0.3s ease-in-out;
      transform-origin: left center;
    }

    @media screen and (max-width: 1200px) {
      nav .nav-links,
      nav .search-wrap,
      nav .lang-switcher {
        display: none !important;
      }

      .hamburger {
        display: flex !important;
        position: absolute;
        right: 20px;
        top: 50%;
        transform: translateY(-50%);
      }

      nav.open .nav-links {
        display: flex !important;
        flex-direction: column !important;
        position: absolute !important;
        top: 60px !important; /* height of nav */
        left: 0 !important;
        right: 0 !important;
        background: rgba(255, 255, 255, 0.98) !important;
        padding: 20px 0 !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1) !important;
        gap: 15px !important;
        /* Start of slide down animation */
        clip-path: polygon(0 0, 100% 0, 100% 0, 0 0);
        animation: slideDown 0.4s ease forwards;
      }

      @keyframes slideDown {
        to {
            clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
        }
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

      /* Animated X */
      nav.open .hamburger span:nth-child(1) {
        transform: rotate(45deg);
        width: 34px;
      }
      nav.open .hamburger span:nth-child(2) {
        opacity: 0;
      }
      nav.open .hamburger span:nth-child(3) {
        transform: rotate(-45deg);
        width: 34px;
      }
    }
"""

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Update the Unified CSS block if it exists
    if '/* --- UNIFIED MOBILE NAVIGATION --- */' in content:
        content = re.sub(r'/\* --- UNIFIED MOBILE NAVIGATION --- \*/[\s\S]*?</style>', unified_css + '\n  </style>', content)
    else:
        content = content.replace('</style>', unified_css + '\n  </style>')
        
    # 2. Remove the old messy script tag at the bottom (if exists)
    content = re.sub(r'<script>\s*const hamburgerMenuBtn = document\.getElementById\(\'hamburger\'\);[\s\S]*?</script>', '', content)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print(f'Updated {f}')
