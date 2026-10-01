# DNS records for Zoho Mail on haroldsautorepair.com

The domain's nameservers are `ns1.vercel-dns.com` / `ns2.vercel-dns.com`, so all records are managed in
**Vercel → Domains → haroldsautorepair.com → DNS Records** (or with `scripts/vercel-dns.py`).

Current state (checked 2026-10-01): A records for apex and www exist (the website). No MX, no TXT, no DMARC.

## Records to add

| # | Type | Name / Host | Value | Priority | When |
|---|------|-------------|-------|----------|------|
| 1 | TXT | `@` | `zoho-verification=zb78393541.zmverify.zoho.com` | — | Now (domain verification) |
| 2 | MX | `@` | `mx.zoho.com` | 10 | Now |
| 3 | MX | `@` | `mx2.zoho.com` | 20 | Now |
| 4 | MX | `@` | `mx3.zoho.com` | 50 | Now |
| 5 | TXT | `@` | `v=spf1 include:zohomail.com -all` | — | Now |
| 6 | TXT | `<selector>._domainkey` (e.g. `zmail._domainkey`) | *(public key Zoho generates)* | — | After verification: Admin Console → Domains → Email Configuration → DKIM → Add selector (use `zmail`) → copy the TXT value |
| 7 | TXT | `_dmarc` | `v=DMARC1; p=none; rua=mailto:postmaster@haroldsautorepair.com; adkim=r; aspf=r` | — | After DKIM is live |

Notes
- In the Vercel dashboard the apex name is `@`; in the API it is an empty string. TTL 60 is fine.
- `scripts/vercel-dns.py` adds rows 1–5 and 7 in one go (and row 6 when `ZOHO_DKIM_VALUE` is set). It needs `VERCEL_TOKEN` in the environment.
- A domain may have **only one** SPF record. Record 5 is that record; if another service later needs to send
  as this domain (e.g. a form backend or SocialCRM via your domain), add its `include:` to the same string.
- Zoho shows the MX hostnames for your data center under Admin Console → Tools & Configurations. The values above
  are for the US (.com) data center; if the console shows different hostnames, use the console's.
- DMARC starts at `p=none` (monitor only). After a few weeks of clean reports, move to `p=quarantine`.
- Change the DMARC `rua` mailbox to whichever Zoho mailbox should receive aggregate reports.
- Zoho's console may also offer an optional CNAME for a custom webmail URL (e.g. `mail.haroldsautorepair.com → business.zoho.com`). Not required.

## Verify after adding

```bash
# any machine with dig:
dig +short MX haroldsautorepair.com
dig +short TXT haroldsautorepair.com
dig +short TXT zmail._domainkey.haroldsautorepair.com
```
Then click **Verify** in Zoho (TXT), then **Verify MX**, **Verify SPF**, **Verify DKIM**.
