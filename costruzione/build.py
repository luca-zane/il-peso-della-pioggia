#!/usr/bin/env python3
"""Costruisce il PDF del libro. Uso: python3 build.py [--bozza]"""
import subprocess, sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
bozza = '--bozza' in sys.argv
subprocess.run(['python3', 'conv.py', '../testo/il-peso-della-pioggia.html', 'body.tex'] + (['--bozza'] if bozza else []), check=True)
body = open('body.tex').read()
# righe di scena consecutive: dalla seconda in poi rientrano come un paragrafo normale
_out=[]; _prev=False
for _l in body.split('\n'):
    if not _l.strip():
        _out.append(_l); continue
    if _l.startswith('\\scena{') and _prev:
        _l='\\scenacont{'+_l[len('\\scena{'):]
    _prev=_l.startswith('\\scena{') or _l.startswith('\\scenacont{')
    _out.append(_l)
body='\n'.join(_out)
open('body.tex','w').write(body)
cut = body.index('\\renewcommand{\\corto}{La soglia del dojo}')
open('body-front.tex', 'w').write(body[:cut])
open('body-main.tex', 'w').write(body[cut:])
with open('versione.tex', 'w') as f:
    if bozza:
        f.write('\\newcommand{\\notabozza}{{\\sffamily\\fontsize{6.5}{8}\\selectfont\\color{grigio}Bozza 0.99 per i primi lettori · non diffondere}}\n')
        f.write('\\newcommand{\\BOZZA}{BOZZA 0.99 PER I PRIMI LETTORI · NON DIFFONDERE}\n')
    else:
        f.write('\\newcommand{\\notabozza}{}\n\\newcommand{\\BOZZA}{}\n')
for _ in range(3):
    r = subprocess.run(['lualatex', '-interaction=nonstopmode', '-halt-on-error', 'libro.tex'], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-4000:]); sys.exit(1)
# copertina davanti, titolo e autore nei metadati: il file che si scarica
nome = 'il-peso-della-pioggia-bozza.pdf' if bozza else 'il-peso-della-pioggia.pdf'
try:
    import pikepdf
    with pikepdf.open('copertina/copertina.pdf') as cop, pikepdf.open('libro.pdf') as lib:
        out = pikepdf.new()
        out.pages.extend(cop.pages); out.pages.extend(lib.pages)
        out.docinfo['/Title'] = 'Il peso della pioggia'
        out.docinfo['/Author'] = 'Luca Zane'
        out.docinfo['/Subject'] = "L'intelligenza artificiale dal neurone ai modelli che ragionano"
        out.save(nome)
except ImportError:
    subprocess.run(['pdfunite', 'copertina/copertina.pdf', 'libro.pdf', nome], check=True)
print('ok:', nome)
