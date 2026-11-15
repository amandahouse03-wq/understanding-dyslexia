#!/usr/bin/env python3
"""Builds the published site in site/ from the two source pages in src/.

    python3 build.py

src/home.html        the home page (title, styles, content, script)
src/simulation.html  the simulation (same shape)
Videos, posters, the icon and the share image already live in site/ and are left alone.
"""
import pathlib, re
ROOT = pathlib.Path(__file__).parent
URL = 'https://www.understanding-dyslexia.com/'
DESC = 'What school is really like with dyslexia, dysgraphia and dyscalculia, from a high school junior who lives it. Four short videos and an interactive simulation.'
RESET = '<style>html{color-scheme:light;-webkit-text-size-adjust:100%}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'

def split(src):
    src = re.sub(r'<meta name="claude:[^>]*>\n', '', src)
    i = src.index('</style>') + len('</style>')
    return src[:i].strip(), src[i:].strip()

def page(head, body, title, desc, path):
    head = re.sub(r'<title>.*?</title>\n?', '', head)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{URL}{path}">
<link rel="icon" href="{'../' if path else ''}favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{URL}{path}">
<meta property="og:image" content="{URL}og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{RESET}{head}
</head>
<body>
{body}
</body>
</html>
'''

home_head, home_body = split((ROOT / 'src/home.html').read_text(encoding='utf-8'))
(ROOT / 'site/index.html').write_text(page(home_head, home_body, 'Understanding Dyslexia', DESC, ''), encoding='utf-8')

sim_head, sim_body = split((ROOT / 'src/simulation.html').read_text(encoding='utf-8'))
# a way back to the home page, shown only when the simulation is opened on its own (not inside the home page's frame)
marker = '\n</section>\n\n<section class="screen" id="between"'
assert sim_body.count(marker) == 1
sim_body = sim_body.replace(marker, '\n  <p class="muted" id="backLink"><a href="../index.html" target="_top">Back to Understanding Dyslexia</a></p>' + marker)
sim_body += '\n<script>if (window.self !== window.top) document.getElementById("backLink").hidden = true;</script>'
(ROOT / 'site/simulation').mkdir(exist_ok=True)
(ROOT / 'site/simulation/index.html').write_text(page(sim_head, sim_body, 'The Simulation | Understanding Dyslexia', 'An interactive simulation of a school day with dyslexia, dysgraphia and dyscalculia: a reading quiz, a lecture, a written response and a math quiz.', 'simulation/'), encoding='utf-8')
print('built site/index.html and site/simulation/index.html')
