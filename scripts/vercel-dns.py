#!/usr/bin/env python3
"""Add the Zoho Mail DNS records for haroldsautorepair.com to Vercel DNS.

Idempotent: records that already exist (same type, name and value) are skipped.

Requires:
  VERCEL_TOKEN      Vercel API token (Account Settings → Tokens). Scope: the account/team that owns the domain.
  VERCEL_TEAM_ID    optional, only if the domain lives in a team scope.
Optional:
  ZOHO_DKIM_SELECTOR / ZOHO_DKIM_VALUE   add the DKIM record once Zoho has generated it.
  DMARC_RUA         mailbox for DMARC aggregate reports (default postmaster@haroldsautorepair.com).

Usage:
  python3 scripts/vercel-dns.py            # add verification + MX + SPF (+ DMARC)
  python3 scripts/vercel-dns.py --dry-run  # show what would be added
"""
import json, os, sys, urllib.request, urllib.parse, urllib.error

DOMAIN = "haroldsautorepair.com"
API = "https://api.vercel.com"
TOKEN = os.environ.get("VERCEL_TOKEN")
TEAM = os.environ.get("VERCEL_TEAM_ID")
DRY = "--dry-run" in sys.argv
RUA = os.environ.get("DMARC_RUA", f"postmaster@{DOMAIN}")

# name "" is the apex (shown as "@" in the dashboard)
RECORDS = [
    {"type": "TXT", "name": "", "value": "zoho-verification=zb78393541.zmverify.zoho.com", "ttl": 60},
    {"type": "MX",  "name": "", "value": "mx.zoho.com",  "mxPriority": 10, "ttl": 60},
    {"type": "MX",  "name": "", "value": "mx2.zoho.com", "mxPriority": 20, "ttl": 60},
    {"type": "MX",  "name": "", "value": "mx3.zoho.com", "mxPriority": 50, "ttl": 60},
    {"type": "TXT", "name": "", "value": "v=spf1 include:zohomail.com -all", "ttl": 60},
    {"type": "TXT", "name": "_dmarc", "value": f"v=DMARC1; p=none; rua=mailto:{RUA}; adkim=r; aspf=r", "ttl": 60},
]
if os.environ.get("ZOHO_DKIM_VALUE"):
    sel = os.environ.get("ZOHO_DKIM_SELECTOR", "zmail")
    RECORDS.append({"type": "TXT", "name": f"{sel}._domainkey", "value": os.environ["ZOHO_DKIM_VALUE"], "ttl": 60})

def call(method, path, body=None):
    q = f"?teamId={urllib.parse.quote(TEAM)}" if TEAM else ""
    req = urllib.request.Request(API + path + q, method=method, data=json.dumps(body).encode() if body else None,
                                 headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"{method} {path} -> {e.code}: {e.read().decode()[:400]}")

def main():
    if not TOKEN and not DRY:
        sys.exit("VERCEL_TOKEN is not set. Add it to the environment (never paste it in chat) and re-run.")
    existing = call("GET", f"/v4/domains/{DOMAIN}/records?limit=100").get("records", []) if TOKEN else []
    have = {(r["type"], r.get("name", ""), r["value"]) for r in existing}
    spf = [r for r in existing if r["type"] == "TXT" and r.get("name", "") == "" and r["value"].startswith("v=spf1")]
    print(f"{len(existing)} existing records on {DOMAIN}")
    for r in RECORDS:
        key = (r["type"], r["name"], r["value"])
        label = f'{r["type"]:4} {r["name"] or "@":18} {r["value"]}' + (f' (prio {r["mxPriority"]})' if "mxPriority" in r else "")
        if key in have:
            print("  skip (exists)", label); continue
        if r["value"].startswith("v=spf1") and spf and spf[0]["value"] != r["value"]:
            print(f"  WARNING: an SPF record already exists ({spf[0]['value']}). Merge includes by hand; not adding.", label); continue
        if DRY:
            print("  would add    ", label); continue
        res = call("POST", f"/v2/domains/{DOMAIN}/records", r)
        print("  added        ", label, "->", res.get("uid", res))
    print("done" if not DRY else "dry run complete")

if __name__ == "__main__":
    main()
