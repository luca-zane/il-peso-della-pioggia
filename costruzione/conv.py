#!/usr/bin/env python3
"""Converte l'export HTML del libro in LaTeX (LuaLaTeX, memoir).
Uso: python3 conv.py libro.html body.tex [--bozza]"""
import re, sys, html as H
from bs4 import BeautifulSoup, NavigableString, Tag

SRC, OUT = sys.argv[1], sys.argv[2]
BOZZA = '--bozza' in sys.argv

SUB = dict(zip('₀₁₂₃₄₅₆₇₈₉ₐₑₒₓₕₖₗₘₙₚₛₜᵢⱼᵣᵤᵥ', '0123456789aeoxhklmnpstijruv'))
SUP = dict(zip('⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻ⁿⁱᵀˣᶻʲˡᵒᵍᵗᵃᵇᶜᵈᵉᶠʰᵏᵐᵖʳˢᵘᵛʷʸ', '0123456789+−niTxzjlogtabcdefhkmprsuvwy'))

def esc(s):
    s = s.replace('\\', '\\textbackslash{}')
    s = re.sub(r'([&%$#_{}])', r'\\\1', s)
    s = s.replace('~', '\\textasciitilde{}').replace('^', '\\textasciicircum{}')
    # pedici e apici Unicode -> comandi LaTeX con le cifre del carattere del testo
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c in SUB or c in SUP:
            tab, cmd = (SUB, 'textsubscript') if c in SUB else (SUP, 'textsuperscript')
            j = i
            while j < len(s) and s[j] in tab: j += 1
            out.append('\\%s{%s}' % (cmd, ''.join(tab[x] for x in s[i:j])))
            i = j
        else:
            out.append(c); i += 1
    s = ''.join(out)
    s = s.replace('...', '…')
    return s

def inline(node):
    if isinstance(node, NavigableString):
        return esc(str(node))
    t = node.name
    inner = ''.join(inline(c) for c in node.children)
    if t == 'strong': return '\\textbf{%s}' % inner
    if t == 'em': return '\\emph{%s}' % inner
    if t == 'code': return '\\code{%s}' % inner
    if t == 'a': return inner
    if t == 'br': return '\\\\'
    if t in ('time', 'span'): return ''
    return inner

def text_of(node):
    return node.get_text() if isinstance(node, Tag) else str(node)

LEAD = [
    ('Maestro:', 'speaker'), ('Allievo:', 'speaker'),
    ('Mokusō.', 'mokuso'),
    ('Dicerie di banchina.', 'runin'),
    ('La lezione per il mondo:', 'mondo'),
    ('Kata per casa.', 'runin'), ("L'ultimo kata per casa.", 'runin'),
    ('Per chi vuole i conti.', 'conti'),
]

def para(p, ctx):
    kids = [k for k in p.children if not (isinstance(k, NavigableString) and not k.strip())]
    first = kids[0] if kids else None
    lead = first.get_text().strip() if isinstance(first, Tag) and first.name == 'strong' else None
    if lead:
        for key, kind in LEAD:
            if lead.startswith(key) and lead == key:
                rest = ''.join(inline(c) for c in list(p.children)[list(p.children).index(first)+1:]).strip()
                if kind == 'speaker':
                    return '\\parla{%s}%s\n' % (key[:-1], rest)
                if kind == 'mokuso':
                    return '\\mokuso{%s}\n' % rest
                if kind == 'mondo':
                    if rest[:1].isalpha(): rest = rest[0].upper() + rest[1:]
                    return '\\mondo{%s}\n' % rest
                if kind == 'conti':
                    return '\\conti{%s}\n' % rest
                return '\\runin{%s}%s\n' % (esc(key.rstrip('.:')), rest)
    body = ''.join(inline(c) for c in p.children).strip()
    if not body: return ''
    # paragrafo tutto in corsivo: una riga di scena
    if len(kids) == 1 and isinstance(first, Tag) and first.name == 'em':
        return '\\scena{%s}\n' % ''.join(inline(c) for c in first.children).strip()
    return body + '\n'

def col_weights(rows):
    n = max(len(r) for r in rows)
    w = [0.0] * n
    for r in rows:
        for i, c in enumerate(r):
            w[i] = max(w[i], min(len(c), 60))
    w = [max(x, 6) ** 0.8 for x in w]
    s = sum(w)
    return [x * n / s for x in w]

def ismath(c):
    return c.strip() != '' and not re.search(r'[A-Za-zàèéìòùÀ-ÿ]{3,}', c) and re.search(r'[0-9=+−×·]', c)

def splittable(x):
    # un conto vero: un solo '=', e prima dell'uguale almeno un'operazione
    return x.count(' = ') == 1 and re.search(r'[+−×·/]', x.split(' = ')[0]) is not None

def due_righe(text):
    w = text.split(' ')
    best = min(range(1, len(w)), key=lambda k: max(len(' '.join(w[:k])), len(' '.join(w[k:])))) if len(w) > 1 else 1
    return [x for x in (' '.join(w[:best]), ' '.join(w[best:])) if x]

def stack(lines):
    if len(lines) == 1: return lines[0]
    return '\\begin{tabular}[t]{@{}l@{}}%s\\end{tabular}' % '\\\\'.join(lines)

def wrap_words(text, width):
    words, lines, cur = text.split(' '), [], ''
    for w_ in words:
        if cur and len(cur) + 1 + len(w_) > width:
            lines.append(cur); cur = w_
        else:
            cur = (cur + ' ' + w_).strip()
    if cur: lines.append(cur)
    return lines

def table(t):
    head = [[c for c in tr.find_all(['th', 'td'])] for tr in t.find('thead').find_all('tr')] if t.find('thead') else []
    body = [[c for c in tr.find_all(['th', 'td'])] for tr in (t.find('tbody') or t).find_all('tr')]
    htxt = [[text_of(c).strip() for c in r] for r in head]
    btxt = [[text_of(c).strip() for c in r] for r in body]
    n = max(len(r) for r in htxt + btxt)
    bcols = [[r[i] if i < len(r) else '' for r in btxt] for i in range(n)]
    hcols = [[r[i] if i < len(r) else '' for r in htxt] for i in range(n)]
    math = []
    for i in range(n):
        cs = [c for c in bcols[i] if c]
        math.append(bool(cs) and sum(1 for c in cs if ismath(c)) / len(cs) >= 0.6)
    # celle "conto = risultato": se le colonne di conti sono troppo larghe, il risultato va a capo dopo il conto, sempre allo stesso modo
    blen = [max([len(x) for x in bcols[i]] + [0]) for i in range(n)]
    split = [False] * n
    mathw = sum(blen[i] + 2 for i in range(n) if math[i])
    compatto = mathw > 62 and sum(1 for i in range(n) if math[i] and any(splittable(x) for x in bcols[i])) >= 3
    if False:
        for i in range(n):
            if math[i] and blen[i] > 12 and any(splittable(x) for x in bcols[i]):
                split[i] = True
                blen[i] = max((max(len(x.rsplit(' = ', 1)[0]) * 0.8, len(x.rsplit(' = ', 1)[1]) + 2)) if splittable(x) else len(x) for x in bcols[i] if x)
    nospace = [all(x.count(' ') <= 1 for x in bcols[i]) and blen[i] <= 30 for i in range(n)]
    short = [(math[i] and blen[i] <= 24) or nospace[i] or max([len(x) for x in bcols[i] + hcols[i]] + [0]) <= 16 for i in range(n)]
    # larghezza naturale stimata: se la tabella sta comoda nella pagina, resta larga quanto serve e va al centro
    def hwidth(i):
        h = ' '.join(hcols[i]).strip()
        lim = max(blen[i], max([len(x) for x in h.split(' ')] + [0]), 14)
        return len(h) if len(h) <= lim + 4 else max(len(x) for x in due_righe(h))
    colw = [max(blen[i], hwidth(i)) for i in range(n)]
    fits = sum(colw) * 4.9 + n * 14 <= 400
    natural = (all(short) or fits) and not compatto
    if natural: short = [True] * n
    longs = [i for i in range(n) if not short[i]]
    cols_all = [bcols[i] + hcols[i] for i in range(n)]
    w = {i: max(sum(len(x) for x in cols_all[i]) / len(cols_all[i]), 8) ** 0.7 for i in longs}
    s = sum(w.values())
    spec = ''
    for i in range(n):
        if short[i]:
            spec += '>{\\raggedright\\arraybackslash}l'
        else:
            spec += '>{\\hsize=%.3f\\hsize\\raggedright\\arraybackslash}X' % (w[i] * len(longs) / s)
    def cell(c, i, hdr):
        tex = ''.join(inline(k) for k in c.children).strip() if c is not None else ''
        if not tex: return ''
        if hdr:
            if short[i]:
                plain = text_of(c).strip()
                width = max(blen[i], max(len(x) for x in plain.split(' ')), 14 if natural else 12)
                if len(plain) > width + 4 and plain == H.unescape(plain) and tex == esc(plain):
                    tex = stack([esc(x) for x in (due_righe(plain) if natural else wrap_words(plain, width))])
            return '\\thead{%s}' % tex
        if split[i] and splittable(text_of(c)) and tex.count(' = ') == 1:
            lhs, rhs = tex.rsplit(' = ', 1)
            return stack(['{\\footnotesize\\color{grigio}%s}' % lhs, '= ' + rhs])
        return tex
    def cells(r, hdr=False):
        cs = [cell(r[i] if i < len(r) else None, i, hdr) for i in range(n)]
        return ' & '.join(cs) + ' \\\\'
    env_forzato = None
    intera = len(body) <= 22  # una tabella breve non si spezza tra due pagine
    if head and head[0] and head[0][0] is not None and text_of(head[0][0]).strip() == 'Scuola':
        env_forzato = 'tabellapiccolabreve'  # la mappa delle scuole apre la lezione 13: piu' fitta, per stare sotto il titolo
    env = 'tabellanaturale' if natural else ('tabellaconti' if compatto else 'tabella')
    if intera: env += 'breve'
    if env_forzato: env = env_forzato; intera = True
    out = ['\\begin{%s}{%s}' % (env, spec), '\\toprule']
    for r in head: out.append(cells(r, True))
    if head:
        out.append('\\midrule' if intera else '\\midrule\\endhead')
    for k, r in enumerate(body):
        out.append(cells(r))
        if k < len(body) - 1: out.append('\\riga')
    out.append('\\bottomrule')
    out.append('\\end{%s}' % env)
    return '\n'.join(out) + '\n'

def lst(l):
    env = 'enumerate' if l.name == 'ol' else 'itemize'
    out = ['\\begin{%s}' % env]
    for li in l.find_all('li', recursive=False):
        parts = []
        for c in li.children:
            if isinstance(c, Tag) and c.name == 'p':
                parts.append(para(c, None).strip())
            elif isinstance(c, Tag) and c.name in ('ol', 'ul'):
                parts.append(lst(c))
            elif isinstance(c, Tag):
                parts.append(inline(c))
            elif str(c).strip():
                parts.append(esc(str(c)))
        txt = '\n\n'.join(x for x in parts if x)
        txt = re.sub(r'^\\parla', r'\\parlaitem', txt)
        out.append('\\item ' + txt)
    out.append('\\end{%s}' % env)
    return '\n'.join(out) + '\n'

def blockquote(b, epigrafe):
    t = b.get_text()
    ps = b.find_all('p')
    if t.startswith('Cronaca del 2026'):
        p = ps[0]; s = p.find('strong')
        titolo = s.get_text().replace('Cronaca del 2026 · ', '').strip(); s.extract()
        return '\\cronaca{%s}{%s}\n' % (esc(titolo), ''.join(inline(c) for c in p.children).strip())
    if t.startswith('Registro del dojo'):
        p = ps[0]; s = p.find('strong')
        titolo = s.get_text().replace('Registro del dojo · ', '').strip(); s.extract()
        return '\\registro{%s}{%s}\n' % (esc(titolo), ''.join(inline(c) for c in p.children).strip())
    if epigrafe:
        p = ps[0]; e = p.find('em')
        q = ''.join(inline(c) for c in e.children).strip(); e.extract()
        autore = p.get_text().strip().lstrip('—').strip()
        return '\\epigrafe{%s}{%s}\n' % (q, esc(autore))
    return '\\begin{quote}\n' + ''.join(para(p, None) for p in ps) + '\\end{quote}\n'

def figure(f):
    nid = f['data-embed'].split('/')[-1]
    cap = ''.join(inline(c) for c in f.find('figcaption').children) if f.find('figcaption') else ''
    if nid == 'e2615d3a-c158':  # il disegno del Maestro, in fondo al foglio
        return '\\disegnomaestro{%s}\n' % nid
    return '\\figura{%s}{%s}\n' % (nid, cap)

def pre(p):
    code = p.find('code')
    lang = (code.get('class') or ['language-text'])[0].replace('language-', '')
    src = code.get_text()
    if lang == 'latex':
        return '\\formula{%s}\n' % src.strip()
    return '\\begin{codice}\n%s\n\\end{codice}\n' % src.rstrip()

LABEL = re.compile(r'^(Prologo|Epilogo|Intermezzo|Lezione \d+|Appendice) · (.+?)(?: \(([^)]*)\))?$')

def chapter(h2):
    t = h2.get_text().strip()
    m = LABEL.match(t)
    if m:
        lab, tit, belt = m.group(1), m.group(2), m.group(3) or ''
        return lab, tit, belt
    return '', t, ''

soup = BeautifulSoup(open(SRC).read(), 'html.parser')
out = []
nodes = [n for n in soup.children if isinstance(n, Tag)]
i = 0
mode = 'front'
just_chapter = False
in_appendix = False
credits = []
while i < len(nodes):
    n = nodes[i]
    if n.name == 'h1':
        i += 1; continue
    if n.name == 'p' and n.find(['time', 'span']):
        i += 1; continue
    if mode == 'front' and n.name == 'p' and n.find('em') and not n.find('strong'):
        out.append('\\epigrafelibro{%s}\n' % ''.join(inline(c) for c in n.find('em').children))
        i += 1; continue
    if n.name == 'h2':
        t = n.get_text().strip()
        if t == 'Crediti e licenza':
            mode = 'credits'; i += 1; continue
        if mode == 'credits':
            out.insert(0, '\\begin{crediti}\n' + ''.join(credits) + '\\end{crediti}\n')
            mode = 'body'
        if t == 'Indice':
            out.append('\\capitolosenzanumero{Il cammino}\n'); just_chapter = True
        elif t == 'Prefazione':
            out.append('\\indice\n\\capitolosenzanumero{Prefazione}\n'); just_chapter = True
        elif t == 'Colofone':
            out.append('\\colofone\n'); mode = 'colofone'
        elif t == 'Le storie del rotolo':
            out.append('\\capitolosenzanumero{Le storie del rotolo}\n'); just_chapter = True
        else:
            lab, tit, belt = chapter(n)
            in_appendix = lab == 'Appendice'
            corto = re.split(r'[:,]', tit)[0].strip(); out.append('\\renewcommand{\\corto}{%s}\\capitolo{%s}{%s}{%s}\n' % (esc(corto), esc(lab), esc(tit), esc(belt))); just_chapter = True
        i += 1; continue
    if mode == 'credits':
        if n.name == 'p':
            txt = n.get_text()
            if BOZZA and txt.startswith('© 2026'):
                credits.append('\\licenzabozza\n\n')
            else:
                credits.append(para(n, None) + '\n')
        i += 1; continue
    if n.name == 'h3':
        t = n.get_text().strip()
        if in_appendix:
            out.append('\\soluzioni{%s}\n' % esc(t))
        else:
            m = re.match(r'^(\w+ seduta) · (.+)$', t)
            if m: out.append('\\seduta{%s}{%s}\n' % (esc(m.group(1)), esc(m.group(2))))
            else: out.append('\\seduta{}{%s}\n' % esc(t))
        just_chapter = False; i += 1; continue
    if n.name == 'blockquote':
        out.append(blockquote(n, just_chapter)); just_chapter = False; i += 1; continue
    just_chapter = False
    if n.name == 'p': out.append(para(n, None))
    elif n.name in ('ol', 'ul'): out.append(lst(n))
    elif n.name == 'table': out.append(table(n))
    elif n.name == 'figure': out.append(figure(n))
    elif n.name == 'pre': out.append(pre(n))
    else: out.append('%% non gestito: %s\n' % n.name)
    i += 1

def virgolette(t):
    out=[]
    for line in t.split('\n'):
        k=[0]
        def rep(m):
            k[0]+=1
            return '“' if k[0]%2 else '”'
        out.append(re.sub(r'"', rep, line))
    return '\n'.join(out)
body = virgolette('\n'.join(out))
open(OUT, 'w').write(body)
print('scritto', OUT, len(body))
