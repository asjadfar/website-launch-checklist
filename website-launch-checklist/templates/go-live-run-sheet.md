# Go-Live Run Sheet

> One copy per launch. Fill in every [bracketed] field before the launch
> day. Run the steps in order — do not skip ahead, and do not announce
> before live verification passes. If a step fails, stop at that step,
> write down what failed, and tell the owner before doing anything else.

## Launch details

- **Business name:**
- **Website address (domain):** https://
- **Tier:** Basic (1 page) / Standard (up to 5 pages) / Premium (up to 10 pages)
- **Launch date and time (owner-approved):**
- **Run-sheet owner (who runs the steps):**
- **Owner contact for approvals on launch day (phone / WhatsApp):**
- **Hosting / registrar login holder:** owner, on their own device
- **Backup location (where the backup will be stored):**

## Approval gate (before Step 1)

- **Filled-in launch checklist approved:** [ ] Yes — owner name / date:
- **This run sheet approved:** [ ] Yes — owner name / date:
- **Exact launch moment approved:** [ ] Yes — date / time:

Do NOT start Step 1 if any box above is unticked.

## Step 1 — Content freeze

- **Freeze time (owner-approved):**
- **Freeze announced to everyone who edits the site:** [ ] Yes — who was told:
- **Edits after this time:** only through this run sheet, with fresh owner approval.

| Time | Done | Note |
|---|---|---|
| | [ ] | Content freeze applied — no more edits |

## Step 2 — Backup

- **What was backed up:** [ ] Site files / content export [ ] Store / product export (if the site has one) [ ] Other:
- **Backup file name / location:**
- **Backup confirmed to exist and open:** [ ] Yes — checked by / time:
- **Owner can reach the backup:** [ ] Yes — where:

| Time | Done | Note |
|---|---|---|
| | [ ] | Backup taken and confirmed |

## Step 3 — Final content check (pre-live version)

- [ ] Page inventory re-checked (every page loads, no placeholder text)
- [ ] Every form re-tested (submit, confirmation shown, owner received it)
- [ ] Prices, phone, email, opening hours match the brief
- [ ] Automated check run on the pre-live URL: `python3 scripts/check_site.py https://` — result: ___ passed / ___ failed — date:
- **Problems found in this step (fix before the switch, not after):**

| Time | Done | Note |
|---|---|---|
| | [ ] | Final content check complete — no open problems |

## Step 4 — DNS / domain switch

Write down the exact change BEFORE applying it. One change at a time; confirm each one before the next. A wrong DNS change can take the live site down.

| # | Exact change (record + old value → new value) | Applied by | Time | Confirmed |
|---|---|---|---|---|
| 1 | | | | [ ] |
| 2 | | | | [ ] |
| 3 | | | | [ ] |

- **Registrar / hosting panel used:** ___ (owner signed in on their own device)
- **No other DNS, redirect, or hosting setting changed:** [ ] Yes

## Step 5 — Wait for propagation, then verify live

- **Propagation wait started:** ___ — **Live domain first resolved:** ___
- **Checked on desktop:** [ ] Yes — **Checked on a phone:** [ ] Yes — phone / viewport:
- [ ] Homepage loads on https:// with the padlock, no warning
- [ ] Every page in the inventory loads on the live domain
- [ ] Every form submits on the live domain and the owner receives it
- [ ] 404 page works on the live domain (made-up URL shows the custom 404 page)
- [ ] Favicon shows in the browser tab
- [ ] No mixed-content warning on any page

**Live verification result:** [ ] PASS — all of the above checked / [ ] FAIL — see below

**If FAIL — what failed, on which page, and what was done:**

- **Rolled back using the Step 2 backup:** [ ] Yes / [ ] No — reason:
- **Owner told exactly what failed:** [ ] Yes — time:

## Step 6 — Re-run the automated check (live domain)

- **Command:** `python3 scripts/check_site.py https:// --pages /about /services /contact`
- **Run at:** ___ — **Result:** ___ passed / ___ failed
- **Failures (if any) and how each was fixed + re-tested:**

| Time | Done | Note |
|---|---|---|
| | [ ] | Automated check passes on the live domain |

## Step 7 — Announce

Announce ONLY after Step 5 and Step 6 both pass.

- **Owner told the site is live:** [ ] Yes — time:
- **Live URL given to the owner:** https://
- **Tier delivered:** Basic / Standard / Premium — **Pages live:** ___
- **Still pending (if anything):**
- **Launch announcement to customers / social media:** [ ] Owner will post it / [ ] Approved words for Claude to post: "___"
- **Announcement posted:** [ ] Yes — time / where:

## Sign-off

- **Launched by:** ___ — **Date / time live:**
- **Owner sign-off:** [ ] Site is live and accepted — name / date:
