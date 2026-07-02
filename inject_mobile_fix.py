import os
import glob

# The files we want to modify
html_files = glob.glob('*.html')

css_link = '  <link rel="stylesheet" href="mobile-fix.css">\n'

js_script = """
  <!-- MOBILE NAV FIX JS -->
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      var hamburger = document.querySelector('.hamburger');
      var navbar = document.getElementById('navbar');
      if(hamburger && navbar) {
        // Remove old onclick attribute to prevent conflicts
        hamburger.removeAttribute('onclick');
        
        // Add robust event listener
        hamburger.addEventListener('click', function(e) {
          e.preventDefault();
          e.stopPropagation();
          navbar.classList.toggle('open');
        });
        
        // Close menu when a link is clicked
        var navLinks = document.querySelectorAll('.nav-links a');
        navLinks.forEach(function(link) {
          link.addEventListener('click', function() {
            navbar.classList.remove('open');
          });
        });
      }
    });
  </script>
"""

for file_path in html_files:
    if file_path == 'live_test_mobile.html':
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if already injected
    if 'mobile-fix.css' in content:
        print(f"Skipping {file_path}, already injected.")
        continue
        
    # Inject CSS before </head>
    if '</head>' in content:
        content = content.replace('</head>', css_link + '</head>')
        
    # Inject JS before </body>
    if '</body>' in content:
        content = content.replace('</body>', js_script + '</body>')
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Successfully injected fixes into {file_path}")
