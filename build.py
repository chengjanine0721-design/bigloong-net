# -*- coding: utf-8 -*-
"""Bigloong static site generator - English piano guide & experience blog.
Design language adapted from hoffmanacademy.com (gold + indigo, rounded, friendly).
URL architecture:
  /, /blog/, /blog/{slug}/, /faq/, /faq/{slug}/, /video-tutorial/, /video-tutorial/{slug}/
  /about-us/ (file about/index.html), /contact-us/ (file contact/index.html)
  /privacy/, /terms/, /404.html, /sitemap.xml, /robots.txt
"""
import os
import json

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "bigloong.net"
AUTHOR = "Alice Baker"
EMAIL = "contact@bigloong.net"

# ---------------------------- data ----------------------------

POSTS = [
    {
        "slug": "how-much-does-a-piano-cost",
        "cat": "Buying Guide",
        "title": "How Much Does a Piano Cost in 2026",
        "desc": "A complete price guide by piano type. Compare digital pianos, uprights and grand pianos, brand prices and the hidden costs of ownership.",
        "emoji": "\U0001F3B9",
        "c1": "#FFF0C9", "c2": "#E7E5F6",
        "date": "2026-11-19",
        "read": "12 min read",
        "seo_title": "How Much Does a Piano Cost in 2026? Complete Price Guide by Type",
        "full_h1": "How Much Does a Piano Cost in 2026? (Complete Price Guide by Type)",
        "body_file": "_piano_cost_body.html",
        "image": "/assets/img/how-to-start-learning-piano/average-piano-pricing.webp",
        "keywords": "how much does a piano cost, piano prices, digital piano cost, upright piano cost, steinway piano cost",
        "toc": [
            ("price-by-type", "Price Ranges by Type"),
            ("digital-pianos", "Digital Pianos and Keyboards"),
            ("upright-pianos", "Acoustic Upright Pianos"),
            ("grand-pianos", "Grand Pianos"),
            ("prices-by-brand", "Prices by Brand"),
            ("choose-by-budget", "Choose by Budget"),
            ("beginners", "Piano Costs for Beginners"),
            ("faq", "FAQ"),
            ("conclusion", "Conclusion"),
        ],
        "faqs": [
            ("What is the 80/20 rule for piano", "The 80/20 rule means roughly 80 percent of your progress comes from 20 percent of your practice. Spend most of your time on the few difficult bars that hold a piece back rather than playing it from the top again and again."),
            ("Does piano lower cortisol", "Playing the piano is an active form of music engagement that several studies link to reduced cortisol, the body's stress hormone. Practising and playing for pleasure can lower stress and improve mood."),
        ],
    },
    {
        "slug": "how-to-start-learning-piano",
        "cat": "Beginner Guide",
        "title": "How to Start Learning Piano as a Beginner",
        "desc": "15 quick tips on how to start learning piano, from choosing your first keyboard and finding middle C to finger technique and a simple daily practice routine.",
        "emoji": "\U0001F3B9",
        "c1": "#FFF0C9", "c2": "#FBE8F2",
        "date": "2026-11-18",
        "read": "18 min read",
        "seo_title": "A Full Guide to Start Learning Piano as a Beginner [15 Quick Tips]",
        "full_h1": "How to Start Learning Piano as a Beginner: 15 Quick Tips (Everything You Need to Know)",
        "body_file": "_piano_article_body.html",
        "image": "/assets/img/how-to-start-learning-piano/average-piano-pricing.webp",
        "keywords": "how to start learning piano, learn piano by yourself, piano for beginners, piano tips",
        "toc": [
            ("instrument", "1. Get the Right Instrument"),
            ("hand-position", "Hand and Finger Positioning"),
            ("know-the-keys", "2. Know the Piano and Keys"),
            ("beginner-songs", "3. Play Beginner Songs"),
            ("how-to-learn", "4. Choose How You Learn"),
            ("daily-practice", "5. Daily Finger Exercises"),
            ("mistakes", "6. Common Mistakes"),
            ("faq", "FAQ"),
            ("conclusion", "Conclusion"),
        ],
        "faqs": [
            ("How Long Until I Can Play a Song", "It depends on practice frequency, method and song difficulty. A simple melody may come within days or weeks, while a full two hand song takes longer."),
            ("Do I Need to Learn to Read Music", "Not before your first song, but it is highly recommended for long term progress. Start with a few notes and use free tools such as musictheory.net."),
            ("Should a Beginner Get a Piano Teacher", "If you can afford one, a teacher is the most reliable path to good technique. On a budget, self teaching with method books and video lessons works well."),
        ],
    },
]

FAQS = [
    {
        "slug": "how-often-should-i-tune-a-piano",
        "q": "How often should I tune a piano",
        "a": "A new piano should be tuned two to four times in its first year as the strings settle. After that, twice a year is a good rhythm for most homes. Pianos in dry or humid climates, or those used for teaching, may need more frequent tuning.",
    },
    {
        "slug": "digital-or-acoustic-piano-for-beginners",
        "q": "Digital or acoustic piano for beginners",
        "a": "A weighted digital piano is the best start for most beginners. It costs less, needs no tuning, fits small spaces and lets you practise with headphones. Choose an acoustic upright when you want a traditional touch and have a dedicated room and a long term budget.",
    },
    {
        "slug": "how-long-does-it-take-to-learn-piano",
        "q": "How long does it take to learn piano",
        "a": "With short daily practice, most players can play a simple two hand song within four to eight weeks. Reaching a confident intermediate level usually takes one to three years. Consistency matters far more than long occasional sessions.",
    },
    {
        "slug": "best-age-to-start-piano-lessons",
        "q": "Best age to start piano lessons",
        "a": "Many children start formal lessons between four and six, once they can focus for a short session and recognise left from right. Adults can start at any age and often progress quickly because they understand practice and choose their own repertoire.",
    },
    {
        "slug": "do-i-need-a-piano-teacher",
        "q": "Do I need a piano teacher",
        "a": "A teacher gives the fastest reliable progress and catches technique problems early. If that is not in the budget, structured method books plus video lessons work well. Either way, regular feedback on what you play is the key ingredient.",
    },
    {
        "slug": "what-is-the-80-20-rule-for-piano",
        "q": "What is the 80/20 rule for piano",
        "a": "The 80/20 rule means roughly 80 percent of your progress comes from 20 percent of your practice. Rather than playing a piece from the top again and again, isolate the few hard passages and repeat them slowly and correctly until they become easy.",
    },
]

VIDEOS = [
    {
        "slug": "piano-posture-for-beginners",
        "title": "Piano Posture for Beginners",
        "desc": "Sit tall, relax your shoulders and find the right bench height. Good posture prevents tension and makes every note easier to play.",
        "duration": "6:12",
        "emoji": "\U0001F9D8",
        "c1": "#FFF0C9", "c2": "#E7E5F6",
        "steps": [
            "Place the bench so your forearms are level with the keyboard when your fingers rest on the keys.",
            "Sit on the front half of the bench with feet flat on the floor and a straight but relaxed back.",
            "Keep elbows slightly away from your body and let your shoulders drop.",
            "Curve your fingers naturally and play from the weight of your arm rather than finger force alone.",
        ],
    },
    {
        "slug": "finding-middle-c-on-piano",
        "title": "Finding Middle C on a Piano",
        "desc": "Middle C is your home base on the keyboard. Learn two quick ways to find it every time you sit down to play.",
        "duration": "4:35",
        "emoji": "\U0001F3B9",
        "c1": "#E7E5F6", "c2": "#FFF0C9",
        "steps": [
            "Look for the group of two black keys near the centre of the keyboard.",
            "The white key immediately to the left of that pair is middle C.",
            "On a full 88 key piano, middle C is also the fourth C counted up from the lowest note.",
            "Mark it once with a removable sticker if you are new, then remove it as your reading improves.",
        ],
    },
    {
        "slug": "first-piano-song-tutorial",
        "title": "Your First Piano Song Tutorial",
        "desc": "Put a few notes together in a simple melody you can play in your first week. Slow, even practice is the whole secret.",
        "duration": "9:48",
        "emoji": "\U0001F3B5",
        "c1": "#FFF0C9", "c2": "#DFF3E4",
        "steps": [
            "Learn the right hand melody one phrase at a time, three notes at a time.",
            "Practise slowly with a steady count until the notes feel automatic.",
            "Add the left hand only when the melody is comfortable.",
            "Play hands together at a slow tempo, then gradually increase speed.",
        ],
    },
    {
        "slug": "piano-scales-for-beginners",
        "title": "Piano Scales for Beginners",
        "desc": "Start with C major and learn a clean fingering pattern that unlocks dozens of songs and builds coordination.",
        "duration": "7:20",
        "emoji": "\U0001F3B9",
        "c1": "#E7E5F6", "c2": "#FFF0C9",
        "steps": [
            "Begin on middle C and play only the white keys up to the next C.",
            "Use fingers 1 2 3 1 2 3 4 5 going up, and reverse coming down.",
            "Keep a steady rhythm with a metronome set to a comfortable speed.",
            "Practise hands separately first, then put them together once each is smooth.",
        ],
    },
]

# ---------------------------- shared partials ----------------------------

def head(title, description, jsonld="", keywords="", canonical="/"):
    kw = ('<meta name="keywords" content="%s">' % keywords) if keywords else ""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
{kw}
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Bigloong">
<link rel="canonical" href="https://{SITE}{canonical}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&family=Poppins:wght@500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css">
{jsonld}
</head>
<body>
'''

def breadcrumb(crumbs):
    parts = []
    for i, (label, url) in enumerate(crumbs):
        if url:
            parts.append(f'<a href="{url}">{label}</a>')
        else:
            parts.append(f'<span class="cur">{label}</span>')
        if i < len(crumbs) - 1:
            parts.append('<span class="sep"></span>')
    return f'''<div class="breadcrumb"><div class="wrap">
{''.join(parts)}
</div></div>'''

def header(active=""):
    def cls(name):
        return "nav-link active" if active == name else "nav-link"
    return f'''<header class="site-header"><div class="wrap">
<nav class="nav">
  <a href="/" class="brand"><span class="brand-mark">B</span>bigloong<span class="dot">.</span></a>
  <button class="menu-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
  <ul class="nav-links">
    <li><a href="/" class="{cls('home')}">Home</a></li>
    <li><a href="/blog/" class="{cls('blog')}">Blog</a></li>
    <li><a href="/faq/" class="{cls('faq')}">FAQ</a></li>
    <li><a href="/video-tutorial/" class="{cls('video')}">Video Tutorial</a></li>
    <li class="has-drop"><a href="/about-us/" class="{cls('more')}">More <span class="caret"></span></a>
      <div class="dropdown">
        <a href="/about-us/"><span class="ico">i</span>About Us</a>
        <a href="/privacy/"><span class="ico">&#128274;</span>Privacy</a>
        <a href="/contact-us/"><span class="ico">&#9993;</span>Contact Us</a>
        <a href="/terms/"><span class="ico">&#167;</span>Terms</a>
      </div>
    </li>
    <li><a href="/blog/" class="btn btn-primary btn-sm nav-cta">Explore guides</a></li>
  </ul>
</nav>
</div></header>'''

def footer():
    return f'''<footer class="site-footer"><div class="wrap">
<div class="footer-grid">
  <div class="footer-brand">
    <a href="/" class="brand"><span class="brand-mark">B</span>bigloong<span class="dot">.</span></a>
    <p>Practical piano guides, clear tutorials and honest buying advice. Made for players who want to spend less time guessing and more time playing.</p>
  </div>
  <div class="footer-col">
    <h4>Explore</h4>
    <a href="/">Home</a>
    <a href="/blog/">Blog</a>
    <a href="/faq/">FAQ</a>
    <a href="/video-tutorial/">Video Tutorial</a>
  </div>
  <div class="footer-col">
    <h4>Learn</h4>
    <a href="/blog/how-to-start-learning-piano/">Start learning piano</a>
    <a href="/blog/how-much-does-a-piano-cost/">Piano prices</a>
    <a href="/faq/">Common questions</a>
  </div>
  <div class="footer-col">
    <h4>Company</h4>
    <a href="/about-us/">About Us</a>
    <a href="/privacy/">Privacy</a>
    <a href="/contact-us/">Contact Us</a>
    <a href="/terms/">Terms</a>
  </div>
</div>
<div class="footer-bottom">
  <span>&copy; 2026 Bigloong. All rights reserved.</span>
  <span>Questions? Email us at <a href="mailto:{EMAIL}">{EMAIL}</a>.</span>
</div>
</div></footer>
<script src="/assets/js/main.js"></script>
</body>
</html>'''

def page(title, description, body, active="", crumbs=None, jsonld="", keywords="", canonical="/"):
    crumb_html = breadcrumb(crumbs) if crumbs else ""
    return (head(title, description, jsonld, keywords, canonical)
            + header(active) + crumb_html + body + footer())

def ld_breadcrumb(crumbs):
    items = []
    for i, (label, url) in enumerate(crumbs):
        items.append({
            "@type": "ListItem",
            "position": i + 1,
            "name": label,
            "item": "https://" + SITE + (url if url else "/")
        })
    obj = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>'

def write(relpath, content):
    path = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", relpath)

def post_card(p):
    return f'''<article class="post-card">
  <div class="post-thumb" style="--c1:{p['c1']};--c2:{p['c2']}">
    <span class="cat">{p['cat']}</span>
    <span class="thumb-emoji">{p['emoji']}</span>
  </div>
  <div class="post-body">
    <h3><a href="/blog/{p['slug']}/">{p['title']}</a></h3>
    <p>{p['desc']}</p>
    <div class="post-meta">
      <span class="author">AB</span>
      <span>{AUTHOR}</span>
      <span>&middot;</span>
      <span>{p['read']}</span>
    </div>
    <a class="read-link" href="/blog/{p['slug']}/">Read guide <span class="arrow">&rarr;</span></a>
  </div>
</article>'''

# ---------------------------- pages ----------------------------

def build_home():
    cards = "".join(post_card(p) for p in POSTS[:3])
    faq_preview = "".join(f'''<div class="faq-item">
      <button class="faq-q">{f['q']}<span class="plus">+</span></button>
      <div class="faq-a"><p>{f['a']}</p></div>
    </div>''' for f in FAQS[:3])
    body = f'''<main>
<section class="hero">
  <div class="staff-lines"></div>
  <div class="wrap">
    <span class="hero-badge"><span class="pulse"></span> Piano guides for real players</span>
    <h1>Learn piano with <span class="grad-text">confidence</span></h1>
    <p class="lede">Clear piano guides, honest buying advice and short video tutorials. From your first note to your first song, we help you enjoy the journey.</p>
    <div class="hero-actions">
      <a href="/blog/" class="btn btn-primary">Browse piano guides <span>&rarr;</span></a>
      <a href="/video-tutorial/" class="btn btn-ghost">Watch video tutorials</a>
    </div>
  </div>
</section>

<section class="section section-soft"><div class="wrap">
  <div class="section-head">
    <span class="eyebrow">Start here</span>
    <h2>Find your next step at the piano</h2>
    <p>Whether you are choosing a first keyboard, learning a new song or tuning an acoustic piano, there is a clear guide waiting for you.</p>
  </div>
  <div class="grid grid-3">
    <div class="card"><div class="icon">&#127929;</div><span class="badge-tag">Blog</span><h3>In depth guides</h3><p>Long form piano guides written in plain language, from first notes to choosing the right instrument.</p></div>
    <div class="card"><div class="icon">&#127909;</div><span class="badge-tag">Video</span><h3>Video tutorials</h3><p>Short, focused lessons that show you the posture, the note or the technique without the filler.</p></div>
    <div class="card"><div class="icon">&#10067;</div><span class="badge-tag">FAQ</span><h3>Quick answers</h3><p>Straight answers to the questions every new piano player asks, from tuning to practice time.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head">
    <span class="eyebrow">Latest posts</span>
    <h2>Fresh from the blog</h2>
    <p>New piano guides written by {AUTHOR} and the Bigloong team.</p>
  </div>
  <div class="grid grid-3">{cards}</div>
  <div style="text-align:center;margin-top:38px">
    <a href="/blog/" class="btn btn-ghost">See every guide <span>&rarr;</span></a>
  </div>
</div></section>

<section class="section section-soft"><div class="wrap">
  <div class="split">
    <div class="split-copy">
      <span class="eyebrow">Why Bigloong</span>
      <h2>Built for piano learners</h2>
      <p>We know how frustrating it is to hunt through ten tabs for one clear answer. Bigloong collects piano advice in one calm, readable place.</p>
      <p>Every guide is written with care, checked against real playing experience and updated when needed. No clickbait, no clutter and no unexplained jargon.</p>
      <a href="/about-us/" class="read-link">Learn more about us <span class="arrow">&rarr;</span></a>
    </div>
    <div class="split-visual">
      <div class="visual-box"><div class="glow"></div>
        <div class="mock">
          <div class="mock-line purple w70"></div>
          <div class="mock-line"></div>
          <div class="mock-line w45"></div>
          <div class="mock-line"></div>
          <div class="mock-btn"></div>
        </div>
      </div>
    </div>
  </div>
</div></section>

<section class="section section-soft"><div class="wrap">
  <div class="section-head"><span class="eyebrow">FAQs</span><h2>Quick answers</h2></div>
  <div class="faq-list">{faq_preview}</div>
  <div style="text-align:center;margin-top:32px"><a href="/faq/" class="btn btn-ghost">All frequently asked questions</a></div>
</div></section>

<div class="section"><div class="cta-band">
  <h2>Your next piano lesson starts here</h2>
  <p>Pick a guide, find your answer and get back to the keyboard with confidence.</p>
  <div class="actions">
    <a href="/blog/" class="btn btn-primary">Explore guides</a>
    <a href="/contact-us/" class="btn btn-ghost">Get in touch</a>
  </div>
</div></div>
</main>'''
    write("index.html", page("Bigloong | Piano Guides That Make You Want to Play",
        "Clear piano guides, honest buying advice, video tutorials and FAQs. Learn piano with confidence on Bigloong.",
        body, active="home", keywords="piano guides, learn piano, piano for beginners, piano tutorials, Bigloong"))

def build_blog():
    cards = "".join(post_card(p) for p in POSTS)
    body = f'''<main>
<section class="page-intro"><div class="wrap">
  <span class="eyebrow">The blog</span>
  <h1>Piano guides worth your time</h1>
  <p>Detailed piano guides and honest advice, written by {AUTHOR} and updated as your playing grows.</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="grid grid-3">{cards}</div>
</div></section>
<div class="section"><div class="cta-band">
  <h2>Need a hand with something specific</h2>
  <p>Send us a message and we will point you toward the right guide or make one for you.</p>
  <div class="actions"><a href="/contact-us/" class="btn btn-primary">Contact us</a></div>
</div></div>
</main>'''
    crumbs = [("Home", "/"), ("Blog", None)]
    write("blog/index.html", page("Blog | Bigloong",
        "Browse all piano guides, playing tips and buying advice from Bigloong.", body,
        active="blog", crumbs=crumbs, jsonld=ld_breadcrumb(crumbs), canonical="/blog/"))

def build_article(p):
    slug = p["slug"]
    with open(os.path.join(ROOT, p["body_file"]), encoding="utf-8") as f:
        body_html = f.read()
    toc_html = "".join(f'<a href="#{i}">{t}</a>' for i, t in p["toc"])
    article_ld = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": p["full_h1"], "description": p["desc"],
        "author": {"@type": "Person", "name": AUTHOR},
        "publisher": {"@type": "Organization", "name": "Bigloong"},
        "datePublished": p["date"], "dateModified": p["date"],
        "image": "https://" + SITE + p["image"],
        "mainEntityOfPage": "https://" + SITE + "/blog/" + slug + "/"
    }
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q,
                              "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faqs"]]}
    ld = ('<script type="application/ld+json">' + json.dumps(article_ld, ensure_ascii=False) + '</script>'
          + '<script type="application/ld+json">' + json.dumps(faq_ld, ensure_ascii=False) + '</script>')
    crumbs = [("Home", "/"), ("Blog", "/blog/"), (p["title"], None)]
    crumb_ld = ld_breadcrumb(crumbs)
    ld += crumb_ld
    body = f'''<main>
<section class="section"><div class="wrap">
<div class="article">
  <div class="article-main">
    <span class="eyebrow">{p['cat']}</span>
    <h1>{p['full_h1']}</h1>
    <div class="article-meta">
      <span class="author">AB</span>
      <span>By {AUTHOR}</span>
      <span>&middot;</span>
      <span>{p['read']}</span>
    </div>
    <div class="article-cover" style="background:linear-gradient(145deg,{p['c1']},{p['c2']})">{p['emoji']}</div>
    <div class="prose">{body_html}</div>
  </div>
  <aside class="toc"><div class="toc-box">
    <h4>On this page</h4>
    {toc_html}
  </div></aside>
</div>
</div></section>
<div class="section"><div class="cta-band">
  <h2>Keep learning with Bigloong</h2>
  <p>Browse more step by step piano guides and tutorials.</p>
  <div class="actions"><a href="/blog/" class="btn btn-primary">Back to the blog</a></div>
</div></div>
</main>'''
    canonical = "/blog/" + slug + "/"
    write("blog/%s/index.html" % slug,
          page(p["seo_title"], p["desc"], body, active="blog",
               crumbs=crumbs, jsonld=ld, keywords=p["keywords"], canonical=canonical))

def build_faq_index():
    items = "".join(f'''<div class="faq-item">
      <button class="faq-q">{f['q']}<span class="plus">+</span></button>
      <div class="faq-a"><p>{f['a']}</p></div>
    </div>''' for f in FAQS)
    cards = "".join(f'''<article class="post-card faq-card">
  <div class="post-body">
    <h3><a href="/faq/{f['slug']}/">{f['q']}</a></h3>
    <p>{f['a'][:150]}...</p>
    <a class="read-link" href="/faq/{f['slug']}/">Read answer <span class="arrow">&rarr;</span></a>
  </div>
</article>''' for f in FAQS)
    ld_obj = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": f["q"],
                              "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in FAQS]}
    ld = '<script type="application/ld+json">' + json.dumps(ld_obj, ensure_ascii=False) + '</script>'
    crumbs = [("Home", "/"), ("FAQ", None)]
    ld += ld_breadcrumb(crumbs)
    body = f'''<main>
<section class="page-intro"><div class="wrap">
  <span class="eyebrow">Help centre</span>
  <h1>Frequently asked questions</h1>
  <p>Quick answers about learning piano, buying an instrument and practising well.</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="grid grid-2">{cards}</div>
</div></section>
<section class="section section-soft"><div class="wrap">
  <div class="section-head"><span class="eyebrow">In brief</span><h2>Common questions, answered</h2></div>
  <div class="faq-list">{items}</div>
</div></section>
<div class="section"><div class="cta-band">
  <h2>Still have a question</h2>
  <p>We are happy to help. Reach out and we will get back to you.</p>
  <div class="actions"><a href="/contact-us/" class="btn btn-primary">Contact us</a></div>
</div></div>
</main>'''
    write("faq/index.html", page("FAQ | Bigloong", "Answers to common questions about learning piano, piano prices and practice.",
          body, active="faq", crumbs=crumbs, jsonld=ld, canonical="/faq/"))

def build_faq_detail(f):
    slug = f["slug"]
    related = [x for x in FAQS if x["slug"] != slug][:3]
    related_html = "".join(f'<a class="read-link" href="/faq/{r["slug"]}/">{r["q"]} <span class="arrow">&rarr;</span></a>' for r in related)
    ld_obj = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": f["q"],
                              "acceptedAnswer": {"@type": "Answer", "text": f["a"]}}]}
    crumbs = [("Home", "/"), ("FAQ", "/faq/"), (f["q"], None)]
    ld = '<script type="application/ld+json">' + json.dumps(ld_obj, ensure_ascii=False) + '</script>' + ld_breadcrumb(crumbs)
    body = f'''<main>
<section class="section"><div class="wrap">
<div class="article single-col">
  <div class="article-main">
    <span class="eyebrow">FAQ</span>
    <h1>{f['q']}</h1>
    <div class="article-meta"><span class="author">AB</span><span>By {AUTHOR}</span></div>
    <div class="prose"><p class="article-lead">{f['a']}</p></div>
    <div class="related-box"><h4>Related questions</h4>{related_html}</div>
  </div>
</div>
</div></section>
<div class="section"><div class="cta-band">
  <h2>Have another question</h2>
  <p>Send it our way and we will add an answer.</p>
  <div class="actions"><a href="/contact-us/" class="btn btn-primary">Contact us</a></div>
</div></div>
</main>'''
    canonical = "/faq/" + slug + "/"
    write("faq/%s/index.html" % slug,
          page(f["q"] + " | Bigloong FAQ", f["a"][:160], body, active="faq",
               crumbs=crumbs, jsonld=ld, canonical=canonical))

def build_video_index():
    cards = ""
    for v in VIDEOS:
        cards += f'''<article class="post-card">
  <div class="post-thumb" style="--c1:{v['c1']};--c2:{v['c2']}">
    <span class="cat">Video</span>
    <span class="thumb-emoji">{v['emoji']}</span>
    <span class="dur-badge">{v['duration']}</span>
  </div>
  <div class="post-body">
    <h3><a href="/video-tutorial/{v['slug']}/">{v['title']}</a></h3>
    <p>{v['desc']}</p>
    <div class="post-meta"><span class="author">AB</span><span>{AUTHOR}</span></div>
    <a class="read-link" href="/video-tutorial/{v['slug']}/">Watch tutorial <span class="arrow">&rarr;</span></a>
  </div>
</article>'''
    crumbs = [("Home", "/"), ("Video Tutorial", None)]
    ld = ld_breadcrumb(crumbs)
    body = f'''<main>
<section class="page-intro"><div class="wrap">
  <span class="eyebrow">Watch and learn</span>
  <h1>Piano video tutorials</h1>
  <p>Short, focused lessons that show you exactly what to do at the keyboard, without the filler.</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="grid grid-3">{cards}</div>
</div></section>
<div class="section"><div class="cta-band">
  <h2>Prefer to read</h2>
  <p>Every topic also has a written guide on the blog.</p>
  <div class="actions"><a href="/blog/" class="btn btn-primary">Browse the blog</a></div>
</div></div>
</main>'''
    write("video-tutorial/index.html", page("Video Tutorial | Bigloong", "Short, focused piano video tutorials by Bigloong.",
          body, active="video", crumbs=crumbs, jsonld=ld, canonical="/video-tutorial/"))

def build_video_detail(v):
    slug = v["slug"]
    steps = "".join(f'<li>{s}</li>' for s in v["steps"])
    ld_obj = {"@context": "https://schema.org", "@type": "VideoObject",
              "name": v["title"], "description": v["desc"],
              "uploadDate": "2026-11-19", "duration": "PT6M",
              "thumbnailUrl": "https://" + SITE + "/assets/css/placeholder.jpg"}
    crumbs = [("Home", "/"), ("Video Tutorial", "/video-tutorial/"), (v["title"], None)]
    ld = '<script type="application/ld+json">' + json.dumps(ld_obj, ensure_ascii=False) + '</script>' + ld_breadcrumb(crumbs)
    body = f'''<main>
<section class="section"><div class="wrap">
<div class="article single-col">
  <div class="article-main">
    <span class="eyebrow">Video Tutorial &middot; {v['duration']}</span>
    <h1>{v['title']}</h1>
    <div class="article-meta"><span class="author">AB</span><span>By {AUTHOR}</span></div>
    <div class="video-placeholder" style="background:linear-gradient(145deg,{v['c1']},{v['c2']})">
      <span class="vp-play">&#9654;</span>
      <span class="vp-label">Video tutorial coming soon</span>
    </div>
    <div class="prose">
      <p class="article-lead">{v['desc']}</p>
      <h2 id="steps">What you will learn</h2>
      <ol>{steps}</ol>
      <div class="note"><strong>Tip</strong> Practise one step at a time and only move on when the current one feels easy.</div>
    </div>
  </div>
</div>
</div></section>
<div class="section"><div class="cta-band">
  <h2>More video tutorials</h2>
  <p>Browse the full collection of piano lessons.</p>
  <div class="actions"><a href="/video-tutorial/" class="btn btn-primary">All tutorials</a></div>
</div></div>
</main>'''
    canonical = "/video-tutorial/" + slug + "/"
    write("video-tutorial/%s/index.html" % slug,
          page(v["title"] + " | Bigloong Video Tutorial", v["desc"], body, active="video",
               crumbs=crumbs, jsonld=ld, canonical=canonical))

def build_simple(rel, title, intro, sections, active="more", canonical=None, dirname=None):
    body_sections = ""
    for h, paras in sections:
        body_sections += f"<h2>{h}</h2>" + "".join(f"<p>{x}</p>" for x in paras)
    body = f'''<main>
<section class="page-intro"><div class="wrap">
  <span class="eyebrow">Bigloong</span>
  <h1>{title}</h1>
  <p>{intro}</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="prose prose-page">{body_sections}</div>
</div></section>
</main>'''
    label = title
    crumbs = [("Home", "/"), (label, None)]
    out_dir = dirname if dirname else rel
    can = canonical if canonical else "/" + rel + "/"
    write(out_dir + "/index.html", page(title + " | Bigloong", intro, body, active=active,
          crumbs=crumbs, jsonld=ld_breadcrumb(crumbs), canonical=can))

def build_about():
    title = "About Us"
    intro = "Bigloong is a small independent site for people who love the piano."
    sections = [
        ("Our story", ["Bigloong started with a simple idea. Finding a clear piano guide should not take longer than learning the piece itself. What began as notes for friends grew into a collection of practical guides."]),
        ("What we publish", ["We write in depth guides, short video tutorials and quick answers that help you learn and buy with confidence. Every piece is checked against real playing experience and updated when needed."]),
        ("Who writes here", ["Guides are written by " + AUTHOR + " with care for accuracy and readability. We explain our reasoning so you can apply it to your own playing."]),
        ("Get in touch", ["Questions, suggestions or a topic you would like us to cover. Email us at " + EMAIL + " and we will get back to you as soon as we can."]),
    ]
    build_simple("about-us", title, intro, sections, canonical="/about-us/", dirname="about")

def build_privacy():
    title = "Privacy Policy"
    intro = "How Bigloong handles the small amount of information involved in using this site."
    sections = [
        ("Information we collect", ["Bigloong does not require an account and does not ask for personal details to read guides or watch tutorials. If you contact us by email, we receive the message you choose to send."]),
        ("Cookies and analytics", ["We use basic analytics to understand which guides are helpful. This data is aggregated and does not identify you personally."]),
        ("Email and forms", ["If you write to us, your message is handled only to reply to your question. We do not sell or share your email address."]),
        ("Your choices", ["You can browse the entire site without sharing information. For any question about your data, contact us at " + EMAIL + " and we will help."]),
    ]
    build_simple("privacy", title, intro, sections)

def build_terms():
    title = "Terms of Use"
    intro = "The simple rules for using Bigloong guides, videos and content."
    sections = [
        ("Using our content", ["Guides and tutorials on Bigloong are free for personal use. You may share links freely and quote short passages with credit to Bigloong."]),
        ("Republishing", ["Please ask before republishing full guides elsewhere. We are usually happy to help but want to know where our work appears. Write to " + EMAIL + "."]),
        ("Accuracy", ["We aim for accurate guides but instruments and methods vary. If you spot an error, let us know and we will correct it."]),
        ("Liability", ["Bigloong is provided as is. We are not responsible for decisions made using our guides or advice."]),
    ]
    build_simple("terms", title, intro, sections)

def build_contact():
    body = f'''<main>
<section class="page-intro"><div class="wrap">
  <span class="eyebrow">Say hello</span>
  <h1>Contact us</h1>
  <p>Questions, ideas or a guide request. We would love to hear from you.</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="contact-grid">
    <div class="contact-info">
      <span class="eyebrow">Get in touch</span>
      <h2>We are here to help</h2>
      <p style="margin-bottom:30px">Whether you are choosing a piano or want to suggest a topic, send a message and we will get back to you as soon as we can.</p>
      <div class="info-item"><div class="info-ico">&#9993;</div><div><h4>Email</h4><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div></div>
      <div class="info-item"><div class="info-ico">&#128218;</div><div><h4>Guide requests</h4><p>Tell us the topic and what you need help with.</p></div></div>
      <div class="info-item"><div class="info-ico">&#128337;</div><div><h4>Response time</h4><p>Usually within two working days.</p></div></div>
    </div>
    <form class="form-card" id="contactForm">
      <div class="field"><label for="name">Your name</label><input id="name" name="name" type="text" placeholder="Jane Doe" required></div>
      <div class="field"><label for="email">Email address</label><input id="email" name="email" type="email" placeholder="jane@example.com" required></div>
      <div class="field"><label for="subject">Subject</label><input id="subject" name="subject" type="text" placeholder="Guide request"></div>
      <div class="field"><label for="message">Message</label><textarea id="message" name="message" placeholder="How can we help?" required></textarea></div>
      <button type="submit" class="btn btn-primary" style="width:100%">Send message <span>&rarr;</span></button>
      <p style="font-size:.78rem;margin-top:14px;text-align:center">You can also email us directly at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    </form>
  </div>
</div></section>
</main>'''
    crumbs = [("Home", "/"), ("Contact Us", None)]
    write("contact/index.html", page("Contact Us | Bigloong", "Get in touch with Bigloong for guide requests, questions and feedback.",
          body, crumbs=crumbs, jsonld=ld_breadcrumb(crumbs), canonical="/contact-us/"))

def build_404():
    body = '''<main>
<section class="hero"><div class="staff-lines"></div><div class="wrap">
  <span class="eyebrow">404</span>
  <h1>That page went <span class="grad-text">missing</span></h1>
  <p class="lede">The guide you are looking for may have moved. Try the blog or head back home.</p>
  <div class="hero-actions">
    <a href="/" class="btn btn-primary">Go home</a>
    <a href="/blog/" class="btn btn-ghost">Browse guides</a>
  </div>
</div></section>
</main>'''
    write("404.html", page("Page not found | Bigloong", "The page you requested could not be found.", body))

def build_sitemap():
    urls = ["/", "/blog/", "/faq/", "/video-tutorial/", "/about-us/", "/privacy/", "/contact-us/", "/terms/"]
    urls += ["/blog/%s/" % p["slug"] for p in POSTS]
    urls += ["/faq/%s/" % f["slug"] for f in FAQS]
    urls += ["/video-tutorial/%s/" % v["slug"] for v in VIDEOS]
    entries = "".join(f"  <url><loc>https://{SITE}{u}</loc></url>\n" for u in urls)
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}</urlset>
'''
    write("sitemap.xml", xml)
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: https://{SITE}/sitemap.xml\n")
    # Cloudflare Pages rewrite: keep clean public URLs while files live in short dirs
    write("_redirects", "/about-us/  /about/index.html  200\n/contact-us/  /contact/index.html  200\n")

def build_aliases():
    """Mirror about/ and contact/ into public URL dirs so clean URLs work on any
    static host, not only Cloudflare Pages (whose _redirects is not universal).
    Canonical tags already point at /about-us/ and /contact-us/ so no duplicate
    content issue. The _redirects rules are kept as a bonus for Pages hosts."""
    for src, dst in (("about/index.html", "about-us/index.html"),
                     ("contact/index.html", "contact-us/index.html")):
        sp = os.path.join(ROOT, src)
        if os.path.exists(sp):
            with open(sp, "r", encoding="utf-8") as f:
                write(dst, f.read())

def main():
    build_home()
    build_blog()
    for p in POSTS:
        build_article(p)
    build_faq_index()
    for f in FAQS:
        build_faq_detail(f)
    build_video_index()
    for v in VIDEOS:
        build_video_detail(v)
    build_about()
    build_privacy()
    build_terms()
    build_contact()
    build_404()
    build_sitemap()
    build_aliases()
    print("DONE")

if __name__ == "__main__":
    main()
