# Harold's Quality Auto Repair – Website

Static, bilingual (English / Spanish) multi-page site for Harold's Quality Auto Repair Inc, West Salem, Oregon, at **www.haroldsautorepair.com**. Built to pair with Mitchell 1 Manager SE add-ons (online booking, digital inspections, text-to-pay, SocialCRM). No framework, no build step on Vercel.

See `docs/website-roadmap.md` for the strategy behind the site and the Mitchell 1 integration research.

## Pages

| Path | Purpose |
|---|---|
| `/` | Home: "See what we see" DVI pitch, services, text-update convenience, reviews, club + first-visit offer, about, visit |
| `/book` | Booking. Shows the live scheduler when configured, otherwise a diagnostics-first appointment request form |
| `/inspections` | How digital inspections work, sample report, FAQ |
| `/pay` | Pay-by-text explainer, financing, warranty |
| `/maintenance-club` | Annual membership offer + signup form |
| `/specials` | First-visit coupon by SMS (with consent language), seasonal checks |
| `/fleet` | Fleet accounts + quote form |
| `/corporate` | Corporate vehicle accounts, Employee Car Care Program, pickup & delivery + inquiry form |
| `/review` | One public review link for everyone + direct-to-manager form (not gated) |
| `/about` | History, facility, warranty (`#warranty`), financing (`#financing`) |
| `/contact` | Address, hours, map, message form |
| `/privacy` | Privacy policy and SMS program terms (required for 10DLC registration) |
| `/services` | Overview |
| `/services/*` | Oil change, brakes, tires-alignment, diagnostics, engine-transmission, ac-heating, exhaust |
| `/es/...` | Spanish version of every page above, same slugs (`/es/book`, `/es/services/brakes`, …) |

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
| `ga4MeasurementId` | `G-…` | Google Analytics 4 → Admin → Data streams |
| `googleAdsId`, `googleAdsConversions` | `AW-…` plus one conversion label per action (call, text, book, form) | Google Ads → Tools → Conversions |
| `metaPixelId` | Pixel ID | Meta Events Manager |

With any of the tracking IDs set, the site loads the official tag and reports `call_click`, `text_click`, `book_click` and `form_submit` (with the form name) to GA4, fires the matching Google Ads conversion when a label is set, and sends Meta `Contact`, `Schedule` and `Lead` events. Nothing loads when the IDs are empty. Every event is also dispatched as a `harolds:track` DOM event for call-tracking or other scripts.

Until `formEndpoint` is set, forms show a "call or text us" notice instead of pretending to send. Until `bookingUrl` is set, buttons go to the request form.

Form payloads look like `{"form":"appointment-request","name":...,"phone":...,"vehicle_year":...,"service":...,"symptoms":...,"sms_consent":"yes","page":"/book","submitted_at":"..."}`. Form names: `appointment-request`, `contact`, `maintenance-club`, `first-visit-coupon`, `fleet-inquiry`, `manager-feedback`.

## SEO

Every page has a unique title, description, canonical and hreflang pair, and `sitemap.xml` / `robots.txt` are generated. The build adds JSON-LD automatically: `AutoRepair` on the home pages, `Service` on service pages, `FAQPage` wherever a page has `<details>` FAQs, and `BreadcrumbList` on interior pages. `llms.txt` at the root summarises the business for AI crawlers; update it when services or hours change.

Still to do outside the code: claim and update the Google Business Profile (link it to this domain, match name, address, phone and hours), set up Google Search Console and Bing Webmaster Tools and submit the sitemap, and update the WhirLocal, BBB and Yelp listings to the new domain.

## Editing pages

English sources are in `src/pages/`, Spanish in `src/pages/es/`. Each is wrapped by `src/layout.html` (header, footer, top bar, mobile action bar), whose labels come from the `STRINGS` table in `build.py` for each language. After editing, run:

```bash
python3 src/gen_services.py   # only if you changed service copy (data lives in that file, both languages)
python3 build.py
```

This rewrites the HTML in the repo root, `services/`, `es/` and `es/services/`, plus `sitemap.xml` and `robots.txt`. Commit the generated files; Vercel serves them as-is (`vercel.json` enables clean URLs so `/book` serves `book.html`). Every page carries `hreflang` links to its counterpart, and the language switch sits in the top bar and the mobile menu.

Each page source starts with a JSON comment holding its `title`, `description`, `path` and optional `jsonld` structured data.

## Photos

`assets/img/` holds licensed stock placeholders (sources in `assets/img/SOURCES.md`). Replace them with real photos of the shop using the same filenames and nothing else needs to change. Keep them around 1600px wide and under 250 KB.

## Still to do before launch

- Replace the stock placeholder photos with real photos of the shop, bays and team (see `assets/img/SOURCES.md`).
- Confirm hours, the "new ownership in 2026" line on `/` and `/about`, Maintenance Club pricing and the first-visit offer amount.
- `www.haroldsautorepair.com` is on Vercel. Also redirect the old `haroldsqualityautorepair.com` (currently a WhirLocal profile) to it, and set the apex `haroldsautorepair.com` to redirect to `www`.
- Get the Google Business Profile "Book" button enabled through Book It Now so Maps users can schedule without visiting the site.
- Register the texting number for 10DLC through the texting vendor, using `/privacy` as the program terms page.

## Deploy to Vercel

1. Import this repo at vercel.com → Add New → Project. Framework preset: Other. No build command, output directory `.`.
2. Under Project → Settings → Domains confirm `www.haroldsautorepair.com` is the primary domain and `haroldsautorepair.com` redirects to it.
3. Every push to `main` redeploys.
