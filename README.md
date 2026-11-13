# Website Launch Checklist Skill

A Claude skill for the pre-launch and go-live checklist of a business website, built from Asjad's real website work. Claude handles all the work end to end — domain, hosting and SSL, page inventory, form tests, SEO basics, analytics, mobile, speed, the 404 page, the go-live run sheet, and the first-week checks — with the owner involved only for the decisions, accounts, sign-ins and approval gates. It is modeled on the launch standard behind the live store Fragrance Empire, a complete Shopify store with 155 products, 18 brands and 28 collections.

## What it does

Takes a finished website from "looks done" to verified live in one repeatable workflow:

1. **Brief** — business, domain, page list for the tier, forms, analytics, launch date. No checking before the brief is confirmed.
2. **Domain + hosting + SSL** — domain connected and primary, SSL active, no mixed content, www / non-www redirect correct.
3. **All pages present** — home, about, services/products, contact, privacy policy, terms, with no placeholder text left.
4. **Forms tested** — every form submits, the confirmation shows, the owner receives the submission, and the failure cases show a clear error.
5. **SEO basics** — unique title + meta description per page, one H1 per page, image alt text, sitemap submitted, Search Console verified, favicon present.
6. **Analytics** — installed on every page and confirmed receiving data in the owner's account.
7. **Mobile test** — every page on a real phone-sized viewport, no horizontal scroll, tap targets big enough, full visitor journey on a phone.
8. **Speed check** — images sized for the web, no render-blocking bloat, fast on mobile data.
9. **404 page** — custom, branded, with a link back home (and a real 404 status).
10. **Go-live steps in order** — content freeze, backup, DNS / domain switch, live verification of every page + form, then announce.
11. **First week** — broken links, form submissions, analytics, search indexing, fixes re-verified live, handover.

## Who does what — Claude handles all the work end to end

Claude runs every check — the page inventory, the form test plan, the SEO, mobile and speed checks, the go-live run sheet, the first-week report. The owner is involved only at three points: (1) decisions only the owner can make (domain, hosting, contact details, business facts, page list, what each form must do); (2) accounts, sign-ins and money (registrar, hosting, Search Console, analytics, and any payment — all on the owner's own device); and (3) approval gates (filled-in checklist, go-live run sheet, exact launch moment). The two device-bound exceptions are hosting / registrar access (browser with the owner's sign-in) and confirming a test form submission arrived and analytics is receiving data (owner's inbox / account, on their device). Everything else is Claude's work — do not hand it back to the owner as homework.

## The live example site

- **Site:** Fragrance Empire — https://fragranceempire.my
- **Platform:** Shopify, Basic plan, Horizon theme, currency MYR, timezone Asia/Kuala_Lumpur, market Malaysia
- **Catalog:** 155 products = 142 single products + 13 bundles, 18 brands, 28 collections
- **Domain:** connected and primary; SSL active; the store loads on the real domain
- **Contact:** info@fragranceempire.my is the contact / notifications / About sender
- **Pages:** Home, About, Contact, FAQ, policies (Privacy, Refund / Return, Shipping, Terms of Service), plus collection and product pages
- **Shipping promise:** Standard, FREE, 3–5 business days across Malaysia; product pages show Ordered today / Packed +1 day / Delivered +2 days, "Dispatched in 24 hours."
- **Mobile-first:** about 90% of customers order by mobile, so every page is checked on a phone-sized viewport first
- **Built by:** Asjad Farooq, Shopify Store Designer — Shopify gig https://www.fiverr.com/s/L34yBpA

## Service tiers (the seller's real website packages)

| Tier | Pages | Delivery | Revisions | Price |
|---|---|---|---|---|
| Basic | 1 | 3 days | Unlimited | $80 |
| Standard | Up to 5 | 5 days | Unlimited | $180 |
| Premium | Up to 10 | 7 days | Unlimited | $350 |

Ask the owner which tier the build is before starting, and do not check a bigger scope than the tier covers without agreement. The launch checklist itself is the same for every tier; only the page inventory changes size.

## Files

```
website-launch-checklist/
├── README.md                                  # this file
└── website-launch-checklist/
    ├── SKILL.md                               # the Claude skill — the workflow itself
    ├── scripts/
    │   └── check_site.py                      # public checks: reachability, SSL, title/meta, sitemap, favicon
    └── templates/
        ├── launch-checklist.md                # brief + full pre-launch checklist (printable, tickable)
        ├── launch-checklist.csv               # same checklist as a spreadsheet (one row per check)
        ├── go-live-run-sheet.md               # go-live steps in order, with times and sign-off
        └── first-week-check.md                # post-launch checks for day 1, day 3, day 7 + handover
```

## Setup

### 1. Get the brief first

Fill in `templates/launch-checklist.md` (Step 1 of `SKILL.md`) with the owner: business name, domain, page list for the tier, every form and who receives it, analytics tool and account owner, launch date. Do not start checking until the owner confirms the brief.

### 2. Run the automated checks (no login needed)

`scripts/check_site.py` uses only the Python standard library, so it runs anywhere Python 3 is installed. It checks only what a visitor can see — it cannot test forms, confirm analytics data, or judge content, so it never replaces the manual checks in `SKILL.md`.

```bash
python3 scripts/check_site.py https://example-business.com
python3 scripts/check_site.py https://example-business.com --pages /about /services /contact
python3 scripts/check_site.py https://example-business.com --output launch-check.json
```

Exit code 0 means every check passed; exit code 1 means at least one check failed — fix every failure before launch.

### 3. Hosting / registrar access

If a step needs the hosting panel or the domain registrar, the owner signs in on their own device and approves the change, or approves a browser session. Claude prepares the exact change (written in the run sheet first) and the owner applies it. No credentials in the skill files, in chat, or in a repo — credentials live only in the owner's secure storage.

### 4. Use in Claude

Copy the `website-launch-checklist/` folder into a Claude skills directory (for example a Claude Code skills folder, or a repo Claude is pointed at), or keep this whole repo and point Claude at `website-launch-checklist/SKILL.md`. Then ask Claude to run the workflow, for example: "Check my business website before launch using the website-launch-checklist skill. Tier: Standard. Site: https://example-business.com"

## Honest limits — read before using

- **No direct hosting connection.** Claude does not have a built-in hosting or registrar connection. Changes go through the browser (owner's sign-in + approval) or the public checks in `check_site.py`, which need no login. Never claim direct auto-setup without one of those.
- **No credentials in the skill.** No API keys, passwords, access tokens, bank details or secrets are stored in these files. If a step needs a login or a payment detail, the owner does it on their own device.
- **Approval gate is mandatory.** No DNS change, domain switch, or launch announcement happens until the owner approves the filled-in checklist, the run sheet, and the exact launch moment. A changed page, price, form or policy after approval needs fresh approval.
- **Never invent business facts.** Every business name, address, phone number, email, price, opening hour and policy timeframe comes from the owner. Placeholder text is a launch blocker, not a detail to leave in.
- **Public checks cannot see everything.** The script checks reachability, SSL, title / meta, sitemap and favicon only. Form submissions, analytics data, login-only pages, and whether the content is correct are checked by hand and never marked passed on the script's say-so alone.
- **Paid tools and paid plans need approval.** Never buy a domain, hosting plan, SSL certificate, or paid tool, or accept a trial that converts to a charge, without the owner approving the exact price first.
- **Do not change DNS, redirects, or hosting settings without approval.** A wrong DNS change can take the live site down. Every DNS change is written in the run sheet first, approved, and then applied once.

## How to run one launch

1. Fill in the brief in `templates/launch-checklist.md` and get the owner to confirm it.
2. Work Steps 2–9 of `SKILL.md` in order. Run `scripts/check_site.py` early (Step 2) and again at go-live (Step 10).
3. Fill in `templates/go-live-run-sheet.md` and get the owner's approval at the gate (Step 10).
4. Run the go-live steps in order, verify live, then announce.
5. Do the first-week checks in `templates/first-week-check.md` on day 1, day 3, and day 7, and hand over the completed documents.
