# FUMIHEALING: Company Website

## What this project is
Static company website for **"FOLIYA JAPAN" MCHJ** — a Japanese-style deep lymph care salon and training school founded by **Suzuki Fumiko** in Tashkent, Uzbekistan (registered 10.09.2025, reg. № 2940359).

The site introduces the company, the FUMIHEALING: method, the training school, and contact info. No user accounts, no bookings, no database — pure content.

## Tech stack
- **Django** (no database — `INSTALLED_APPS` has only `staticfiles` + `website`)
- **whitenoise** for static file serving in production
- **gunicorn** as WSGI server
- **Django i18n** — 4 languages: English (default), Uzbek (`uz`), Russian (`ru`), Japanese (`ja`)
- Deployed to **Render.com** via `render.yaml`

## Commands
```bash
python manage.py runserver          # local dev
python manage.py compilemessages    # after editing .po translation files
python manage.py collectstatic --no-input  # before deploy
```
**Never run `migrate`** — there is no database configured. This is intentional.

## Pages (5 total)
| URL | Template | Content |
|---|---|---|
| `/` | `home.html` | Hero, stats, pillars, gallery, school CTA |
| `/about/` | `about.html` | Fumiko's story, timeline, mission, values |
| `/method/` | `method.html` | Philosophy, deep vs surface, shiatsu, comparison table |
| `/school/` | `school.html` | 6-module curriculum, gallery, omotenashi |
| `/contact/` | `contact.html` | Address, phone, email, Telegram, registration |

## Key file locations
```
website/
  templates/website/     ← all 5 page templates + base.html
  static/website/
    css/style.css        ← all design (CSS variables, components, responsive)
    img/                 ← owner_image.png, owner_image_2.png, foliya_logo_2.png, massage_1-4.png
    favicon/             ← favicon.ico, PNGs, apple-touch-icon, webmanifest
locale/
  uz/ru/ja/LC_MESSAGES/  ← django.po (source) + django.mo (compiled)
render.yaml              ← Render.com deployment config
```

## Design system (style.css)
- Colors: `--teal: #2d6a6a`, `--gold: #c09a52`, `--ivory: #faf9f7`, `--ink: #1a1a1a`
- Fonts: Noto Serif JP (body/headings) + Noto Sans JP (UI elements)
- Japanese-minimalist aesthetic — clean whitespace, thin rules, subtle kanji watermarks
- Gallery images use `filter: contrast(1.12) brightness(0.82) saturate(0.68)` for editorial look
- Mobile breakpoints: 900px (tablet) and 640px (mobile — hamburger nav)

## Company facts
- **Founder:** Suzuki Fumiko (鈴木 文子) — 17 years as therapist/educator in Japan
- **Brand name:** FUMIHEALING: (the colon is part of the brand name)
- **Legal entity:** "FOLIYA JAPAN" MAS'ULIYATI CHEKLANGAN JAMIYAT
- **INN:** 312420998
- **Address:** Yangihayet district, Fayzli MFY, Rayxon ko'chasi, 107-uy, Tashkent
- **Phone:** +998 (91) 099-00-23
- **Email:** 232355fh@gmail.com
- **Telegram:** https://t.me/fumihealing
- **Tagline (Japanese):** 先に整えて、流す ("Balance first, then flow")

## Method philosophy
FUMIHEALING: combines Japanese shiatsu (point work) with lymph drainage (area work). The key principle is **balance before drainage** — unlike most methods that simply push lymph, this approach first releases muscle tension and corrects structural imbalance so the body flows naturally. Sessions focus on the décolleté, neck, and arms. Depth, patience ("pause and wait"), and the spirit of omotenashi (hospitality) are central to the teaching.

## Translation workflow
1. Edit text in templates using `{% trans "..." %}` tags
2. Run `python manage.py makemessages -l uz -l ru -l ja` to extract new strings
3. Fill translations in `locale/XX/LC_MESSAGES/django.po`
4. Run `python manage.py compilemessages` to compile `.mo` files
5. Language switcher in navbar links to `/en/`, `/uz/`, `/ru/`, `/ja/`
