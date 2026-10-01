# Harold's Quality Auto Repair – Website

Static, multi-page site for Harold's Quality Auto Repair Inc, West Salem, Oregon. Built to pair with Mitchell 1 Manager SE add-ons (online booking, digital inspections, text-to-pay, SocialCRM). No framework, no build step on Vercel.

See `docs/website-roadmap.md` for the strategy behind the site and the Mitchell 1 integration research.

## Pages

| Path | Purpose |
|---|---|
| `/` | Home: "See what we see" DVI pitch, services, text-update convenience, reviews, club + first-visit offer, about, visit |
| `/book` | Booking. Shows the live scheduler when configured, otherwise a diagnostics-first appointment request form |
| `/inspections` | How digital inspections work, sample report, FAQ |
| `/pay` | Pay-by-text explainer, after-hours pickup, financing, warranty |
| `/maintenance-club` | Annual membership offer + signup form |
| `/specials` | First-visit coupon by SMS (with consent language), seasonal checks |
| `/fleet` | Fleet accounts + quote form |
| `/review` | One public review link for everyone + direct-to-manager form (not gated) |
| `/about` | History, facility, warranty (`#warranty`), financing (`#financing`) |
| `/contact` | Address, hours, map, message form |
| `/privacy` | Privacy policy and SMS program terms (required for 10DLC registration) |
| `/services` | Overview |
| `/services/*` | Oil change, brakes, tires-alignment, diagnostics, engine-transmission, ac-heating, exhaust, marine |

## Connecting Mitchell 1 and other services

Everything integration-related lives in **`assets/js/config.js`**. Edit values there; no page edits needed.

| Config key | What to paste | Where it comes from |
|---|---|---|
| `bookingUrl` | Scheduler link | SocialCRM Book It Now, SocialCRM Online Appointments, or AutoOps. Every "Book Online" button opens it. |
| `bookingEmbed` | Iframe/script snippet | Same vendors, if you'd rather embed the scheduler on `/book` than link out |
| `payUrl` | Hosted payment page URL | 360 Payments / 1stMile / Global Payments, if offered. Text-to-pay links from Manager SE don't need this. |
| `reviewUrl` | Google "write a review" short link | Google Business Profile → Ask for reviews. Or the SureCritic link from SocialCRM. |
| `googleRating`, `googleReviewCount` | Numbers | Google Business Profile. Leave `null` to hide. |
| `formEndpoint` | URL that accepts a JSON POST | Formspree / Basin / a Vercel function, or a SocialCRM lead endpoint. All five forms post here with a `form` field naming which one. |
| `smsNumber` | 10DLC-registered texting number | Issued by SocialCRM or whichever platform sends marketing texts |
| `smsKeyword`, `firstVisitOffer` | Keyword and offer text | Must match the auto-reply configured in the texting platform |
| `hours`, `mapEmbed` | | Verify Friday hours against the shop |

Until `formEndpoint` is set, forms show a "call or text us" notice instead of pretending to send. Until `bookingUrl` is set, buttons go to the request form.

Form payloads look like `{"form":"appointment-request","name":...,"phone":...,"vehicle_year":...,"service":...,"symptoms":...,"sms_consent":"yes","page":"/book","submitted_at":"..."}`. Form names: `appointment-request`, `contact`, `maintenance-club`, `first-visit-coupon`, `fleet-inquiry`, `manager-feedback`.

## Editing pages

Sources are in `src/pages/` (one file per page, wrapped by `src/layout.html` which holds the header, footer and mobile action bar). After editing, run:

```bash
python3 build.py
```

This rewrites the HTML files in the repo root and `services/`, plus `sitemap.xml` and `robots.txt`. Commit the generated files; Vercel serves them as-is (`vercel.json` enables clean URLs so `/book` serves `book.html`).

Each page source starts with a JSON comment holding its `title`, `description`, `path` and optional `jsonld` structured data.

## Still to do before launch

- Replace the stock-free hero and about sections with real photos of the shop, bays and team (`assets/img/`).
- Confirm hours, the "new ownership in 2026" line on `/` and `/about`, Maintenance Club pricing and the first-visit offer amount.
- Point `haroldsqualityautorepair.com` at Vercel (it currently redirects to the WhirLocal profile).
- Get the Google Business Profile "Book" button enabled through Book It Now so Maps users can schedule without visiting the site.
- Register the texting number for 10DLC through the texting vendor, using `/privacy` as the program terms page.

## Deploy to Vercel

1. Import this repo at vercel.com → Add New → Project. Framework preset: Other. No build command, output directory `.`.
2. Add the custom domain under Project → Settings → Domains and update DNS at the registrar.
3. Every push to `main` redeploys.
