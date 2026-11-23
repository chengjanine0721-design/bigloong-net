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
import hashlib

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "bigloong.net"
AUTHOR = "Alice Baker"
EMAIL = "contact@bigloong.net"

def _asset_ver(rel):
    """基于静态文件内容 md5 的版本号，作为 cache-busting 查询参数，避免浏览器/CDN 缓存旧样式。"""
    p = os.path.join(ROOT, rel.lstrip("/"))
    try:
        with open(p, "rb") as fh:
            return hashlib.md5(fh.read()).hexdigest()[:8]
    except OSError:
        return "0"

CSS_VER = _asset_ver("assets/css/style.css")
JS_VER = _asset_ver("assets/js/main.js")

def img_ver(url):
    """给图片 URL 加基于文件内容的 md5 版本号，换图后 URL 随之改变，彻底绕过浏览器/CDN 缓存。"""
    if not url:
        return url
    site_prefix = "https://" + SITE
    if url.startswith(site_prefix) and url[len(site_prefix):].startswith("/assets/"):
        path = url[len(site_prefix):]
        return site_prefix + path + "?v=" + _asset_ver(path)
    if url.startswith("/assets/"):
        return url + "?v=" + _asset_ver(url)
    return url

# ---------------------------- data ----------------------------

POSTS = [
    {
        "slug": "how-to-tune-a-piano-yourself-basic-guide",
        "cat": "Beginner Guide",
        "title": "How to Tune a Piano Yourself: A Basic Guide",
        "desc": "Learn how to tune a piano yourself with a basic guide to the tools, the note order and the simple steps that keep your piano in tune between professional visits.",
        "emoji": "\U0001F3B9",
        "c1": "#FFF0C9", "c2": "#E7E5F6",
        "date": "2026-11-21",
        "read": "9 min read",
        "seo_title": "How to Tune a Piano Yourself: A Basic DIY Guide",
        "full_h1": "How to Tune a Piano Yourself (A Basic DIY Guide)",
        "body_file": "_tune_piano_body.html",
        "image": "/assets/img/how-to-tune-a-piano-yourself-basic-guide/cover.jpg",
        "cover_img": "/assets/img/how-to-tune-a-piano-yourself-basic-guide/cover.jpg",
        "keywords": "how to tune a piano yourself basic guide, how to tune a piano, piano tuning DIY, tune piano at home, piano tuning tools",
        "toc": [
            ("what-tuning-does", "What Tuning Does"),
            ("tools", "The Tools You Need"),
            ("before-you-start", "Before You Start"),
            ("order-of-work", "The Order of Work"),
            ("finding-notes", "Finding the Notes"),
            ("common-mistakes", "Common Mistakes"),
            ("how-often", "How Often to Tune"),
            ("faq", "FAQ"),
            ("conclusion", "Start Slow and Listen"),
        ],
        "faqs": [
            ("Can a beginner really tune a piano at home", "Yes, for a piano that is already close to pitch and has no structural problems. With a basic kit, a chromatic tuner and a careful approach, a beginner can handle routine drift. Save major pitch raises, broken strings and new instruments for a qualified technician."),
            ("How long does it take to tune a piano yourself", "A first full tuning usually takes two to four hours because you are learning the layout and moving slowly. With practice, an experienced amateur can finish a stable piano in about an hour. Rushing is the main cause of mistakes."),
            ("Will tuning my piano myself damage it", "Not if you use the correct lever, raise pitch gently and leave large changes to a professional. The real risks are rounded pins from the wrong tool and broken strings from over-tightening, both of which are avoidable with patience."),
        ],
    },
    {
        "slug": "music-theory-basics-for-piano",
        "cat": "Beginner Guide",
        "title": "Music Theory Basics for Piano",
        "desc": "Learn music theory basics for piano: the notes, scales, intervals, chords and rhythm that make every song easier to understand and play, even if you are teaching yourself at home.",
        "emoji": "\U0001F3B9",
        "c1": "#E7E5F6", "c2": "#FFF0C9",
        "date": "2026-11-21",
        "read": "11 min read",
        "seo_title": "Music Theory Basics for Piano: A Beginner Guide",
        "full_h1": "Music Theory Basics for Piano (A Beginner Friendly Guide)",
        "body_file": "_music_theory_body.html",
        "image": "/assets/img/music-theory-basics-for-piano/cover.jpg",
        "cover_img": "/assets/img/music-theory-basics-for-piano/cover.jpg",
        "keywords": "learning piano by yourself, adult beginner piano, best way to learn piano as an adult, how to learn piano adults, piano lessons beginner adult, music theory basics for piano",
        "toc": [
            ("why-theory", "Why Theory Helps"),
            ("alphabet", "The Musical Alphabet"),
            ("rhythm", "Note Values and Rhythm"),
            ("scales", "Major and Minor Scales"),
            ("intervals", "Intervals"),
            ("chords", "Chords"),
            ("reading", "Reading Music Without Fear"),
            ("practice", "How to Practise Theory"),
            ("faq", "FAQ"),
            ("conclusion", "Theory Is a Tool"),
        ],
        "faqs": [
            ("Do I need theory to play the piano", "No, you can start playing by ear or from chord charts straight away. But theory makes later learning much faster and helps you understand what you are doing. A little knowledge early on saves a lot of guesswork."),
            ("Is it harder to learn piano as an adult", "Adults sometimes find fingering and rhythm slower to settle, but they usually understand theory and practice habits faster than children. With realistic goals and short daily sessions, adult beginners often make swift, steady progress."),
            ("What theory should a complete beginner learn first", "Start with the musical alphabet, the layout of white and black keys, note values, the C major scale and three basic chords. Those few ideas unlock a large amount of beginner music."),
        ],
    },
    {
        "slug": "piano-finger-exercises-for-beginners",
        "cat": "Beginner Guide",
        "title": "Piano Exercises for Beginners",
        "desc": "Build control with simple piano exercises for beginners. Learn finger drills, five-finger patterns, slow scales and a short daily routine that actually sticks.",
        "emoji": "\U0001F3B9",
        "c1": "#FFF0C9", "c2": "#E7E5F6",
        "date": "2026-11-22",
        "read": "10 min read",
        "seo_title": "Piano Exercises for Beginners: Simple Daily Drills That Work",
        "full_h1": "Piano Exercises for Beginners (Simple Daily Drills That Work)",
        "body_file": "_piano_exercises_body.html",
        "image": "/assets/img/piano-finger-exercises-for-beginners/cover.jpg",
        "cover_img": "/assets/img/piano-finger-exercises-for-beginners/cover.jpg",
        "keywords": "piano exercises for beginners, piano practice for beginners, piano exercise, piano drills for beginners",
        "toc": [
            ("why-exercises", "Why Exercises Matter"),
            ("before-you-start", "Posture and Hand Shape"),
            ("warm-up", "The Warm-Up"),
            ("five-finger-patterns", "Five-Finger Patterns"),
            ("scales", "Slow Scales"),
            ("finger-independence", "Finger Independence"),
            ("hands-together", "Hands Together"),
            ("rhythm", "Rhythm Variations"),
            ("routine", "A Daily Routine"),
            ("mistakes", "Common Mistakes"),
            ("faq", "FAQ"),
            ("conclusion", "Start Small"),
        ],
        "faqs": [
            ("How long should a beginner practise piano each day", "Ten to twenty minutes of focused daily practice is a great start. Short, regular piano exercises for beginners build technique faster than one long session a week, because the brain consolidates the movement between sessions."),
            ("Do I need a teacher to do these exercises correctly", "No, these drills are safe to do on your own if you stay relaxed and stop when you feel strain. A teacher is still valuable for catching small posture issues early, but a careful self-taught player can make steady progress with them."),
            ("How soon will I see results from finger exercises", "Most beginners notice smoother, more even fingers within two to three weeks of short daily practice. Stronger independence in the weak fingers takes a little longer, so be patient and keep the sessions consistent."),
        ],
    },
    {
        "slug": "how-to-play-chords-on-piano",
        "cat": "Beginner Guide",
        "title": "How to Play Chords on Piano",
        "desc": "Build fuller chords and smoother changes from day one. Learn major and minor triads, fingering, a simple piano chords chart and easy progressions.",
        "emoji": "\U0001F3B9",
        "c1": "#FFF0C9", "c2": "#E7E5F6",
        "date": "2026-11-20",
        "read": "11 min read",
        "seo_title": "How to Play Chords on Piano: Beginner Chord Guide & Chart",
        "full_h1": "How to Play Chords on Piano (Beginner Chord Guide & Chart)",
        "body_file": "_chords_body.html",
        "image": "/assets/img/how-to-play-chords-on-piano/cover.jpg",
        "cover_img": "/assets/img/how-to-play-chords-on-piano/cover.jpg",
        "keywords": "how to play chords on piano, how to play piano chords, playing chords on piano, how to play a chord on piano, piano music chords for beginners, piano chords chart, piano chord, piano chord structure, understanding piano chords, chords on piano, chords piano tutorial, study piano chords",
        "toc": [
            ("what-is-a-chord", "What Is a Piano Chord?"),
            ("triads", "Major and Minor Triads"),
            ("chord-chart", "A Simple Chords Chart"),
            ("fingerings", "Smooth Fingerings"),
            ("chord-structure", "Chord Structure"),
            ("progressions", "Simple Progressions"),
            ("chord-changes", "Smooth Chord Changes"),
            ("tutorial", "Step by Step Tutorial"),
            ("faq", "FAQ"),
            ("conclusion", "Start Today"),
        ],
        "faqs": [
            ("What is the easiest chord to start with on piano", "C major is the best first chord. It uses only white keys and fits comfortably under fingers 1 3 5, so you can focus on tone and relaxation rather than awkward positions. From there, A minor and G major are natural next steps."),
            ("How long does it take to play chords smoothly", "Most players can hold a few basic chords within a first week and move between them smoothly after two to four weeks of short daily practice. Consistency matters more than session length."),
            ("Do I need to read music to play chords", "No. Chord charts name the notes or shapes directly, so you can start playing immediately. Reading music is still worth adding later because it opens up far more songs."),
        ],
    },
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
        "image": "/assets/img/how-much-does-a-piano-cost/cover.jpg",
        "cover_img": "/assets/img/how-much-does-a-piano-cost/cover.jpg",
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
        "image": "/assets/img/how-to-start-learning-piano/cover.jpg",
        "cover_img": "/assets/img/how-to-start-learning-piano/cover.jpg",
        "keywords": "how to start learning piano, learn piano by yourself, piano for beginners, piano tips",
        "toc": [
            ("instrument", "1. Get the Right Instrument"),
            ("hand-position", "Hand and Finger Positioning"),
            ("know-keys", "2. Know the Piano and Keys"),
            ("beginner-songs", "3. Play Beginner Songs"),
            ("how-to-learn", "4. Choose How You Learn"),
            ("finger-exercises", "5. Daily Finger Exercises"),
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
    {
        "slug": "how-to-improve-piano-finger-speed-and-dexterity",
        "cat": "Technique",
        "title": "How to Improve Piano Finger Speed and Dexterity",
        "desc": "Relaxed hands, clean technique and a few focused exercises are all it takes to build fast, even fingers. Learn how to improve piano finger speed and dexterity step by step.",
        "emoji": "\U0001F599",
        "c1": "#FFF0C9", "c2": "#E7E5F6",
        "date": "2026-11-19",
        "read": "9 min read",
        "seo_title": "How to Improve Piano Finger Speed and Dexterity: Exercises That Work",
        "full_h1": "How to Improve Piano Finger Speed and Dexterity (Step by Step)",
        "body_file": "_finger_speed_body.html",
        "image": "/assets/img/how-to-improve-piano-finger-speed-and-dexterity/cover.jpg",
        "cover_img": "/assets/img/how-to-improve-piano-finger-speed-and-dexterity/cover.jpg",
        "keywords": "how to improve piano finger speed and dexterity, finger dexterity exercises piano, play piano faster, piano finger speed test, improve finger speed at home",
        "toc": [
            ("what-is-dexterity", "Speed vs Dexterity"),
            ("relax-first", "Start Relaxed"),
            ("warm-up", "Warm-Up Exercises"),
            ("speed-exercises", "Exercises for Speed"),
            ("at-home-routine", "A Routine at Home"),
            ("measure-progress", "Measure Your Progress"),
            ("common-mistakes", "Common Mistakes"),
            ("faq", "FAQ"),
            ("conclusion", "Conclusion"),
        ],
        "faqs": [
            ("Can adults still build fast fingers", "Yes. Adult learners often progress quickly because they understand the value of slow, deliberate practice. Finger speed is a trained skill, not a talent reserved for children."),
            ("How long does it take to get faster", "Most players notice smoother runs within two to three weeks of short daily practice. Meaningful gains in top speed usually take a few months of consistent work."),
            ("Should I use finger exercises or real music", "Both. Exercises isolate the movement, while real music teaches you to use it. Spend part of each session on technique and the rest on a piece you enjoy."),
        ],
    },
    {
        "slug": "how-to-read-sheet-music-piano",
        "cat": "Beginner Guide",
        "title": "How to Read Sheet Music for Piano",
        "desc": "Learn to read piano sheet music from scratch: the staff, both clefs, note values and a simple method for a new piece. No teacher required.",
        "emoji": "\U0001F3B4",
        "c1": "#E7E5F6", "c2": "#FFF0C9",
        "date": "2026-11-19",
        "read": "11 min read",
        "seo_title": "How to Read Sheet Music for Piano: A Beginner's Guide",
        "full_h1": "How to Read Sheet Music for Piano: A Beginner's Guide",
        "body_file": "_read_sheet_music_body.html",
        "image": "/assets/img/how-to-read-sheet-music-piano/cover.jpg",
        "cover_img": "/assets/img/how-to-read-sheet-music-piano/cover.jpg",
        "keywords": "how to read sheet music piano, how to read piano sheet music for beginners, learn to read piano sheet, how to learn sheet music, learn piano notes",
        "toc": [
            ("the-staff", "The Staff"),
            ("note-values", "Note Values"),
            ("sharps-flats", "Sharps and Flats"),
            ("read-notes", "Reading Notes on the Keyboard"),
            ("a-step-by-step-method", "A Step by Step Method"),
            ("practice-tips", "Tips for Beginners"),
            ("faq", "FAQ"),
            ("conclusion", "Start Reading Today"),
        ],
        "faqs": [
            ("Do I need to read music to play piano", "No, you can learn songs by ear or by following chord charts. But reading opens up far more music and makes learning new pieces much faster, so it is worth adding alongside whatever method you use."),
            ("Which clef should I learn first", "Most beginners start with the treble clef because it carries the melody. Add the bass clef once the treble notes are comfortable. Reading both together comes with practice."),
            ("How long does it take to read sheet music", "You can recognise the basic notes in a couple of weeks of short daily practice. Becoming a fluent, sight reading pianist takes months or years, but the early gains come quickly."),
        ],
    },
    {
        "slug": "do-you-need-88-keys-on-a-piano",
        "cat": "Buying Guide",
        "title": "Do You Need 88 Keys on a Piano?",
        "desc": "A practical guide to keyboard size, from 61 keys to a full 88-key instrument, and which one fits your goals, space and budget as a piano learner.",
        "emoji": "\U0001F3B9",
        "c1": "#FFF0C9", "c2": "#E7E5F6",
        "date": "2026-11-23",
        "read": "9 min read",
        "seo_title": "Do You Need 88 Keys on a Piano? 61 vs 76 vs 88 Explained",
        "full_h1": "Do You Need 88 Keys on a Piano? (61 vs 76 vs 88 Keys)",
        "body_file": "_do_you_need_88_body.html",
        "image": "/assets/img/do-you-need-88-keys-on-a-piano/cover.jpg",
        "cover_img": "/assets/img/do-you-need-88-keys-on-a-piano/cover.jpg",
        "keywords": "do you need 88 keys on a piano, do i need 88 keys, 88 keys vs 61 keys, is 61 keys enough, piano keyboard size guide, how many keys do i need",
        "toc": [
            ("what-88-keys-means", "What 88 Keys Give You"),
            ("keyboard-sizes", "61, 76 and 88 Keys Compared"),
            ("weighted-keys", "Weight and Key Action"),
            ("who-needs-88", "Who Should Choose 88 Keys"),
            ("who-can-wait", "Who Can Wait"),
            ("faq", "FAQ"),
            ("conclusion", "The Bottom Line"),
        ],
        "faqs": [
            ("Is 61 keys enough to learn piano", "Yes. For the first one to two years, 61 keys cover beginner pieces, scales, chords and most popular songs. Upgrade to 88 keys only when the music you want to play needs notes outside that range."),
            ("Is an 88 key piano better for beginners", "It is not automatically better, but it is more complete. The extra range and weighted action prepare you for any style of music and avoid an upgrade later. Choose it if your budget and space allow."),
            ("Can I get 88 keys in a portable keyboard", "Yes. Many stage pianos and folding keyboards offer a full 88 key weighted action in a portable package, giving you the full range without needing a permanent space."),
        ],
    },
    {
        "slug": "how-much-do-piano-lessons-cost",
        "cat": "Buying Guide",
        "title": "How Much Do Piano Lessons Cost?",
        "desc": "Understand private and group lesson rates, package deals, and what you really get for your money when budgeting for piano lessons.",
        "emoji": "\U0001F3B9",
        "c1": "#FFF0C9", "c2": "#E7E5F6",
        "date": "2026-11-23",
        "read": "11 min read",
        "seo_title": "How Much Do Piano Lessons Cost? 2026 Rates & Price Guide",
        "full_h1": "How Much Do Piano Lessons Cost? (2026 Price Guide)",
        "body_file": "_piano_lessons_cost_body.html",
        "image": "/assets/img/how-much-do-piano-lessons-cost/cover.jpg",
        "cover_img": "/assets/img/how-much-do-piano-lessons-cost/cover.jpg",
        "keywords": "how much are piano lessons, how much do piano lessons cost, average cost of piano lessons, piano lesson rates, piano private lessons rates, how much are piano lessons for kids, fees for piano lessons, piano classes cost",
        "toc": [
            ("average-cost", "Average Lesson Cost"),
            ("what-affects-rates", "What Affects Rates"),
            ("kids-lessons", "Lessons for Kids"),
            ("private-rates", "Private vs Group"),
            ("hidden-costs", "Hidden Costs"),
            ("save-money", "How to Save"),
            ("faq", "FAQ"),
            ("conclusion", "The Bottom Line"),
        ],
        "faqs": [
            ("What is the average cost of piano lessons", "In the United States the average is about $50 for a 30 minute private lesson, with most teachers charging between $30 and $80. Group classes average $15 to $35 per person."),
            ("How much does it cost for piano lessons for a full year", "A weekly 30 minute private lesson at $50 per session comes to roughly $1,500 to $1,800 for a 36 week year. Group lessons can reduce that to $600 to $1,200."),
            ("Are piano lessons worth the cost", "For most learners, yes. A good teacher corrects technique early, prevents bad habits and keeps you motivated, which speeds progress and reduces frustration."),
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

# Rich FAQ articles (Q&A structure + Article/FAQPage/BreadcrumbList schema)
FAQ_ARTICLES = [
    {
        "slug": "is-piano-a-string-instrument",
        "title": "Is the Piano a String Instrument?",
        "desc": "Is the piano a string or percussion instrument? Learn how a piano makes sound, which family it belongs to and why both labels are technically correct.",
        "full_h1": "Is the Piano a String Instrument? (String, Percussion or Both?)",
        "seo_title": "Is the Piano a String Instrument? String or Percussion Explained",
        "body_file": "_is_piano_string_body.html",
        "keywords": "is piano a string instrument, is piano a percussion or string instrument, is piano a stringed instrument, what family of instruments does the piano belong to",
        "date": "2026-11-22",
        "read": "7 min read",
        "toc": [
            ("short-answer", "A String Instrument?"),
            ("how-it-works", "How It Makes Sound"),
            ("percussion", "Percussion or String?"),
            ("family", "Which Family?"),
            ("digital", "Digital Pianos"),
            ("faq", "FAQ"),
            ("conclusion", "Bottom Line"),
        ],
        "faqs": [
            ("Is the piano a percussion instrument", "Partly. A felt hammer strikes the strings, so the piano produces sound by percussion. That is why it is sometimes grouped with percussion instruments. But because the vibrating source is a string, most formal classifications still call it a string instrument overall."),
            ("Why is the piano in the string section of an orchestra", "Because its notes come from vibrating strings, the same as violins and cellos. In orchestral writing the piano is treated as a string-toned instrument and is often listed in the string section, even though it is played from a keyboard."),
            ("Is a piano a stringed instrument like a guitar", "It is a stringed instrument in the sense that strings create the sound, but it is not played like a guitar. Guitar strings are plucked with the fingers or a pick, while piano strings are struck by hammers controlled from a keyboard. Both belong to the string family."),
        ],
    },
    {
        "slug": "how-many-keys-on-a-piano",
        "title": "How Many Keys Are on a Piano?",
        "desc": "A full piano has 88 keys: 52 white and 36 black. Learn how many keys, notes and octaves a piano has, why 88 became standard and whether you need all of them.",
        "full_h1": "How Many Keys Are on a Piano? (Notes, Octaves & 88-Key Guide)",
        "seo_title": "How Many Keys Are on a Piano? 88 Keys, Notes & Octaves Explained",
        "body_file": "_many_keys_body.html",
        "keywords": "how many keys on a piano, how many notes on a piano, how many octaves are in a piano, 88 piano keys, how many notes on piano, numbers of piano keys",
        "date": "2026-11-20",
        "read": "8 min read",
        "toc": [
            ("keys-and-notes", "Keys and Notes"),
            ("octaves", "How Many Octaves"),
            ("why-88", "Why 88 Became Standard"),
            ("do-you-need-88", "Do You Need 88 Keys?"),
            ("faq", "FAQ"),
            ("conclusion", "Bottom Line"),
        ],
        "faqs": [
            ("How many keys on a piano are white and how many are black", "A standard piano has 52 white keys and 36 black keys, making 88 in total. The black keys sit in repeating groups of two and three, which is what lets you find any note by touch and sight."),
            ("How many notes on a piano can you play at once", "Technically you can press several keys together, and a full chord uses three or more. In practice, hands can comfortably hold around ten notes at once, though most music uses far fewer."),
            ("Is 61 keys enough to learn piano", "Yes, for the first year or two. A 61-key keyboard covers five octaves and handles beginner pieces, chords and most popular songs. Move to 88 keys when your repertoire needs the extreme low or high notes."),
        ],
    },
]

VIDEOS = [
    {
        "slug": "piano-posture-for-beginners",
        "title": "Piano Posture for Beginners",
        "desc": "Sit tall, relax your shoulders and find the right bench height. Good posture prevents tension and makes every note easier to play.",
        "cover_img": "/assets/img/videos/posture-cover.jpg",
        "duration": "6:12",
        "emoji": "\U0001F9D8",
        "c1": "#FFF0C9", "c2": "#E7E5F6",
        "steps": [
            "Place the bench so your forearms are level with the keyboard when your fingers rest on the keys.",
            "Sit on the front half of the bench with feet flat on the floor and a straight but relaxed back.",
            "Keep elbows slightly away from your body and let your shoulders drop.",
            "Curve your fingers naturally and play from the weight of your arm rather than finger force alone.",
        ],
        "embeds": [
            {"id": "MoiMo6S9CE8", "label": "Sit Position"},
            {"id": "ROM9szRJHpg", "label": "Hand Position"},
            {"id": "eq1-8RWO8S4", "label": "Incorrect Posture"},
            {"id": "EItL4YrvASA", "label": "Correct Posture"},
        ],
    },
    {
        "slug": "finding-middle-c-on-piano",
        "title": "Finding Middle C on a Piano",
        "desc": "Middle C is your home base on the keyboard. Learn two quick ways to find it every time you sit down to play.",
        "cover_img": "/assets/img/videos/middle-c-cover.jpg",
        "duration": "4:35",
        "emoji": "\U0001F3B9",
        "c1": "#E7E5F6", "c2": "#FFF0C9",
        "steps": [
            "Look for the group of two black keys near the centre of the keyboard.",
            "The white key immediately to the left of that pair is middle C.",
            "On a full 88 key piano, middle C is also the fourth C counted up from the lowest note.",
            "Mark it once with a removable sticker if you are new, then remove it as your reading improves.",
        ],
        "copy_first": True,
        "embeds": [
            {"id": "tbslYrPGzQA", "label": "Find Middle C Fast",
             "desc": "Spot middle C the moment you sit down — no counting, no guessing.", "ratio": "9/16"},
            {"id": "W6LnO6m-mss", "label": "Middle C in Seconds",
             "desc": "Another quick visual trick to locate middle C on any keyboard.", "ratio": "9/16"},
            {"id": "ZCIEcgRnMZc", "label": "Keys & Every C Explained",
             "desc": "A complete walkthrough of the keys: where middle C sits, how notes repeat, and how to find every C on a full-size, 36, 49 or 61-key keyboard.", "ratio": "16/9"},
        ],
    },
    {
        "slug": "first-piano-song-tutorial",
        "title": "Your First Piano Song Tutorial",
        "desc": "Put a few notes together in a simple melody you can play in your first week. Slow, even practice is the whole secret.",
        "cover_img": "/assets/img/videos/first-song-cover.jpg",
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
        "cover_img": "/assets/img/videos/scales-cover.jpg",
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
    {
        "slug": "how-to-play-twinkle-twinkle-little-star-on-the-piano",
        "title": "How to Play Twinkle Twinkle Little Star on the Piano",
        "desc": "A clear lesson on how to play Twinkle Twinkle Little Star on the piano. Learn the simple right hand melody by ear and note, then add an easy left hand accompaniment.",
        "cover_img": "/assets/img/videos/twinkle-cover.jpg",
        "duration": "8:05",
        "emoji": "\U0001F31F",
        "c1": "#FFF0C9", "c2": "#E7E5F6",
        "steps": [
            "Find middle C, then locate the notes C C G G A A G using the group of two black keys as your guide.",
            "Play the opening phrase one note at a time and say each note name aloud: C C G G A A G, then hold the G for two beats.",
            "Learn the second phrase F F E E D D C and listen for the way it steps down back to the starting note.",
            "Keep the melody in the right hand with fingers 1 and 5 on the repeated C and G notes, using finger 3 for the A.",
            "Add a simple left hand by playing a low C on the first beat of each bar, then try alternating low C and G for a fuller sound.",
            "Put both hands together slowly with a metronome, and only increase the tempo once the notes are even and relaxed.",
        ],
        "intro": "Twinkle Twinkle Little Star is one of the first songs nearly every piano learner meets. It is an easy, beginner-level piece: the melody uses only a few notes, stays in a comfortable range, and repeats a simple pattern, so it suits complete beginners and young children well. Most learners can play the right-hand tune in a single afternoon and put both hands together within a week of short, regular practice. Its slow, familiar tune makes it ideal for building note reading, steady rhythm and confidence at the keyboard before moving on to more demanding pieces.",
        "embeds": [
            {"id": "GgHkBKH1m1Q", "label": "Easy Piano Tutorial",
             "desc": "A slow, note-by-note walkthrough you can play along with.", "ratio": "16/9"},
        ],
        "sheet": {
            "img": "/assets/img/videos/twinkle-sheet.png",
            "note": "Want the full printable score? Download the complete ",
            "anchor": "twinkle twinkle little star piano sheet",
            "url": "https://www.makingmusicfun.net/public/assets/pdf/sheet_music/twinkle-twinkle-little-star-piano-solo.pdf",
        },
    },
    {
        "slug": "how-to-play-happy-birthday-on-piano",
        "title": "How to Play Happy Birthday on Piano",
        "desc": "A simple lesson on how to play Happy Birthday on piano. Learn the melody with one hand first, add easy chords and play it smoothly for any birthday celebration.",
        "duration": "7:40",
        "emoji": "\U0001F389",
        "c1": "#FFF0C9", "c2": "#FBE8F2",
        "steps": [
            "Find middle C just left of the two black keys. The opening of Happy Birthday starts on the F below it, so locate F and place your right thumb there.",
            "Learn the first phrase one note at a time: F F G F, then B flat A. Say the note names aloud as you play so the pattern sticks.",
            "Play the pickup lines slowly: F F G F C B flat A. Keep an even rhythm and do not rush the repeated F notes.",
            "Use fingers 1 1 2 1 4 3 for the opening phrase. Relax the hand between notes and let the thumb stay loose.",
            "Once the melody is comfortable, add a simple left hand chord under the start of each line: B flat major, then F major.",
            "Practise hands together at a slow tempo with a steady count, then increase speed only when the notes and chords feel even.",
        ],
    },
    {
        "slug": "how-to-play-erika-on-piano",
        "title": "How to Play Erika on Piano",
        "desc": "Learn how to play Erika on piano with a simple melody in the right hand, easy left hand chords and a steady march-like rhythm, ideal for beginners.",
        "keywords": "how to play erika on piano, erika piano tutorial, erika piano notes, erika piano easy, learn erika piano",
        "duration": "6:30",
        "emoji": "\U0001F3B9",
        "c1": "#FFF0C9", "c2": "#E7E5F6",
        "steps": [
            "Erika uses a simple three-chord pattern. In G major the main chords are G (G B D), C (C E G) and D (D F sharp A). Find each shape and practise moving between them with your left hand.",
            "Learn the right hand melody in small phrases. The opening notes are C, then D E E E A A, so place your right thumb on C and use fingers 1 2 3 for the stepwise movement.",
            "Break the tune into two bar chunks and repeat each one slowly until the notes feel automatic before joining the next phrase.",
            "Add a simple left hand by playing the root note of each chord on the first beat of the bar: G, C and D. Keep it low and steady under the melody.",
            "Practise the melody and bass hands separately first. Once each is comfortable, put them together at a slow tempo with a metronome.",
            "Keep an even, march-like rhythm and a firm but relaxed touch. Increase the speed only when the notes and chord changes are clean and even.",
        ],
        "embeds": [
            {"id": "pXj-V8W9p1M", "label": "Erika Piano (Easy Version)",
             "desc": "A short, easy-to-follow piano version you can play along with.", "ratio": "9/16"},
        ],
    },
]

# ---------------------------- shared partials ----------------------------

def head(title, description, jsonld="", keywords="", canonical="/", og_image=""):
    kw = ('<meta name="keywords" content="%s">' % keywords) if keywords else ""
    ogimg = ('<meta property="og:image" content="%s">' % img_ver("https://" + SITE + og_image)) if og_image else ""
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
{ogimg}<link rel="canonical" href="https://{SITE}{canonical}">
<link rel="icon" type="image/png" href="/assets/img/favicon.png">
<link rel="shortcut icon" href="/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&family=Poppins:wght@500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css?v={CSS_VER}">
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
  <a href="https://bigloong.net" class="brand"><img class="brand-mark" src="/assets/img/favicon.png" alt="Bigloong">bigloong</a>
  <button class="menu-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
  <ul class="nav-links">
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
    <a href="https://bigloong.net" class="brand"><img class="brand-mark" src="/assets/img/favicon.png" alt="Bigloong">bigloong</a>
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
<script src="/assets/js/main.js?v={JS_VER}"></script>
</body>
</html>'''

def page(title, description, body, active="", crumbs=None, jsonld="", keywords="", canonical="/", og_image=""):
    crumb_html = breadcrumb(crumbs) if crumbs else ""
    return (head(title, description, jsonld, keywords, canonical, og_image)
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

_MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def fmt_date(iso):
    """2026-11-22 -> Nov 22, 2026"""
    y, m, d = iso.split("-")
    return f"{_MONTHS[int(m) - 1]} {int(d)}, {y}"


def post_card(p, show_date=False):
    cover = p.get("cover_img")
    if cover:
        thumb = (f'<div class="post-thumb post-thumb-cover">'
                 f'<img src="{img_ver(cover)}" alt="{p["title"]}" loading="lazy">'
                 f'<span class="cat">{p["cat"]}</span></div>')
    else:
        thumb = (f'<div class="post-thumb" style="--c1:{p["c1"]};--c2:{p["c2"]}">'
                 f'<span class="cat">{p["cat"]}</span>'
                 f'<span class="thumb-emoji">{p["emoji"]}</span></div>')
    date_html = (f'<time class="post-date" datetime="{p["date"]}">{fmt_date(p["date"])}</time>'
                 if show_date else "")
    return f'''<article class="post-card">
  {thumb}
  <div class="post-body">
    <h3><a href="/blog/{p['slug']}/">{p['title']}</a></h3>
    <p>{p['desc']}</p>
    <div class="post-meta">
      <img class="author" src="/assets/img/author-avatar.png" alt="Alice Baker">
      <span>{AUTHOR}</span>
      <span>&middot;</span>
      <span>{p['read']}</span>
      {date_html}
    </div>
    <a class="read-link" href="/blog/{p['slug']}/">Read guide <span class="arrow">&rarr;</span></a>
  </div>
</article>'''


def related_cards(slug, n=3):
    """Related Articles: recommend n other blog posts, never the current one.

    Rotate the slice by the current post's position so each article shows a
    different set of recommendations (all valid internal blog links).
    """
    others = [p for p in POSTS if p["slug"] != slug]
    if not others:
        return ""
    idx = next((i for i, p in enumerate(POSTS) if p["slug"] == slug), 0)
    picked = [others[(idx + k) % len(others)] for k in range(min(n, len(others)))]
    return "".join(post_card(p) for p in picked)


# ---------------------------- pages ----------------------------

def build_home():
    cards = "".join(post_card(p) for p in POSTS[:3])
    faq_preview = "".join(f'''<div class="faq-item">
      <button class="faq-q">{f['q']}<span class="plus">+</span></button>
      <div class="faq-a"><p>{f['a']}</p></div>
    </div>''' for f in FAQS[:3])
    videos = [
        {"id":"Fs4LZFKoXqo","title":"Raindrops &mdash; Calm Piano Tutorial","channel":"Soothing Tutorials","tag":"SIGHT-PLAYING","url":"https://www.youtube.com/watch?v=Fs4LZFKoXqo&amp;list=PLQ_PIlf6OzqLlGAej0q49Tvip9wlqZoj0"},
        {"id":"QBH6IpRkVDs","title":"Piano for Beginners, Lesson 1: The Keyboard","channel":"Bill Hilton","tag":"BEGINNER LESSON","url":"https://www.youtube.com/watch?v=QBH6IpRkVDs&amp;list=PLpOuhygfD7QnP46wUgQudOySX_z2UOhXs"},
        {"id":"Yv-W4ezHvH0","title":"Full 10-Hour Piano Course for Beginners","channel":"Zak Serroukh","tag":"FULL COURSE","url":"https://www.youtube.com/watch?v=Yv-W4ezHvH0"},
    ]
    video_cards = "".join(f'''<a class="video-card" href="{v['url']}" target="_blank" rel="noopener noreferrer">
      <div class="video-thumb">
        <img src="/assets/img/videos/{v['id']}.webp" alt="{v['title']}" loading="lazy">
        <span class="video-play">&#9654;</span>
        <span class="video-tag">{v['tag']}</span>
      </div>
      <div class="video-info">
        <h4 class="video-title">{v['title']}</h4>
        <span class="video-channel">{v['channel']}</span>
      </div>
    </a>''' for v in videos)
    body = f'''<main>
<section class="hero">
  <div class="staff-lines"></div>
  <div class="wrap">
    <span class="hero-badge"><span class="pulse"></span> Piano guides for real players</span>
    <h1>Learn piano with<br><span class="hero-word" aria-label="Bigloong">Bigloong<span class="hero-caret" aria-hidden="true"></span></span></h1>
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
  <div class="video-strip">
    <div class="video-strip-head">
      <span class="eyebrow">Watch &amp; learn</span>
      <h3>A library of piano videos worth your time</h3>
      <p>From calm sight-reading to full beginner courses, we collect the piano learning videos that actually help you play.</p>
    </div>
    <div class="grid grid-3">{video_cards}</div>
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
    cards = "".join(post_card(p, show_date=True) for p in POSTS)
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
        "author": {"@type": "Person", "name": AUTHOR, "image": "https://" + SITE + "/assets/img/author-avatar.png"},
        "publisher": {"@type": "Organization", "name": "Bigloong"},
        "datePublished": p["date"], "dateModified": p["date"],
        "image": img_ver("https://" + SITE + p["image"]),
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
    cover = p.get("cover_img")
    if cover:
        cover_block = (f'<a class="article-cover article-cover-img" href="{img_ver(cover)}" target="_blank" rel="noopener">'
                       f'<img src="{img_ver(cover)}" alt="{p["title"]}" loading="eager"></a>')
    else:
        cover_block = (f'<div class="article-cover" style="background:linear-gradient(145deg,{p["c1"]},{p["c2"]})">'
                       f'{p["emoji"]}</div>')
    body = f'''<main>
<section class="section"><div class="wrap">
<div class="article article-lr">
  <div class="article-main">
    <span class="eyebrow">{p['cat']}</span>
    <h1>{p['full_h1']}</h1>
    <div class="article-meta">
      <img class="author" src="/assets/img/author-avatar.png" alt="Alice Baker">
      <span>By {AUTHOR}</span>
      <span>&middot;</span>
      <span>{p['read']}</span>
    </div>
    <div class="prose">{body_html}</div>
  </div>
  <aside class="article-side">
    {cover_block}
    <div class="toc"><div class="toc-box">
      <h4>On this page</h4>
      {toc_html}
    </div></div>
  </aside>
</div>
</div></section>
<section class="section section-soft"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Keep exploring</span><h2>Related Articles</h2></div>
  <div class="grid grid-3">{related_cards(slug)}</div>
</div></section>
</main>'''
    canonical = "/blog/" + slug + "/"
    write("blog/%s/index.html" % slug,
          page(p["seo_title"], p["desc"], body, active="blog",
               crumbs=crumbs, jsonld=ld, keywords=p["keywords"], canonical=canonical,
               og_image=p.get("cover_img", "") or p.get("image", "")))

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
    cards += "".join(f'''<article class="post-card faq-card">
  <div class="post-body">
    <h3><a href="/faq/{f['slug']}/">{f['title']}</a></h3>
    <p>{f['desc'][:150]}...</p>
    <a class="read-link" href="/faq/{f['slug']}/">Read guide <span class="arrow">&rarr;</span></a>
  </div>
</article>''' for f in FAQ_ARTICLES)
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
  <div class="help-search">
    <svg class="search-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><line x1="20" y1="20" x2="16.65" y2="16.65"></line></svg>
    <input id="faqSearch" type="search" placeholder="Search for articles..." aria-label="Search frequently asked questions" autocomplete="off">
  </div>
</div></section>
<section class="section"><div class="wrap">
  <div class="grid grid-3 faq-grid">{cards}</div>
  <p id="faqNoResults" class="faq-empty" hidden>No answers found. Try a different phrase, or <a href="/contact-us/">contact us</a>.</p>
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
<script>
(function(){{
  var input = document.getElementById('faqSearch');
  if (!input) return;
  var cards = [].slice.call(document.querySelectorAll('.faq-grid .faq-card'));
  var empty = document.getElementById('faqNoResults');
  input.addEventListener('input', function(){{
    var q = this.value.trim().toLowerCase(), shown = 0;
    cards.forEach(function(c){{
      var hit = !q || c.textContent.toLowerCase().indexOf(q) !== -1;
      c.hidden = !hit;
      if (hit) shown++;
    }});
    empty.hidden = !(q && shown === 0);
  }});
}})();
</script>
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
    <div class="article-meta"><img class="author" src="/assets/img/author-avatar.png" alt="Alice Baker"><span>By {AUTHOR}</span></div>
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

def build_faq_article(f):
    """Long-form FAQ article with Article + FAQPage + BreadcrumbList schema."""
    slug = f["slug"]
    with open(os.path.join(ROOT, f["body_file"]), encoding="utf-8") as fh:
        body_html = fh.read()
    toc_html = "".join(f'<a href="#{i}">{t}</a>' for i, t in f["toc"])
    article_ld = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": f["full_h1"], "description": f["desc"],
        "author": {"@type": "Person", "name": AUTHOR, "image": "https://" + SITE + "/assets/img/author-avatar.png"},
        "publisher": {"@type": "Organization", "name": "Bigloong"},
        "datePublished": f["date"], "dateModified": f["date"],
        "mainEntityOfPage": "https://" + SITE + "/faq/" + slug + "/"
    }
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q,
                              "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in f["faqs"]]}
    crumbs = [("Home", "/"), ("FAQ", "/faq/"), (f["title"], None)]
    ld = ('<script type="application/ld+json">' + json.dumps(article_ld, ensure_ascii=False) + '</script>'
          + '<script type="application/ld+json">' + json.dumps(faq_ld, ensure_ascii=False) + '</script>'
          + ld_breadcrumb(crumbs))
    cover_block = (f'<div class="article-cover" style="background:linear-gradient(145deg,#FFF0C9,#E7E5F6)">&#127929;</div>')
    body = f'''<main>
<section class="section"><div class="wrap">
<div class="article article-lr">
  <div class="article-main">
    <span class="eyebrow">FAQ Guide</span>
    <h1>{f['full_h1']}</h1>
    <div class="article-meta">
      <img class="author" src="/assets/img/author-avatar.png" alt="Alice Baker">
      <span>By {AUTHOR}</span>
      <span>&middot;</span>
      <span>{f['read']}</span>
    </div>
    <div class="prose">{body_html}</div>
  </div>
  <aside class="article-side">
    {cover_block}
    <div class="toc"><div class="toc-box">
      <h4>On this page</h4>
      {toc_html}
    </div></div>
  </aside>
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
          page(f["seo_title"], f["desc"], body, active="faq",
               crumbs=crumbs, jsonld=ld, keywords=f["keywords"], canonical=canonical))

def video_thumb(v):
    if v.get("cover_img"):
        return (f'<div class="post-thumb post-thumb-cover">'
                f'<img src="{img_ver(v["cover_img"])}" alt="{v["title"]}" loading="lazy">'
                f'<span class="cat">Video</span>'
                f'<span class="dur-badge">{v["duration"]}</span></div>')
    return (f'<div class="post-thumb" style="--c1:{v["c1"]};--c2:{v["c2"]}">'
            f'<span class="cat">Video</span>'
            f'<span class="thumb-emoji">{v["emoji"]}</span>'
            f'<span class="dur-badge">{v["duration"]}</span></div>')


def build_video_index():
    cards = ""
    for v in VIDEOS:
        cards += f'''<article class="post-card">
  {video_thumb(v)}
  <div class="post-body">
    <h3><a href="/video-tutorial/{v['slug']}/">{v['title']}</a></h3>
    <p>{v['desc']}</p>
    <div class="post-meta"><img class="author" src="/assets/img/author-avatar.png" alt="Alice Baker"><span>{AUTHOR}</span></div>
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

def related_video_cards(slug, n=3):
    """Recommend n other video tutorials, never the current one. Rotate by the
    current video's position so each page shows a different valid set."""
    others = [x for x in VIDEOS if x["slug"] != slug]
    if not others:
        return ""
    idx = next((i for i, x in enumerate(VIDEOS) if x["slug"] == slug), 0)
    picked = [others[(idx + k) % len(others)] for k in range(min(n, len(others)))]
    cards = ""
    for x in picked:
        cards += f'''<article class="post-card">
  {video_thumb(x)}
  <div class="post-body">
    <h3><a href="/video-tutorial/{x['slug']}/">{x['title']}</a></h3>
    <p>{x['desc']}</p>
    <div class="post-meta"><img class="author" src="/assets/img/author-avatar.png" alt="Alice Baker"><span>{AUTHOR}</span></div>
    <a class="read-link" href="/video-tutorial/{x['slug']}/">Watch tutorial <span class="arrow">&rarr;</span></a>
  </div>
</article>'''
    return cards


def build_video_detail(v):
    slug = v["slug"]
    steps = "".join(f'<li>{s}</li>' for s in v["steps"])
    ld_obj = {"@context": "https://schema.org", "@type": "VideoObject",
              "name": v["title"], "description": v["desc"],
              "uploadDate": "2026-11-19", "duration": "PT6M",
              "thumbnailUrl": "https://" + SITE + "/assets/css/placeholder.jpg"}
    crumbs = [("Home", "/"), ("Video Tutorial", "/video-tutorial/"), (v["title"], None)]
    ld = '<script type="application/ld+json">' + json.dumps(ld_obj, ensure_ascii=False) + '</script>' + ld_breadcrumb(crumbs)
    if v.get("embeds"):
        def yt(e):
            return (f'<iframe src="https://www.youtube.com/embed/{e["id"]}" '
                    f'title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; '
                    f'clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" '
                    f'allowfullscreen loading="lazy"></iframe>')
        shorts = [e for e in v["embeds"] if e.get("ratio", "9/16") == "9/16"]
        wides = [e for e in v["embeds"] if e.get("ratio") == "16/9"]
        parts = ""
        if shorts:
            cards = ""
            for e in shorts:
                desc = f'<p class="short-desc">{e["desc"]}</p>' if e.get("desc") else ""
                cards += (f'<div class="short-item"><div class="short-frame">{yt(e)}</div>'
                          f'<span class="short-label">{e["label"]}</span>{desc}</div>')
            parts += f'<div class="shorts-row cols-{len(shorts)}">{cards}</div>'
        for e in wides:
            desc = f'<p>{e["desc"]}</p>' if e.get("desc") else ""
            parts += (f'<div class="embed-wide"><div class="wide-frame">{yt(e)}</div>'
                      f'<div class="wide-copy"><h3>{e["label"]}</h3>{desc}</div></div>')
        media = f'<div class="video-embeds">{parts}</div>'
    else:
        media = (f'<div class="video-placeholder" style="background:linear-gradient(145deg,{v["c1"]},{v["c2"]})">'
                 f'<span class="vp-play">&#9654;</span>'
                 f'<span class="vp-label">Video tutorial coming soon</span></div>')
    prose = f'''<div class="prose">
      <p class="article-lead">{v['desc']}</p>
      <h2 id="steps">What you will learn</h2>
      <ol>{steps}</ol>
      <div class="note"><strong>Tip</strong> Practise one step at a time and only move on when the current one feels easy.</div>
    </div>'''
    if v.get("intro"):
        # Rich layout: intro copy -> video -> sheet music (image + anchored download) -> steps
        sh = v["sheet"]
        intro_block = f'<div class="prose"><p class="article-lead">{v["intro"]}</p></div>'
        sheet_block = f'''<div class="sheet-music">
      <h2 id="sheet-music">Piano sheet music</h2>
      <img class="sheet-preview" src="{sh['img']}" alt="Twinkle Twinkle Little Star piano sheet music preview" loading="lazy">
      <p class="sheet-note">{sh['note']}<a href="{sh['url']}" target="_blank" rel="noopener">{sh['anchor']}</a>.</p>
    </div>'''
        steps_block = f'''<div class="prose">
      <h2 id="steps">What you will learn</h2>
      <ol>{steps}</ol>
      <div class="note"><strong>Tip</strong> Practise one step at a time and only move on when the current one feels easy.</div>
    </div>'''
        content = intro_block + "\n    " + media + "\n    " + sheet_block + "\n    " + steps_block
    else:
        content = (prose + "\n    " + media) if v.get("copy_first") else (media + "\n    " + prose)
    body = f'''<main>
<section class="section"><div class="wrap">
<div class="article single-col">
  <div class="article-main">
    <span class="eyebrow">Video Tutorial &middot; {v['duration']}</span>
    <h1>{v['title']}</h1>
    <div class="article-meta"><img class="author" src="/assets/img/author-avatar.png" alt="Alice Baker"><span>By {AUTHOR}</span></div>
    {content}
  </div>
</div>
</div></section>
<section class="section section-soft"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Keep exploring</span><h2>Related Video Tutorials</h2></div>
  <div class="grid grid-3">{related_video_cards(slug)}</div>
</div></section>
</main>'''
    canonical = "/video-tutorial/" + slug + "/"
    write("video-tutorial/%s/index.html" % slug,
          page(v["title"] + " | Bigloong Video Tutorial", v["desc"], body, active="video",
               crumbs=crumbs, jsonld=ld, keywords=v.get("keywords", ""), canonical=canonical,
               og_image=v.get("cover_img", "")))

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

# 页面首次发布日期（W3C 日期），取自 git 首次入库/上线日，写死后不再随正文修改而变。
# 与网页上显示的发布时间（各条目的 date 字段，可改）完全解耦：改网页日期不影响 sitemap lastmod。
FIRST_PUBLISHED = {
    "/": "2026-11-19", "/blog/": "2026-11-19", "/faq/": "2026-11-19", "/video-tutorial/": "2026-11-19",
    "/about-us/": "2026-11-19", "/privacy/": "2026-11-19", "/contact-us/": "2026-11-19", "/terms/": "2026-11-19",
    # blog
    "/blog/how-to-tune-a-piano-yourself-basic-guide/": "2026-11-22",
    "/blog/music-theory-basics-for-piano/": "2026-11-22",
    "/blog/piano-finger-exercises-for-beginners/": "2026-11-22",
    "/blog/how-to-play-chords-on-piano/": "2026-11-20",
    "/blog/how-much-does-a-piano-cost/": "2026-11-19",
    "/blog/how-to-start-learning-piano/": "2026-11-19",
    "/blog/how-to-improve-piano-finger-speed-and-dexterity/": "2026-11-19",
    "/blog/how-to-read-sheet-music-piano/": "2026-11-19",
    # faq (short)
    "/faq/how-often-should-i-tune-a-piano/": "2026-11-19",
    "/faq/digital-or-acoustic-piano-for-beginners/": "2026-11-19",
    "/faq/how-long-does-it-take-to-learn-piano/": "2026-11-19",
    "/faq/best-age-to-start-piano-lessons/": "2026-11-19",
    "/faq/do-i-need-a-piano-teacher/": "2026-11-19",
    "/faq/what-is-the-80-20-rule-for-piano/": "2026-11-19",
    # faq (article)
    "/faq/is-piano-a-string-instrument/": "2026-11-22",
    "/faq/how-many-keys-on-a-piano/": "2026-11-20",
    # video-tutorial
    "/video-tutorial/piano-posture-for-beginners/": "2026-11-19",
    "/video-tutorial/finding-middle-c-on-piano/": "2026-11-19",
    "/video-tutorial/first-piano-song-tutorial/": "2026-11-19",
    "/video-tutorial/piano-scales-for-beginners/": "2026-11-19",
    "/video-tutorial/how-to-play-twinkle-twinkle-little-star-on-the-piano/": "2026-11-19",
    "/video-tutorial/how-to-play-happy-birthday-on-piano/": "2026-11-22",
    # 2026-11-23 batch
    "/blog/do-you-need-88-keys-on-a-piano/": "2026-11-23",
    "/blog/how-much-do-piano-lessons-cost/": "2026-11-23",
    "/video-tutorial/how-to-play-erika-on-piano/": "2026-11-23",
}

def _sitemap_priority(u):
    if u == "/":
        return "1.0"
    if u in ("/blog/", "/faq/", "/video-tutorial/"):
        return "0.8"
    if u.startswith(("/blog/", "/faq/", "/video-tutorial/")):
        return "0.6"
    return "0.4"  # about / privacy / contact / terms 等信息页

def build_sitemap():
    urls = ["/", "/blog/", "/faq/", "/video-tutorial/", "/about-us/", "/privacy/", "/contact-us/", "/terms/"]
    urls += ["/blog/%s/" % p["slug"] for p in POSTS]
    urls += ["/faq/%s/" % f["slug"] for f in FAQS]
    urls += ["/faq/%s/" % f["slug"] for f in FAQ_ARTICLES]
    urls += ["/video-tutorial/%s/" % v["slug"] for v in VIDEOS]
    entries = "".join(
        f"  <url><loc>https://{SITE}{u}</loc><lastmod>{FIRST_PUBLISHED.get(u, '2026-11-19')}</lastmod>"
        f"<priority>{_sitemap_priority(u)}</priority></url>\n"
        for u in urls
    )
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
    for f in FAQ_ARTICLES:
        build_faq_article(f)
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
