---
name: website-launch-checklist
description: Pre-launch and go-live checklist for a business website — Claude checks domain, hosting and SSL, every page, every form, SEO basics, analytics, mobile, speed, and the custom 404 page, then runs the go-live steps in order and the first-week checks. Use when the user asks to launch a website, check a site before it goes live, audit a live site, or verify a site after a redesign or domain switch. Modeled on the launch standard behind Fragrance Empire (fragranceempire.my) and the seller's website gig (Basic $80 / 1 page, Standard $180 / up to 5 pages, Premium $350 / up to 10 pages).
---

# Website Launch Checklist

## When to use

Use this skill when the user asks to launch a business website, check a website before it goes live, audit a site that is already live, verify a site after a redesign, a domain switch, or a move to new hosting, or prepare a site for handover to its owner. The end result is a site that is checked page by page and form by form — not a site that "looks done" on one screen.

Do not use it for building the site itself (that is the build work, done before this skill starts), for a Shopify store build (use the shopify-store-automation skill), or for ongoing content updates after the first week (use a direct edit instead).

## Who does what — Claude handles all the work end to end

Claude runs every check in this skill — domain and SSL, page inventory, form tests, SEO, analytics, mobile, speed, 404 page, the go-live run sheet, and the first-week checks. The owner is involved only at these points:

1. **Decisions only the owner can make** — the domain name, the hosting account, the contact email and phone shown on the site, the business name and address used in the policies, which pages the site has, and what each form must do (who receives it, what the confirmation says).
2. **Accounts, sign-ins and money** — creating or logging in to the domain registrar, the hosting account, Google Search Console, and the analytics account; entering bank / card details; and paying for a domain, hosting plan, or paid tool. These happen on the owner's own device, with the owner's own details. Claude never handles the owner's password, bank details, or payment credentials.
3. **Approval gates** — the owner approves the filled-in checklist, the go-live run sheet, and the exact launch moment before anything goes live (see Step 9). Nothing is switched on, redirected, or announced without that approval.

Two device-bound exceptions, stated honestly so the "end to end" claim is not overstated:

- **Hosting / registrar access:** Claude works through the owner's hosting panel or registrar (browser, with the owner's sign-in) or from the public checks in `scripts/check_site.py`, which need no login at all. Claude never invents hosting or registrar credentials and never logs in as the owner.
- **Forms and analytics accounts:** Claude writes the test plan and reads the public results; the owner (or the owner's inbox) confirms that a test submission actually arrived, and confirms analytics is receiving data in the analytics account on their own device.

Everything else — the page inventory, the checks, the filled-in checklist, the run sheet, the first-week report — is Claude's work. Do not hand any of it back to the owner as homework.

## Website facts — the live reference store (do not invent others)

Fragrance Empire (https://fragranceempire.my) is the live site this skill's launch standard is modeled on. Use its real, verified facts as the reference example. Do not invent a different reference site.

- **Site:** Fragrance Empire, fragranceempire.my, Shopify, Horizon theme, currency MYR, timezone Asia/Kuala_Lumpur, market Malaysia.
- **Catalog:** 155 products = 142 single products + 13 bundles, 18 brands, 28 collections.
- **Domain and hosting:** domain connected and set as primary; SSL active; the store loads on the real domain.
- **Contact:** info@fragranceempire.my is the contact / notifications / About sender; customer emails come only from that address.
- **Pages:** Home, About, Contact, FAQ, policies (Privacy, Refund / Return, Shipping, Terms of Service), plus collection and product pages.
- **Payments:** Cash on Delivery (COD) + card payments via Stripe; checkout requires a mobile number.
- **Shipping promise:** Standard, FREE, 3–5 business days across Malaysia; product pages show Ordered today / Packed +1 day / Delivered +2 days, "Dispatched in 24 hours."
- **Mobile-first:** about 90% of customers order by mobile, so every page is checked on a phone-sized viewport first.
- **Seller services — website gig (Fiverr, in draft):** "I will build a modern responsive website for your business" — Basic $80 — 1 page, 3 days; Standard $180 — up to 5 pages, 5 days; Premium $350 — up to 10 pages, 7 days. Unlimited revisions on all three packages.
- **Seller services — Shopify gig (Fiverr, live):** https://www.fiverr.com/s/L34yBpA — Basic $80 — 10 products, 5 pages, 3 days; Standard $180 — 30 products, 8 pages, 5 days; Premium $350 — 50 products, 10 pages, 7 days. Unlimited revisions on all three packages.

## Hard limits — state them honestly, do not work around them

- **No credentials in the skill.** Never put an API key, password, access token, bank detail or secret in a skill file, in chat, or in a repo. Logins, bank details and hosting / registrar setup happen on the owner's own device.
- **Approval gates are mandatory.** Nothing goes live, no DNS or domain switch happens, and no launch is announced until the owner approves the filled-in checklist and the go-live run sheet. A changed page, price, form or policy after approval needs fresh approval.
- **Never invent business facts.** Every business name, address, phone number, email, price, opening hour and policy timeframe comes from the owner. If a fact is missing, ask — do not fill it in with a plausible guess. Placeholder text ("Lorem ipsum", "Your business here", "123 Main Street", "555-0100") is a launch blocker, not a detail to leave in.
- **Never write fake reviews or fake claims.** Reviews come only from real customers, in their own words. Do not write "100% original", "No. 1 in the country", or any other claim the owner has not stated and taken responsibility for.
- **Public checks cannot see everything.** `scripts/check_site.py` checks only what a visitor can see: reachability, SSL, title / meta, sitemap, favicon. It cannot test a form submission, confirm analytics is receiving data, check a page that needs a login, or judge whether the content is correct. Those checks are done by hand in Steps 3, 5 and 6 and are never marked passed on the script's say-so alone.
- **Speed and mobile checks are indicative, not a guarantee.** A fast result on one connection does not prove the site is fast on mobile data everywhere. Record the connection and device used for each speed test.
- **Paid tools and paid plans need the owner's approval.** Never buy a domain, hosting plan, SSL certificate, or paid tool, or accept a trial that converts to a charge, without the owner approving the exact price first.
- **Do not change DNS, redirects, or hosting settings without the owner's approval.** A wrong DNS change can take the live site down. Every DNS change is written down in the run sheet first, approved, and then applied once.

## Scope tiers — ask which one before starting

Mirror the seller's real website packages. Ask the owner which tier the build is, and do not check a bigger scope than the tier covers without agreement.

| Tier | Pages | Delivery | Revisions | Price |
|---|---|---|---|---|
| Basic | 1 | 3 days | Unlimited | $80 |
| Standard | Up to 5 | 5 days | Unlimited | $180 |
| Premium | Up to 10 | 7 days | Unlimited | $350 |

"Pages" means the site's pages (Home, About, Services / Products, Contact, Privacy Policy, Terms). A site bigger than the tier — more pages, an online store, a booking system, a blog — is a separate scope: agree it (and its price) before starting. The launch checklist itself is the same for every tier; only the page inventory changes size.

## Workflow

### Step 1 — Brief (decisions first, no checking before this)

Collect and write down, in `templates/launch-checklist.md`:

1. Business name, website address (domain), and what the business does in one sentence.
2. The page list for the tier: Home, About, Services / Products, Contact, Privacy Policy, Terms of Service, plus any extra pages the tier covers. Write down the exact URL of every page.
3. Domain and hosting: registrar, hosting provider / plan, who holds the logins (owner, on their own device).
4. Contact details to show on the site: email, phone / WhatsApp, address (only if the owner wants it public).
5. Every form on the site: its page, its fields, who must receive the submission, and what confirmation message the visitor must see.
6. Analytics: which tool (for example Google Analytics), and whose account it lives in.
7. Tier (Basic / Standard / Premium) and the launch date the owner wants.
8. Anything the owner explicitly does NOT want (for example: no live chat yet, no newsletter form, no prices shown on the site, no social feed embedded).

Do not start Step 2 until the brief is filled in and the owner has confirmed it. A missing page URL or a missing form recipient is a blocker, not something to guess.

### Step 2 — Domain + hosting + SSL

1. Confirm the domain is connected to the hosting and set as the primary domain. The site must load on the real domain (for example https://example-business.com), not only on a staging or platform subdomain.
2. Confirm the SSL certificate is active: the address bar shows the padlock, the URL starts with `https://`, and no browser warning appears.
3. Check for mixed content: load the homepage and every key page over HTTPS and confirm no "Not secure" warning and no blocked resource. Common causes are images, fonts, or scripts still loaded over `http://` — fix each one at the source (change the link to `https://` or to a relative path), never by hiding the warning.
4. Confirm the `www` and non-`www` versions behave as intended: one of them redirects to the other (the primary), and neither shows an error.
5. Run `scripts/check_site.py` against the live URL and record the result. A failed SSL check is a launch blocker — do not go live without HTTPS.

### Step 3 — All pages present, no placeholder text

1. Build the page inventory from the brief: one row per page, with its URL, its purpose, and its owner (who wrote / approved the content).
2. Open every page, desktop and phone-sized viewport, and check:
   - The page loads (no error, no blank page, no broken layout).
   - The heading and body text are the owner's real content — no "Lorem ipsum", no "Your business here", no sample text from the theme or template, no stock placeholder image with a watermark.
   - Every image is the right image for that page, loads fully, and has alt text.
   - Every link on the page goes somewhere real — no `#`, no link to a page that does not exist, no link to the template maker's demo site.
   - Prices, opening hours, phone numbers and email addresses match the brief exactly.
3. Required pages for every business site: Home, About, Services / Products, Contact, Privacy Policy, Terms of Service. A missing Privacy Policy or Terms page is a launch blocker.
4. Check the header and footer on every page: logo, navigation, contact details, social links, and policy links must be identical everywhere. A page with a different footer is a bug, not a variation.
5. Record any page that is not ready in the checklist with the exact problem and who must fix it. Do not mark a page passed while it still has placeholder text.

### Step 4 — Forms tested

Test every form on the site, one at a time, exactly as a visitor would:

1. Fill in every required field with test data that is clearly a test (for example name "Test Launch", email owner@example.com, message "Launch test — please ignore"). Never use a real customer's details for a test.
2. Submit the form and confirm the visitor sees a confirmation message or confirmation page — not a blank screen, not an error, not a reload with the fields emptied and no message.
3. Confirm the owner receives the submission: check the inbox (or the form tool's submissions list) the owner named in the brief, and confirm the test arrived with all fields intact.
4. Test the failure cases: submit with a required field empty, and with an invalid email address, and confirm the form shows a clear error and does not send a half-empty submission.
5. Check spam protection is on (for example a CAPTCHA or honeypot) if the owner asked for it, and that a real visitor can still complete the form without a fight.
6. Record each form in the checklist: page, fields, confirmation shown (exact words), submission received (yes / no, where), and the date tested. A form that sends nowhere, or that the owner never receives, is a launch blocker.

### Step 5 — SEO basics

1. Every page has a unique `<title>` (under 60 characters, naming the page and the business) and a unique meta description (under 160 characters, describing that page). No two pages share the same title or description, and no page has the theme's default title.
2. Every page has one main heading (`<h1>`) that matches what the page is about.
3. Every image has alt text describing the image (product / place / person, not "image1.jpg").
4. The sitemap loads (for example https://example-business.com/sitemap.xml) and lists every live page. Run `scripts/check_site.py` — it checks the sitemap and reports which pages it lists.
5. The site is submitted to Google Search Console and ownership is verified (owner's Google account, on their own device). Record the verification date.
6. A favicon is present: the browser tab shows the business's icon, not the platform default. `scripts/check_site.py` checks that the favicon file loads.
7. Check the site appears in search for its own business name after launch (Step 10) — it does not have to rank first on day one, but it must be indexed.

### Step 6 — Analytics

1. Confirm the analytics code is installed on every page, not only the homepage. (On a one-page Basic site this means the single page; on a multi-page site, check every page in the inventory.)
2. Confirm it is receiving data: open the analytics account on the owner's device, visit the site from a phone, and confirm the visit appears in the real-time report. A code snippet that is installed but sends nothing is not "analytics installed".
3. Confirm the analytics account belongs to the owner (the owner's email, not the builder's personal account), and that the owner can open it themselves.
4. Record the analytics tool, the account owner, and the date data was confirmed in the checklist. If the owner has no analytics account yet, create the account with the owner on their device before launch — do not launch with analytics "to be added later" unless the owner explicitly approves that and it is written in the checklist as pending.

### Step 7 — Mobile test

Mobile comes first: about 90% of customers order by mobile on a store like Fragrance Empire, and most business-site visitors arrive on a phone too.

1. Open every page on a real phone-sized viewport (around 360–390 px wide, for example a phone or a browser device preview at that width). Do not check mobile by shrinking a desktop window a little.
2. On every page, check: no horizontal scroll, no text cut off at the edge, no overlapping text or buttons, images fit the screen, and the navigation menu opens and closes.
3. Tap targets: every button and link must be big enough to tap with a finger (at least about 44 × 44 px) and far enough apart that the wrong one is not tapped by accident.
4. Test the full visitor journey on a phone: homepage → services / products → contact page → form submitted; and, if the site takes orders, homepage → product → cart → checkout.
5. Test on at least one real phone if possible, not only a desktop preview — a preview cannot show how the site feels on mobile data or with a real keyboard.
6. Record the phone / viewport used and every problem found, with the exact page. A page that needs horizontal scrolling on a phone is a launch blocker.

### Step 8 — Speed check

1. Check the homepage and the heaviest page (usually the page with the most images) on a phone-sized viewport over a mobile-data-style connection (throttled, or a real phone on mobile data). Record the connection used and how long the page took to become usable.
2. Images: every image must be sized for the web — no multi-megabyte photos straight from a camera, no image displayed at a fraction of its file size. Compress or resize any image over about 300 KB, and confirm it still looks sharp after resizing.
3. Remove render-blocking bloat: no unused apps, widgets, fonts, or scripts loading on pages that do not need them. If a script, font, or embed is not used on a page, it must not load on that page.
4. Aim for: the homepage usable within a few seconds on mobile data, with no blank screen while fonts or scripts load. If a page is slow, name the cause (which image, which script) in the checklist — "it's slow" without a cause is not a finding.
5. Re-run the speed check after every fix. A speed fix that is not re-tested is not a fix.

### Step 9 — 404 page

1. Visit a made-up URL on the site (for example https://example-business.com/this-page-does-not-exist) and confirm a custom 404 page appears — branded like the rest of the site, in plain language ("This page doesn't exist" or similar), with a clear link back to the homepage and a link to the contact page.
2. Confirm the 404 page does NOT show the platform's default error, a blank page, or a server error message.
3. Confirm the 404 page returns a real 404 status (the browser or `scripts/check_site.py` reports it as not found), so search engines do not index it as a real page.
4. Check that broken links found during Step 3 point to real pages or are fixed — the 404 page is a safety net, not a substitute for fixing links.

### Step 10 — Go-live steps (in order) + approval gate

Complete `templates/launch-checklist.md` and `templates/go-live-run-sheet.md` first. Then stop and get the owner's approval for: the filled-in checklist, the run sheet, and the exact launch moment. Launch only after approval.

Run the go-live steps in this order — do not skip ahead, and do not announce before verifying:

1. **Content freeze.** No more content edits from the freeze time the owner approved. Any edit after the freeze goes through the run sheet and needs fresh approval.
2. **Backup.** Take a full backup of the site as it stands (files + content / store export, whichever the platform provides) and confirm the backup file exists and is stored where the owner can reach it. Record where it is.
3. **Final content check.** Re-run the page inventory (Step 3) and the form tests (Step 4) on the staging / pre-live version one last time. Anything found here is fixed before the switch, not after.
4. **DNS / domain switch.** Apply the DNS or domain change exactly as written in the run sheet (owner's registrar / hosting, on the owner's device). One change at a time; confirm each one before the next.
5. **Wait for propagation, then verify live.** Wait for the domain to resolve to the live site, then open the live domain on desktop and on a phone and verify: homepage loads over HTTPS with the padlock, every page in the inventory loads, every form submits and the owner receives it, the 404 page works, and the favicon shows.
6. **Re-run the automated check.** Run `scripts/check_site.py` against the live domain and record the result. Every check must pass before announcing.
7. **Announce.** Only after live verification passes: tell the owner the site is live with the live URL, the tier delivered, the page count, and anything still pending. The owner announces it to customers / social media — Claude does not post the launch announcement without the owner's approval of the exact words.
8. **If anything fails at Step 5 or 6:** stop, roll back using the backup from Step 2 if the live site is broken, tell the owner exactly what failed, and do not announce. A half-live site is worse than a late site.

### Step 11 — After launch (first week)

Use `templates/first-week-check.md`. Do these checks on day 1, day 3, and day 7:

1. **Broken links:** re-check every link in the page inventory. Fix any link that broke in the move and re-verify it live.
2. **Form submissions:** confirm real submissions are arriving (count them, and confirm the owner received each one). A form that worked in testing but receives nothing live is the first thing to investigate.
3. **Analytics:** confirm data is still arriving every day, and record the first week's visitor count. If data stops, the analytics code was lost in the move — reinstall it and re-confirm.
4. **Search:** confirm the site is indexed (search for the business name) and that Search Console shows no new errors.
5. **Speed and mobile:** re-check the homepage on a phone once, after real visitors have used the site.
6. **Fixes:** fix any broken link, wrong price, missing image, or failed form the owner reports, re-verify live after each fix, and record it in the first-week check. Do not change prices, offers, or policies without the owner's approval.
7. **Handover:** at the end of the first week, give the owner the completed checklist, the run sheet, the first-week check, the backup location, and the list of logins they hold (registrar, hosting, analytics, Search Console) — without writing any password into those documents.

## How to run one launch

1. Fill in the brief in `templates/launch-checklist.md` and get the owner to confirm it.
2. Work Steps 2–9 in order. Run `scripts/check_site.py` early (Step 2) and again at go-live (Step 10) — fix every failure it reports; do not launch with a failing check.
3. Fill in `templates/go-live-run-sheet.md`, get the owner's approval at the gate (Step 10), then run the go-live steps in order.
4. Do the first-week checks in `templates/first-week-check.md` on day 1, day 3, and day 7, and hand over the completed documents.
