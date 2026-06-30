import glob
import re

html_files = glob.glob('*.html')

mobile_layout_css = """
    /* --- Vehicle/Blog Mobile Layout Fixes --- */
    @media (max-width: 900px) {
      .media-row {
        flex-direction: column !important;
        gap: 2rem !important;
      }
      .media-thumb,
      .media-info {
        flex: 0 0 100% !important;
        width: 100% !important;
      }
      .specs-grid {
        grid-template-columns: repeat(2, 1fr) !important;
      }
      .flight-day-gallery .gallery-item {
        flex: 0 0 calc(50% - 0.75rem) !important;
      }
    }
    
    @media (max-width: 480px) {
      .specs-grid {
        grid-template-columns: 1fr !important;
      }
      .flight-day-gallery .gallery-item {
        flex: 0 0 calc(85% - 1rem) !important;
      }
    }
"""

for file_path in html_files:
    if "google" in file_path: continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "/* --- Vehicle/Blog Mobile Layout Fixes --- */" not in content:
        # Find the first </style> tag and insert before it
        idx = content.find('</style>')
        if idx != -1:
            new_content = content[:idx] + mobile_layout_css + "\n  " + content[idx:]
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Applied mobile layout CSS to {file_path}")
