# Connecting haroldsautorepair.com to Mitchell 1 — shop-day checklist

Everything the website needs from Mitchell 1 (and a few other accounts) is a handful of links and IDs. They all go into **one file**, `assets/js/config.js`, and the site redeploys itself about a minute after you save. No code changes, no developer needed.

Plan on 30–45 minutes at the shop plus one call to Mitchell 1.

---

## 1. Before you start

Bring or have ready:

- [ ] Admin login to **Manager SE** on the shop computer
- [ ] Login to **SocialCRM** if the shop has it (if nobody knows, it probably doesn't)
- [ ] Mitchell 1 support / sales: **(888) 724-6742** (or your rep's cell)
- [ ] Login to the **Google Business Profile** for "Harold's Quality Auto Repair" (if the previous owner holds it, start the transfer today)
- [ ] GitHub login for `github.com/corbanenns/harolds-auto-repair` (this is where the config file lives)
- [ ] Vercel login (only needed to watch the deploy or if something goes wrong)

---

## 2. Find out what the shop already has (10 min)

On the Manager SE computer:

| Check | Where | Why it matters |
|---|---|---|
| Manager SE version | Help → About | MessageCenter texting needs 7.5+. OneFlow Inspections needs a current version. |
| SocialCRM subscription | Look for an "Insights" or "SocialCRM" button/tab inside Manager SE, or any SocialCRM email in the shop inbox | Book It Now, reminders, review requests and marketing texts all live inside SocialCRM |
| Texting | Is there a MessageCenter / text icon on the Work-In-Progress screen? | Status texts to customers |
| Inspections | Any tablet in the bays? Any "Inspections" or "OneFlow" menu? | Digital inspections with photos |
| Card processor | Look at the card terminal brand, or the last processing statement | Text-to-pay needs 360 Payments (or 1stMile / Global Payments) integrated with Manager SE |
| Shop email | Which address Mitchell 1 sends invoices/notices to | Needed for logins and password resets |

Write the answers down; you'll need them for the call.

---

## 3. The call to Mitchell 1 (15 min)

Say: *"We're the new owners of Harold's Quality Auto Repair in Salem, Oregon, account under (503) 365-9702. We're on Manager SE and want to add online booking, digital inspections and text-to-pay. What do we have today, and what does the bundle cost?"*

Ask for, in this order:

1. **SocialCRM with Book It Now** — online scheduling with real-time availability, synced to the Manager SE schedule and Google Calendar, plus the "Book" button on Google Business Profile. Ask them to turn on **Diagnostics-First Scheduling** and **Incomplete Booking Recovery** (both 2026 features).
   - If the price is too high: ask for the cheaper **Online Appointments** (request-and-approve) instead. Either gives you a link.
2. **OneFlow Inspections** (also called Manager SE Inspections) — the tablet inspection with photos, texted to the customer with approve/decline buttons.
3. **MessageCenter** two-way texting inside Manager SE (may already be included).
4. **360 Payments integration** for Text-to-Pay. They'll hand you to 360 Payments, who will want the current processing statement to quote. Ask about the after-approval financing option too.
5. **SocialCRM texting number**: ask whether the marketing texts go out from a dedicated number and whether it is **10DLC registered**. Give them `https://www.haroldsautorepair.com/privacy` as the SMS terms page if they ask.

Get the rep's direct line and email before hanging up.

---

## 4. Collect the values the website needs

| What | Where to get it | Config key |
|---|---|---|
| **Booking link** | SocialCRM → Book It Now → "Add to website" / share link. For Online Appointments: SocialCRM → Online Appointments → "Website link". (If using AutoOps instead: AutoOps dashboard → Install → link or embed code.) | `bookingUrl` (or `bookingEmbed` if they give you an iframe/script snippet) |
| **Google review link** | Google Business Profile → Home → "Ask for reviews" → copy the short link (looks like `g.page/r/…/review`) | `reviewUrl` |
| **Google rating + count** | Top of the Business Profile | `googleRating`, `googleReviewCount` |
| **Pay page** (optional) | Ask 360 Payments if they offer a hosted "pay my invoice" page. Most shops don't need it; text-to-pay links come from Manager SE. | `payUrl` |
| **Texting number** | The number SocialCRM texts customers from (after 10DLC registration). Until then leave the shop line. | `smsNumber` |
| **Form endpoint** | See section 5. | `formEndpoint` |

---

## 5. Where website forms should go (10 min, can be done from any computer)

The site has six forms (appointment request, contact, maintenance club, first-visit coupon, fleet, corporate, manager feedback). They all post to one address. Pick one:

**Option A — Formspree (fastest, free tier is enough)**
1. Go to formspree.io → sign up with the shop email → New Form → name it "Harold's website".
2. Set the notification email to the service desk mailbox (e.g. `service@haroldsautorepair.com` once Zoho mailboxes exist).
3. Copy the endpoint, which looks like `https://formspree.io/f/abcdwxyz`.
4. In Formspree settings turn on "Accept JSON" (it's on by default on current plans).

**Option B — SocialCRM lead capture**: ask the rep if SocialCRM has a web-form endpoint that creates leads. If yes, use that URL instead; leads then land in Manager SE directly.

Every submission arrives with a `form` field saying which form it was, the page it came from, and `lang` (en/es).

---

## 6. Put the values into the website (5 min)

1. Open `https://github.com/corbanenns/harolds-auto-repair/blob/main/assets/js/config.js`
2. Click the **pencil** (Edit) icon.
3. Paste each value between the quotes. Example:
   ```js
   bookingUrl: "https://bookitnow.socialcrm.com/harolds-quality-auto-repair",
   reviewUrl: "https://g.page/r/XXXXXXXX/review",
   googleRating: 4.7,
   googleReviewCount: 180,
   formEndpoint: "https://formspree.io/f/abcdwxyz",
   smsNumber: "503-555-0100",
   ```
   Leave anything you don't have yet as `""` or `null`. The site hides or falls back for empty values.
4. Scroll down, choose **Commit directly to the main branch**, click **Commit changes**.
5. Wait about one minute. Vercel builds and publishes automatically.

Other values in the same file you may want to set now: `hours` (confirm Friday), `firstVisitOffer` ("$20 off your first visit"), `smsKeyword` ("SAVE" — must match the keyword set up in SocialCRM).

---

## 7. Test it (5 min, use your phone)

- [ ] `www.haroldsautorepair.com` → **Book Online** opens the scheduler (or the request form if no link yet)
- [ ] Submit the contact form → email arrives at the service desk within a minute
- [ ] `/es` → Reservar en línea works the same way
- [ ] `/review` → "Review us on Google" opens the review box
- [ ] Text **SAVE** to the shop number → auto-reply with the coupon (only once SocialCRM has the keyword set up)
- [ ] Tap the phone number on your phone → it dials

---

## 8. Staff workflow once the tools are on (print this for the counter)

**Every vehicle:**
1. Check in → MessageCenter template **"Checked in"** → send.
2. Tech runs the OneFlow inspection on the tablet with photos → send report to customer.
3. Customer approves/declines on their phone. Declined items stay on the vehicle record.
4. Work done → template **"Ready + pay link"** (360 Payments) → send.
5. RO closed → SocialCRM sends thank-you + review link automatically.

**Rules:** one public review link for everyone, never filtered by rating. No marketing texts from personal phones. Every customer who opts in gets the same reminder cadence.

---

## 9. Other accounts to set up this week

| Account | Why | Then paste into config.js |
|---|---|---|
| Google Business Profile (transfer to new owner, update hours, link `www.haroldsautorepair.com`, enable Book It Now button) | #1 local ranking factor | `reviewUrl`, `googleRating` |
| Google Search Console + Bing Webmaster Tools → submit `https://www.haroldsautorepair.com/sitemap.xml` | Get indexed; Bing feeds ChatGPT | — |
| Google Analytics 4 property | Measure visits and calls | `ga4MeasurementId` |
| Google Ads account → conversion actions for call / text / book / form | Only when ready to spend | `googleAdsId`, `googleAdsConversions` |
| Meta Business → Pixel | Facebook/Instagram ads | `metaPixelId` |
| Zoho Mail mailboxes (DNS is done) → create `service@`, `office@`, `postmaster@` | Email on the new domain; DMARC reports go to postmaster | — |
| Update WhirLocal, BBB, Yelp listings to the new domain and phone | Consistent name/address/phone | — |
| **Vercel: revoke the API token** that was shared in chat (Account Settings → Tokens) | Security | — |

---

## 10. If something looks wrong

- **Site didn't update after the commit**: vercel.com → harolds-auto-repair → Deployments. A red build means a typo in config.js (usually a missing comma or quote). Open the file on GitHub, fix, commit again.
- **Form says "Online forms aren't connected yet"**: `formEndpoint` is empty or misspelled.
- **Book Online goes to the request form**: `bookingUrl` is empty. That's fine until Mitchell 1 turns on Book It Now.
- **Reviews button is hidden**: `reviewUrl` is empty.
- **Need to change page text**: edit files under `src/pages/`, then run `python3 build.py` locally and commit the result (details in README.md). For small text changes, ask Claude in a new session with this repo attached.

Reference: `docs/website-roadmap.md` (strategy and Mitchell 1 research), `docs/dns-zoho-mail.md` (email DNS), `README.md` (every config key).
