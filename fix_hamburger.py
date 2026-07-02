import os
import re

files = ['blog-yolo11.html', 'blog.html', 'contact.html', 'team.html', 'vehicle.html']

for file in files:
    if not os.path.exists(file):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Remove the first redundant .hamburger block (if exists)
    pattern1 = re.compile(r'\s*\.hamburger\s*\{\s*display:\s*none;\s*flex-direction:\s*column;\s*gap:\s*5px;\s*background:\s*none;\s*border:\s*none;\s*cursor:\s*pointer;\s*padding:\s*4px;\s*\}\s*\.hamburger\s*span\s*\{\s*display:\s*block;\s*width:\s*22px;\s*height:\s*2px;\s*background:\s*var\(--text\);\s*border-radius:\s*2px;\s*(?:transition:\s*all\s*\.3s;\s*)?\}', re.MULTILINE)
    content = pattern1.sub('', content)

    # 2. Replace the second block
    pattern2 = re.compile(r'\s*\.hamburger\s*\{\s*flex-direction:\s*column;\s*justify-content:\s*space-between;.*?nav\.open\s*\.hamburger\s*span:nth-child\(3\)\s*\{\s*transform:\s*rotate\(-45deg\);\s*width:\s*34px;\s*\}\s*\}', re.DOTALL)
    
    replacement = r'''
    .hamburger {
      flex-direction: column;
      justify-content: space-between;
      width: 30px;
      height: 21px;
      cursor: pointer;
      z-index: 1001;
      display: none; /* By default hidden on desktop */
      background: none;
      border: none;
      padding: 0;
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

    /* DESKTOP EXPLICIT FIX */
    @media screen and (min-width: 1025px) {
      .hamburger {
        display: none !important;
      }
    }

    /* MOBILE NAVIGATION */
    @media screen and (max-width: 1024px) {
      nav {
        padding: 0 1rem !important;
      }
      
      nav .nav-logo {
        flex-shrink: 0 !important;
        position: relative;
        z-index: 1002;
      }

      nav .nav-links,
      nav .search-wrap,
      nav .lang-switcher,
      .top-right-lang {
        display: none !important;
      }

      .hamburger {
        display: flex !important;
        position: absolute;
        right: 20px;
        top: 50%;
        transform: translateY(-50%);
        z-index: 1002;
      }

      nav.open .nav-links {
        display: flex !important;
        flex-direction: column !important;
        position: fixed !important;
        top: 60px !important; /* height of nav */
        left: 0 !important;
        right: 0 !important;
        background: rgba(255, 255, 255, 0.98) !important;
        padding: 20px 0 !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1) !important;
        gap: 15px !important;
        border-bottom: 1px solid var(--border);
        z-index: 1000;
        animation: fadeIn 0.3s ease forwards;
        clip-path: none;
      }

      @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
      }

      nav.open .nav-links li {
        width: 100% !important;
        text-align: center !important;
      }

      nav.open .nav-links a {
        display: inline-block !important;
        padding: 12px 20px !important;
        color: var(--text) !important;
        background: transparent !important;
        border: none !important;
        font-size: 1.1rem !important;
        width: 100%;
      }
      
      nav.open .nav-links .nav-cta {
          margin: 0 auto !important;
          width: 80% !important;
          background: #DB1A1A !important;
          color: #FFF !important;
          border-radius: 6px !important;
      }

      /* Animated X */
      nav.open .hamburger span:nth-child(1) {
        transform: rotate(45deg);
        width: 24px;
      }
      nav.open .hamburger span:nth-child(2) {
        opacity: 0;
      }
      nav.open .hamburger span:nth-child(3) {
        transform: rotate(-45deg);
        width: 24px;
      }
    }'''
    
    content = pattern2.sub(replacement, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file}")
