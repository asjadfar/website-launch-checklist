#!/usr/bin/env python3
"""Public pre-launch checks for a business website.

Checks only what any visitor can see — no login, no credentials, no
account access needed:

  * homepage reachable over HTTPS (status 200)
  * SSL certificate valid (hostname match + not expired)
  * <title> and meta description present on the homepage and on each
    key page given with --pages
  * sitemap reachable (tries /sitemap.xml, then /sitemap_index.xml)
  * favicon present (tries /favicon.ico and the <link rel="icon"> in
    the homepage HTML)
  * a made-up URL returns a 404 status (the custom 404 page exists)

Uses only the Python standard library, so it runs anywhere Python 3
is installed. It does NOT test forms, confirm analytics is receiving
data, check login-only pages, or judge whether the content is correct
— those are manual checks in the skill (SKILL.md Steps 3-6).

Usage:
    python3 check_site.py https://example-business.com
    python3 check_site.py https://example-business.com --pages /about /services /contact
    python3 check_site.py https://example-business.com --output launch-check.json

Exit code 0 = every check passed. Exit code 1 = at least one failed.
"""

import argparse
import html.parser
import json
import re
import socket
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

TIMEOUT = 15
USER_AGENT = "website-launch-checklist/1.0 (pre-launch check)"


class _HeadParser(html.parser.HTMLParser):
    """Collects title, meta description, and icon links from a page."""

    def __init__(self):
        super().__init__()
        self.title = ""
        self._in_title = False
        self.meta_description = ""
        self.icon_hrefs = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "meta":
            if attrs.get("name", "").lower() == "description":
                self.meta_description = attrs.get("content", "").strip()
        elif tag == "link":
            rel = attrs.get("rel", "").lower()
            if "icon" in rel and attrs.get("href"):
                self.icon_hrefs.append(attrs["href"])

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data.strip()


def fetch(url):
    """GET a URL. Returns (status, final_url, body_text, headers).

    Raises urllib.error.URLError / HTTPError on failure; HTTPError
    still carries its status code, so callers can read it.
    """
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            body = response.read().decode("utf-8", errors="replace")
            return response.status, response.geturl(), body, response.headers
    except urllib.error.HTTPError as error:
        body = ""
        try:
            body = error.read().decode("utf-8", errors="replace")
        except Exception:
            pass
        return error.code, error.geturl() or url, body, error.headers


def check_ssl(hostname):
    """Check the TLS certificate: hostname match + not expired.

    Returns (ok, detail). A failure here is a launch blocker.

    The direct socket check gives the expiry date. On networks where a
    direct port-443 connection is blocked (for example a sandbox proxy),
    it falls back to verifying through an HTTPS fetch — urllib validates
    the certificate on every HTTPS request, so a successful fetch proves
    the certificate is valid, even though the expiry date cannot be read
    that way.
    """
    context = ssl.create_default_context()
    try:
        with socket.create_connection((hostname, 443), timeout=TIMEOUT) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as secure:
                cert = secure.getpeercert()
    except ssl.SSLCertVerificationError as error:
        return False, "certificate verification failed: %s" % error
    except (socket.timeout, OSError):
        # Direct connection blocked (proxy / sandbox). Fall back to an
        # HTTPS fetch, which still validates the certificate.
        try:
            fetch("https://%s/" % hostname)
        except ssl.SSLCertVerificationError as error:
            return False, "certificate verification failed: %s" % error
        except Exception as error:
            return False, "could not verify certificate from this network: %s" % error
        return True, "valid (verified via HTTPS fetch; expiry not readable on this network)"

    expires = cert.get("notAfter")
    if not expires:
        return False, "certificate has no expiry date"
    expiry = datetime.strptime(expires, "%b %d %H:%M:%S %Y %Z").replace(
        tzinfo=timezone.utc
    )
    now = datetime.now(timezone.utc)
    if expiry <= now:
        return False, "certificate expired on %s" % expires
    days_left = (expiry - now).days
    return True, "valid, expires %s (%d days left)" % (expires, days_left)


def check_page(url):
    """Check one page: reachable (200), title present, meta present.

    Returns (ok, detail, title, meta_description).
    """
    try:
        status, _final, body, _headers = fetch(url)
    except urllib.error.URLError as error:
        return False, "unreachable: %s" % error.reason, "", ""
    except (socket.timeout, OSError) as error:
        return False, "unreachable: %s" % error, "", ""

    if status != 200:
        return False, "HTTP %s (expected 200)" % status, "", ""

    parser = _HeadParser()
    parser.feed(body)
    problems = []
    if not parser.title:
        problems.append("missing <title>")
    elif len(parser.title) > 60:
        problems.append("title is %d characters (aim under 60)" % len(parser.title))
    if not parser.meta_description:
        problems.append("missing meta description")
    elif len(parser.meta_description) > 160:
        problems.append(
            "meta description is %d characters (aim under 160)"
            % len(parser.meta_description)
        )
    if problems:
        return False, "; ".join(problems), parser.title, parser.meta_description
    return True, "title: %r" % parser.title, parser.title, parser.meta_description


def check_url_exists(url):
    """True if the URL answers 200. Used for sitemap and favicon."""
    try:
        status, _final, _body, _headers = fetch(url)
    except (urllib.error.URLError, socket.timeout, OSError):
        return False, "unreachable"
    if status == 200:
        return True, "HTTP 200"
    return False, "HTTP %s" % status


def run_checks(base_url, pages):
    """Run every check. Returns a list of (name, ok, detail) results."""
    parsed = urllib.parse.urlparse(base_url)
    if parsed.scheme != "https":
        print("Warning: base URL is not https:// — the site must launch on HTTPS.",
              file=sys.stderr)
    base = base_url.rstrip("/")
    hostname = parsed.hostname or ""
    results = []

    # 1. Homepage reachable.
    ok, detail, _t, _m = check_page(base + "/")
    results.append(("Homepage reachable (HTTP 200)", ok, detail))

    # 2. SSL certificate.
    if hostname:
        ok, detail = check_ssl(hostname)
        results.append(("SSL certificate valid", ok, detail))
    else:
        results.append(("SSL certificate valid", False, "no hostname in URL"))

    # 3. Title + meta on each key page.
    for page in pages:
        page_url = base + (page if page.startswith("/") else "/" + page)
        ok, detail, _t, _m = check_page(page_url)
        results.append(("Page %s — title + meta description" % page, ok, detail))

    # 4. Sitemap.
    sitemap_ok, sitemap_detail = False, ""
    for candidate in ("/sitemap.xml", "/sitemap_index.xml"):
        ok, detail = check_url_exists(base + candidate)
        if ok:
            sitemap_ok, sitemap_detail = True, "%s — %s" % (candidate, detail)
            break
        sitemap_detail = "%s — %s" % (candidate, detail)
    results.append(("Sitemap reachable", sitemap_ok, sitemap_detail))

    # 5. Favicon: /favicon.ico first, then the <link rel="icon"> href.
    favicon_ok, favicon_detail = check_url_exists(base + "/favicon.ico")
    if not favicon_ok:
        try:
            _status, _final, body, _headers = fetch(base + "/")
            parser = _HeadParser()
            parser.feed(body)
            for href in parser.icon_hrefs:
                if href.startswith("data:"):
                    # Inline icon embedded in the page — that is a favicon.
                    favicon_ok, favicon_detail = True, "inline data: icon in page"
                    break
                icon_url = urllib.parse.urljoin(base + "/", href)
                ok, detail = check_url_exists(icon_url)
                if ok:
                    favicon_ok, favicon_detail = True, "%s — %s" % (href, detail)
                    break
                favicon_detail = "%s — %s" % (href, detail)
        except (urllib.error.URLError, socket.timeout, OSError):
            favicon_detail = "could not re-read homepage to find icon link"
    results.append(("Favicon present", favicon_ok, favicon_detail))

    # 6. Made-up URL returns 404 (custom 404 page exists).
    test_url = base + "/this-page-does-not-exist-launch-check"
    try:
        status, _final, _body, _headers = fetch(test_url)
        if status == 404:
            results.append(("404 page (missing URL returns 404)", True,
                            "HTTP 404 as expected"))
        else:
            results.append(("404 page (missing URL returns 404)", False,
                            "HTTP %s (expected 404)" % status))
    except urllib.error.URLError as error:
        results.append(("404 page (missing URL returns 404)", False,
                        "unreachable: %s" % error.reason))
    except (socket.timeout, OSError) as error:
        results.append(("404 page (missing URL returns 404)", False,
                        "unreachable: %s" % error))

    return results


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Public pre-launch checks for a business website "
                    "(standard library only, no login needed)."
    )
    parser.add_argument("url", help="site base URL, e.g. https://example-business.com")
    parser.add_argument("--pages", nargs="*", default=[],
                        help="key page paths to check for title + meta, "
                             "e.g. --pages /about /services /contact")
    parser.add_argument("--output", help="optional JSON file to write results to")
    args = parser.parse_args(argv)

    results = run_checks(args.url, args.pages)

    passed = sum(1 for _name, ok, _detail in results if ok)
    failed = len(results) - passed

    print("Launch check: %s" % args.url)
    print("Checked: %s" % datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"))
    print("")
    for name, ok, detail in results:
        mark = "PASS" if ok else "FAIL"
        print("[%s] %s — %s" % (mark, name, detail))
    print("")
    print("%d passed, %d failed, %d total" % (passed, failed, len(results)))
    if failed:
        print("Fix every FAIL before launch. A failed SSL or homepage check "
              "is a launch blocker.")

    if args.output:
        data = {
            "url": args.url,
            "checked_at_utc": datetime.now(timezone.utc).isoformat(),
            "passed": passed,
            "failed": failed,
            "results": [
                {"check": name, "ok": ok, "detail": detail}
                for name, ok, detail in results
            ],
        }
        with open(args.output, "w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2)
        print("Results written to %s" % args.output)

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
