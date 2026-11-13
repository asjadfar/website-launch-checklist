# Website Launch Checklist

> Complete one copy per website. Nothing goes live until the owner approves
> this filled-in checklist, the go-live run sheet, and the exact launch moment.
> A changed page, price, form or policy after approval needs fresh approval.
> Fill in every [bracketed] field — never leave a decision blank and never guess one.
> Print this file and tick the boxes by hand, or use `launch-checklist.csv`
> for the same checks in a spreadsheet.

## Step 1 — Brief (complete before checking)

- **Business name:**
- **Website address (domain):** https://
- **What the business does (one sentence):**
- **Tier (circle one):** Basic (1 page, 3 days, $80) / Standard (up to 5 pages, 5 days, $180) / Premium (up to 10 pages, 7 days, $350)
- **Launch date wanted:**
- **Domain registrar:**
- **Hosting provider / plan:**
- **Who holds the registrar + hosting logins:** owner, on their own device
- **Contact email shown on the site:**
- **Contact phone / WhatsApp shown on the site:**
- **Shop / office address (only if public):**
- **Analytics tool:** [ ] Google Analytics / [ ] Other: ___ — **Account owner (email):**
- **Explicitly NOT wanted (e.g. no live chat yet, no newsletter form, no prices shown, no social feed):**
- **Owner confirmed the brief:** [ ] Yes — name / date:

## Page inventory — one row per page (add rows for the tier)

| Page | URL | Content approved by owner |
|---|---|---|
| Home | https:// / | [ ] |
| About | https:// /about | [ ] |
| Services / Products | https:// /services | [ ] |
| Contact | https:// /contact | [ ] |
| Privacy Policy | https:// /privacy-policy | [ ] |
| Terms of Service | https:// /terms | [ ] |
| Extra page (Standard / Premium only) | https:// / | [ ] |
| Extra page (Standard / Premium only) | https:// / | [ ] |
| Extra page (Premium only) | https:// / | [ ] |
| Extra page (Premium only) | https:// / | [ ] |

## Step 2 — Domain + hosting + SSL

- [ ] Domain connected to hosting and set as the primary domain
- [ ] Site loads on the real domain (not only a staging / platform subdomain)
- [ ] SSL certificate active — padlock shown, URL starts with `https://`, no browser warning
- [ ] No mixed-content warnings on the homepage or any key page (no `http://` images, fonts, or scripts)
- [ ] `www` and non-`www`: one redirects to the other (the primary); neither shows an error
- **Automated check run:** [ ] `python3 scripts/check_site.py https://` — date: ___ — result: ___ passed / ___ failed
- **SSL expiry date:** ___ (renewal owner: ___)

## Step 3 — All pages present, no placeholder text

- [ ] Every page in the inventory above loads (no error, no blank page, no broken layout)
- [ ] Every page has the owner's real content — no "Lorem ipsum", no "Your business here", no theme sample text, no watermarked placeholder image
- [ ] Every image is the right image for that page, loads fully, and has alt text
- [ ] Every link goes somewhere real — no `#` links, no links to missing pages, no links to the template maker's demo site
- [ ] Prices, opening hours, phone numbers and email addresses match the brief exactly
- [ ] Home, About, Services / Products, Contact, Privacy Policy, Terms of Service all present
- [ ] Header and footer identical on every page (logo, navigation, contact details, social links, policy links)
- **Pages not ready (page + exact problem + who fixes it):**

## Step 4 — Forms tested (one block per form — copy as needed)

### Form 1

- **Page:** ___ — **Purpose (e.g. contact, quote request):**
- **Fields:**
- **Who must receive the submission (inbox / form tool):**
- [ ] Submitted with test data ("Test Launch", owner@example.com, "Launch test — please ignore")
- [ ] Confirmation message / page shown — exact words:
- [ ] Owner received the submission with all fields intact — where confirmed:
- [ ] Empty required field shows a clear error and sends nothing
- [ ] Invalid email address shows a clear error and sends nothing
- [ ] Spam protection on (if owner asked for it) and a real visitor can still complete the form
- **Tested by / date:**

### Form 2

- **Page:** ___ — **Purpose:**
- **Fields:**
- **Who must receive the submission:**
- [ ] Test submission sent, confirmation shown, owner received it
- [ ] Empty-field and invalid-email errors checked
- **Tested by / date:**

## Step 5 — SEO basics

- [ ] Every page has a unique `<title>` under 60 characters (page + business name)
- [ ] Every page has a unique meta description under 160 characters
- [ ] Every page has one `<h1>` matching what the page is about
- [ ] Every image has alt text (not "image1.jpg")
- [ ] Sitemap loads (https:// /sitemap.xml) and lists every live page
- [ ] Site submitted to Google Search Console — ownership verified — date:
- [ ] Favicon present — browser tab shows the business icon, not the platform default
- **Duplicate titles / descriptions found (fix before launch):**

## Step 6 — Analytics

- **Analytics tool:** ___ — **Account owner:** ___
- [ ] Analytics code installed on every page in the inventory (not only the homepage)
- [ ] Data confirmed receiving: site visited from a phone, visit appeared in the real-time report — date:
- [ ] Owner can open the analytics account themselves
- **If analytics is pending:** written here as pending, owner approved the delay: [ ] Yes — name / date:

## Step 7 — Mobile test

- **Phone / viewport used:** ___ (width: ___ px) — **Date:**
- [ ] Every page checked on a phone-sized viewport (about 360–390 px wide)
- [ ] No horizontal scroll on any page
- [ ] No text cut off at the edge, no overlapping text or buttons
- [ ] Images fit the screen; navigation menu opens and closes
- [ ] Tap targets big enough (about 44 × 44 px) and far enough apart
- [ ] Full visitor journey tested on a phone: homepage → services / products → contact → form submitted
- [ ] Tested on a real phone (not only a desktop preview): [ ] Yes — phone model: ___ / [ ] No — reason:
- **Mobile problems found (page + problem):**

## Step 8 — Speed check

- **Connection used for the test:** ___ (e.g. mobile data / throttled 4G) — **Date:**
- [ ] Homepage usable within a few seconds on mobile data — time to usable: ___ seconds
- [ ] Heaviest page checked (page: ___) — time to usable: ___ seconds
- [ ] Every image sized for the web — largest image file: ___ KB (aim under about 300 KB each)
- [ ] No unused apps, widgets, fonts, or scripts loading on pages that do not need them
- [ ] Speed re-checked after every fix — final check date:
- **Slow pages and their cause (which image / script):**

## Step 9 — 404 page

- [ ] Visiting https:// /this-page-does-not-exist shows a custom, branded 404 page
- [ ] 404 page says plainly the page does not exist and links back to the homepage
- [ ] 404 page links to the contact page
- [ ] 404 page is NOT the platform default, a blank page, or a server error
- [ ] Missing URL returns a real 404 status (confirmed by `scripts/check_site.py` or the browser)

## Step 10 — Go-live approval gate (mandatory)

- **Owner approved this filled-in checklist:** [ ] Yes — name / date:
- **Owner approved the go-live run sheet:** [ ] Yes — name / date:
- **Owner approved the exact launch moment:** [ ] Yes — date / time:
- **Go-live run sheet completed and attached:** [ ] Yes — file: `templates/go-live-run-sheet.md`

Do NOT launch if any approval box above is unticked. If anything changed after approval (page, price, form, policy), get fresh approval first.

## Step 11 — First week after launch

- **First-week check file:** `templates/first-week-check.md` — completed on day 1, day 3, day 7: [ ] Yes
- [ ] Broken links re-checked and fixed
- [ ] Real form submissions arriving and received by the owner
- [ ] Analytics data arriving every day
- [ ] Site indexed (business-name search) with no new Search Console errors
- **Handover given to the owner (completed checklist, run sheet, first-week check, backup location, login list — no passwords written down):** [ ] Yes — date:
- **Still pending (if anything):**
