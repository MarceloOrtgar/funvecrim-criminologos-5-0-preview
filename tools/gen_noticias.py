# Genera noticias.html a partir de ley.html (mismo <head>, header y footer),
# el adelanto de las 3 últimas en index.html y el enlace "Noticias" en el menú.
# Uso: python gen_noticias.py <carpeta del repo>
import io, re, sys

R = sys.argv[1]
rd = lambda f: io.open(f'{R}/{f}', encoding='utf-8').read()
wr = lambda f, s: io.open(f'{R}/{f}', 'w', encoding='utf-8', newline='').write(s)

# La primera es la destacada; para sumar una noticia, agregarla ARRIBA de la lista.
N = [
 dict(slug='consultorio-iahula', img='consultorio-iahula.jpg', pos='center 30%', tag='Logro institucional', fecha='Octubre 2026',
  t='Se inaugura el Consultorio de Criminología Clínica en el IAHULA',
  r='Un nuevo espacio en el Instituto Autónomo Hospital Universitario de Los Andes para que los estudiantes de Criminología hagan sus pasantías profesionales.',
  p=['La Escuela de Criminología de la ULA celebró la inauguración del Consultorio de Criminología Clínica en el IAHULA, un logro que abre una oportunidad extraordinaria para que los estudiantes realicen sus pasantías profesionales.',
     'Es un paso firme hacia el crecimiento académico y práctico de la disciplina, que lleva la criminología a nuevos espacios de impacto real y demuestra el valor del perfil profesional en áreas fundamentales de la sociedad.',
     'La Escuela agradeció a las instituciones y personas que lo hicieron posible, en especial al Prof. Félix Ángeles y al criminólogo Orlando Celis, por su dedicación, visión y compromiso con el desarrollo de la disciplina.'],
  cita='¡El futuro de la criminología lo construimos juntos!'),
 dict(slug='diplomado-gerencia-policial', img='diplomado-gerencia-policial.jpg', pos='center 60%', tag='Formación', fecha='Octubre 2026',
  t='Culmina con éxito el Diplomado en Gestión y Gerencia Policial',
  r='Cinco semanas de formación académica para fortalecer las capacidades de los organismos de seguridad del Estado, con el impulso de FUNVECRIM.',
  p=['Tras cinco semanas de trabajo intenso finalizó el Diplomado en Gestión y Gerencia Policial, un espacio de formación académica diseñado para fortalecer las capacidades de los organismos de seguridad del Estado.',
     'La Escuela de Criminología de la ULA agradeció a FUNVECRIM y al comité organizador por la iniciativa, al personal obrero y administrativo, y a los profesores María Gabriela Contreras F., Ivan Toro, Jesús Oduber, Baudilio Márquez, Darisbel Márquez, Rolando Sumoza, Orlando Celis y Roberto Barrios.',
     'La Universidad de Los Andes seguirá sumando espacios de este tipo, convencida de que la profesionalización constante es fundamental para la comunidad.']),
 dict(slug='jornada-psicologia', img='jornada-psicologia.jpg', pos='center 15%', tag='Investigación', fecha='Octubre 2026',
  t='Estudiantes de Criminología, ponentes en la I Jornada de Investigación en Psicología',
  r='José Antonio Artigas y Gabriel Edgardo Mendoza presentaron su trabajo sobre la violencia en espacios de aprendizaje desde el triángulo de Galtung.',
  p=['Los bachilleres José Antonio Artigas y Gabriel Edgardo Mendoza participaron como ponentes en la I Jornada de Investigación en Psicología, en la Facultad de Medicina de la Universidad de Los Andes.',
     'Presentaron su aporte sobre la “violencia ejercida en espacios de aprendizaje desde el modelo del triángulo de Galtung”, que despertó gran interés en el público por su enfoque criminológico.',
     'Su compromiso, dedicación y nivel académico reflejan con orgullo lo que representa la disciplina y la universidad.']),
 dict(slug='liderazgo-femenino', img='liderazgo-femenino.jpg', pos='center 35%', tag='Liderazgo', fecha='Octubre 2026',
  t='Criminólogas culminan la Primera Escuela de Liderazgo Femenino e Innovación Política',
  r='Baudimar Araque, Ayleen Erazo, Darisbel Márquez y Rusmairy Rubio completaron el programa de la ONG Juntas Nos Crecieron Alas y la ULA.',
  p=['Baudimar Araque, Ayleen Erazo, Darisbel Márquez y Rusmairy Rubio culminaron con éxito la Primera Escuela de Liderazgo Femenino e Innovación Política del país, organizada por la ONG Juntas Nos Crecieron Alas y la Universidad de Los Andes.',
     'Las participantes de la Escuela de Criminología de la ULA siguen fortaleciendo sus capacidades de liderazgo y construyendo herramientas para la transformación social, hacia una sociedad más justa e igualitaria.',
     'La Escuela agradeció a la profesora María Gabriela Contreras, facilitadora de uno de los módulos, y a la criminóloga Josy Querales, organizadora de la iniciativa.'],
  cita='¡Que nunca nos falten las alas ni el valor para transformar nuestra realidad!'),
 dict(slug='i-encuentro-gracias', img=None, tag='Comunidad estudiantil', fecha='Octubre 2026',
  t='Gracias por hacer posible el I Encuentro de Criminología',
  r='Las consejeras estudiantiles agradecen la participación y anuncian una próxima Asamblea de Estudiantes.',
  p=['Las consejeras de la Escuela de Criminología, Rusmairy y Michell, agradecieron a todos los que se sumaron al I Encuentro de Criminología: ver el evento lleno de vida y a los estudiantes comprometidos con lo que estudian les recuerda por qué aman esta carrera.',
     'Muy pronto convocarán una Asamblea de Estudiantes, un espacio relajado para conversar sobre lo vivido en el encuentro y recoger sugerencias, dudas o inquietudes sobre la escuela.',
     'Invitan a seguir participando y a contar qué les pareció el encuentro: la experiencia de los estudiantes es lo más valioso para seguir construyendo una mejor escuela.']),
]
FUENTE = 'Escuela de Criminología ULA'


def media(n, cls=''):
    if n['img']:
        return f'<img class="{cls}" src="assets/noticias/{n["img"]}" alt="{n["t"]}" loading="lazy" style="object-position:{n.get("pos", "center")}" />'
    return f'<div class="{cls} n-noimg" aria-hidden="true"><span>I Encuentro<br>de Criminología</span></div>'


def body(n):
    s = ''.join(f'<p>{x}</p>' for x in n['p'])
    if n.get('cita'):
        s += f'<blockquote>{n["cita"]}</blockquote>'
    return s + f'<p class="n-src">Fuente: {FUENTE}</p>'


f = N[0]
feat = f'''<article class="n-feat" id="{f['slug']}">
   <div class="n-feat-media">{media(f)}</div>
   <div class="n-feat-copy">
    <div class="n-meta"><span class="n-tag">{f['tag']}</span><span>{f['fecha']}</span></div>
    <h2>{f['t']}</h2>
    {body(f)}
   </div>
  </article>'''
cards = '\n'.join(f'''   <article class="n-card" id="{n['slug']}">
    <div class="n-media">{media(n)}</div>
    <div class="n-body">
     <div class="n-meta"><span class="n-tag">{n['tag']}</span><span>{n['fecha']}</span></div>
     <h3>{n['t']}</h3>
     <p class="n-sum">{n['r']}</p>
     <details><summary>Leer noticia completa</summary>{body(n)}</details>
    </div>
   </article>''' for n in N[1:])

CSS = '''
/* Noticias */
.n-hero{grid-template-columns:1fr!important}.n-hero h1{max-width:820px}
.n-wrap{padding:64px 0 76px}
.n-feat{display:grid;grid-template-columns:1fr 1.1fr;background:#fff;border:1px solid var(--line);border-radius:24px;overflow:hidden;box-shadow:var(--shadow);margin-bottom:34px}
.n-feat-media img,.n-feat-media .n-noimg{width:100%;height:100%;min-height:420px;object-fit:cover;display:block}
.n-feat-copy{padding:36px 38px}
.n-feat-copy h2{font-size:clamp(26px,3vw,36px);line-height:1.12;margin:12px 0 16px;color:var(--navy)}
.n-feat-copy p,.n-card details p{color:#3d4b59;font-size:16px;line-height:1.65;margin:0 0 12px}
.n-meta{display:flex;align-items:center;flex-wrap:wrap;gap:10px 12px;font-size:13px;color:var(--muted);font-weight:700}
.n-tag{background:rgba(226,167,63,.16);color:#8a5a10;border-radius:999px;padding:5px 12px;letter-spacing:.06em;text-transform:uppercase;font-size:11px;font-weight:800}
.n-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:24px}
.n-card{background:#fff;border:1px solid var(--line);border-radius:20px;overflow:hidden;box-shadow:0 10px 30px rgba(13,33,28,.05);display:flex;flex-direction:column;transition:transform .25s ease,box-shadow .25s ease}
.n-card:hover{transform:translateY(-4px);box-shadow:var(--shadow)}
.n-media img,.n-media .n-noimg{width:100%;aspect-ratio:16/10;object-fit:cover;display:block}
.n-noimg{background:linear-gradient(135deg,#0a3258,#1b5a86 60%,#2f8a8a);display:grid;place-items:center;color:#fff}
.n-noimg span{font-family:Georgia,'Iowan Old Style',serif;font-size:26px;line-height:1.15;border-left:4px solid var(--gold);padding-left:16px}
.n-body{padding:22px 24px 24px;display:flex;flex-direction:column;flex:1}
.n-body h3{font-size:21px;line-height:1.2;margin:12px 0 10px;color:var(--navy)}
.n-sum{color:var(--muted);font-size:15px;line-height:1.55;margin:0 0 14px}
.n-card details{margin-top:auto;border-top:1px solid var(--line);padding-top:12px}
.n-card summary{cursor:pointer;font-weight:800;color:var(--navy);font-size:14px;list-style:none}
.n-card summary::-webkit-details-marker{display:none}
.n-card summary::after{content:' ›';color:var(--gold)}
.n-card details[open] summary::after{content:' ‹'}
.n-card details[open] summary{margin-bottom:12px}
.n-feat blockquote,.n-card blockquote{margin:6px 0 12px;padding:10px 16px;border-left:4px solid var(--gold);background:var(--paper);border-radius:0 12px 12px 0;font-style:italic;color:var(--navy)}
.n-src{font-size:13px!important;color:var(--muted)!important;font-weight:700}
.n-more{text-align:center;margin-top:34px;color:var(--muted);font-size:15px}
@media(max-width:920px){.n-feat{grid-template-columns:1fr}.n-feat-media img,.n-feat-media .n-noimg{min-height:0;height:auto;aspect-ratio:4/3}.n-feat-copy{padding:26px 22px}}
@media(max-width:700px){.n-grid{grid-template-columns:1fr}.n-wrap{padding:44px 0 56px}}
'''

# --- noticias.html ---
ley = rd('ley.html')
head, rest = ley.split('<main id="inicio">', 1)
tail = rest[rest.index('</main>'):]
head = re.sub(r'<title>.*?</title>', '<title>Noticias | Criminólogos 5.0</title>', head)
head = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1) + 'Noticias de la comunidad criminológica venezolana: formación, investigación y logros institucionales.', head)
head = head.replace('</style>', CSS + '</style>', 1)
main = f'''<main id="inicio">
<section class="t-hero">
 <div class="container t-hero-inner n-hero">
  <div>
   <a class="t-back" href="index.html#noticias">‹ Volver a Criminólogos 5.0</a>
   <div class="kicker">Comunidad criminológica</div>
   <h1>Noticias <em>de la criminología venezolana</em></h1>
   <p class="t-sub">Logros, formación e investigación de quienes construyen la disciplina en el país.</p>
  </div>
 </div>
</section>

<section class="n-wrap">
 <div class="container">
  {feat}
  <div class="n-grid">
{cards}
  </div>
  <p class="n-more">¿Tienes una noticia para la comunidad? Escríbenos a <a href="mailto:Funvecrim@gmail.com">Funvecrim@gmail.com</a>.</p>
 </div>
</section>

<section class="cta">
 <div class="container cta-inner">
  <div class="cta-copy">
   <small>Las noticias también las haces tú</small>
   <h2>Súmate al <span>movimiento</span></h2>
   <p>Regístrate, participa en la Consulta Nacional y fórmate con el gremio criminológico venezolano.</p>
  </div>
  <a class="btn" href="index.html#participa">Únete a la iniciativa <span>›</span></a>
 </div>
</section>
'''
wr('noticias.html', head + main + tail)

# --- adelanto en index.html (las 3 últimas) ---
idx = rd('index.html')
teaser_cards = '\n'.join(f'''    <a class="n-card" href="noticias.html#{n['slug']}">
     <div class="n-media">{media(n)}</div>
     <div class="n-body"><div class="n-meta"><span class="n-tag">{n['tag']}</span><span>{n['fecha']}</span></div><h3>{n['t']}</h3><p class="n-sum">{n['r']}</p><span class="n-link">Leer más ›</span></div>
    </a>''' for n in N[:3])
teaser = f'''<!-- NOTICIAS (las 3 últimas; se generan con gen_noticias.py) -->
<section class="n-teaser" id="noticias">
 <div class="container">
  <div class="section-head">
   <div class="eyebrow">Noticias</div>
   <h2>Lo que está pasando en la criminología venezolana</h2>
   <p>Formación, investigación y logros de nuestra comunidad.</p>
  </div>
  <div class="n-grid3">
{teaser_cards}
  </div>
  <div class="n-all"><a class="btn navy" href="noticias.html">Ver todas las noticias <span>›</span></a></div>
 </div>
</section>
<!-- /NOTICIAS -->
'''
TCSS = CSS + '''.n-teaser{padding:70px 0}
.n-grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
a.n-card{text-decoration:none;color:inherit}
.n-link{margin-top:auto;font-weight:800;color:var(--navy);font-size:14px}
.n-all{text-align:center;margin-top:30px}
@media(max-width:920px){.n-grid3{grid-template-columns:1fr 1fr}}
@media(max-width:620px){.n-grid3{grid-template-columns:1fr}}
/* /Noticias */
'''
if '<!-- NOTICIAS' in idx:
    idx = re.sub(r'<!-- NOTICIAS.*?<!-- /NOTICIAS -->\n', lambda m: teaser, idx, flags=re.S)
    idx = re.sub(r'\n/\* Noticias \*/.*?/\* /Noticias \*/\n', lambda m: TCSS, idx, count=1, flags=re.S)
else:
    a = idx.index('<section class="cta">', idx.index('id="acciones"'))
    idx = idx[:a] + teaser + '\n' + idx[a:]
    idx = idx.replace('</style>', TCSS + '</style>', 1)
wr('index.html', idx)

# --- "Noticias" en el menú de todas las páginas ---
for fn, href in [('index.html', '#noticias'), ('ley.html', 'noticias.html'), ('noticias.html', 'noticias.html'), ('taller.html', 'noticias.html')]:
    s = rd(fn)
    if '>Noticias</a>' in s:
        continue
    cls = ' class="full"' if fn == 'taller.html' else ''
    s, n = re.subn(r'(<a(?: class="full")? href="(?:index\.html)?#acciones">Acciones</a>)',
                   lambda m: m.group(1) + f'<a{cls} href="{href}">Noticias</a>', s, count=1)
    assert n == 1, fn
    wr(fn, s)
print('ok')
