# Harold's Quality Auto Repair – Website Evaluation & Roadmap

Brainstorm document, October 2026. Covers (1) what the current mockup does and doesn't do, (2) what Mitchell 1 Manager SE actually supports for online booking, payments and inspections, and (3) a tiered plan for a cutting-edge West Salem shop website.

---

## 1. Where the mockup stands today

The repo is a single static `index.html` (about 1,000 lines, inline CSS and JS) intended for Vercel. It looks good and is mobile-friendly, but it is a brochure, not a tool.

**What works**
- Clean hero, About, Services (6 cards), Why Choose Us, testimonials, contact info, hours, Google Map, click-to-call.
- Mobile nav, smooth scroll, scroll animations, back-to-top.
- Basic SEO meta tags.

**Gaps and problems found**
| Area | Issue |
|---|---|
| Contact form | Does nothing. Submit shows a browser `alert()` and resets. No email, no SMS, no CRM. Any lead submitted today is lost. |
| Booking | None. Only CTAs are "Get a Quote" (dead form) and "Call Now". |
| Payments | None. |
| Reviews | Three testimonials attributed to "Satisfied Customer" / "Happy Client". No names, no star rating, no link to Google. Reads as fake even if real. |
| Logo | Hotlinked from `static.whirlocal.io`. If WhirLocal removes it, the header breaks. |
| Map embed | The place ID in the iframe URL looks like a placeholder (`0x4c0f8c8c8c8c8c8c`). Needs a real embed generated from Google Maps. |
| Hours | Site says Mon–Fri 7–5. Public listings show Friday 7–6 in one place. Confirm the real hours and make the site the source of truth. |
| Services | Only 6 generic cards. Public listings say the shop also does tires, alignment, custom exhaust, fleet and marine. None of that is on the site. "R-12" A/C is a 1990s reference. |
| "29+ years" | Hardcoded. Will be wrong next year. |
| SEO | Title and copy say "Salem". The shop is in West Salem and that phrase is what neighbours search. No `schema.org/AutoRepair` structured data. |
| Domain | New site launches on `www.haroldsautorepair.com` (purchased, on Vercel). The old `haroldsqualityautorepair.com` currently 301-redirects to a WhirLocal directory profile (33 reviews, 4.2★) and should be pointed at the new site. |
| Financing / warranty | 1yr/12k warranty is mentioned in passing. No financing info at all, which matters for $1,500+ repairs. |

---

## 2. What Mitchell 1 actually supports

The short version: **every feature you asked about exists, and all of it is bought from Mitchell 1 or an approved partner and embedded in the website. None of it is custom-built.** Mitchell 1 has no self-serve API. Its integration program is gated to approved vendors (shop management, CRM, parts, marketing platforms) and requires an application, a review and a signed partner agreement. An individual shop cannot write code against Manager SE.

### Online booking – yes, two options from Mitchell 1 plus third parties

**SocialCRM Book It Now** (premium add-on inside SocialCRM, requires Manager SE)
- Customer picks a service, sees **real-time availability**, picks a date/time, adds it to their calendar.
- Syncs with the **Manager SE schedule and Google Calendar**.
- Puts a "Book" button on the **Google Business Profile** and on the shop website.
- Optional: show pricing on all / selected / recommended services; suggest add-on maintenance during booking.
- May 2026 additions: **Diagnostics-First Scheduling** (customer describes the problem instead of guessing a service) and **Incomplete Booking Recovery** (auto text to people who abandon the booking).
- Appointment reminder emails/texts 5 days before and morning-of, with confirm / reschedule links.

**SocialCRM Online Appointments** (older, request-based)
- Customer submits a request from the website; it lands in Manager SE as an alert; shop accepts or declines; customer gets a text/email confirmation. No live availability. Cheaper and lower-risk if you'd rather approve every slot by hand.

**Third-party schedulers that integrate with Manager SE**
- **AutoOps (by Steer)**: real-time availability, pushes appointments into the Manager SE calendar, 50+ customisation settings. Strong option if you don't want the full SocialCRM bundle.
- Also integrated with Manager SE: AutoVitals, Kukui, Autoflow, AutoLeap, Broadly, PartsTech.

### "Digital calendar of which tech is on what" – that's Manager SE itself
Manager SE already has the scheduler and work-in-progress board. Technician dispatch is internal shop data and should **never** be on the public website. The website's job is to feed appointments *into* that calendar, which Book It Now or AutoOps does. The Google Calendar sync from Book It Now gives staff a phone-friendly view.

### Paying invoices online – yes, via text-to-pay
- **360 Payments** integration (announced March 2025): **Text-to-Pay** links sent from Manager SE, after-hours vehicle pickup, digital signatures, consumer financing, receipts + signed RO merged into one digital record. Full PCI compliance handled by the processor.
- Also integrated: **1stMile** (financing and loyalty), **Global Payments**.
- Important nuance: there is **no customer-login portal** where someone types an invoice number into your website and pays. The model is push, not pull: the shop sends a secure link by text/email at the moment the invoice is ready. The website's role is a "Pay My Invoice" page that explains this, with a "Didn't get your link? Text us" fallback.

### Digital vehicle inspections – yes
- **Manager SE OneFlow Inspections**: tech does the multi-point inspection on a tablet with photos/video and annotations; the customer gets a **branded report by text/email** and approves or declines each line item in a secure **Online Authorization Portal**. Approved items flow straight into the estimate.
- This is the single biggest trust feature a shop can advertise. The website should explain it with a screenshot.

### Pricing
Mitchell 1 publishes no prices. Third-party reports: Manager SE from roughly $179/mo; one shop reported under $500/mo for management + inspections + texting + repair info + CRM bundled. SocialCRM and Book It Now are quoted separately. Call (888) 724-6742 or your rep.

---

## 3. Recommended roadmap

### Tier 1 – Fix the fundamentals (no Mitchell 1 spend, 1–2 weeks)
1. **Make the form real.** Wire it to a form backend (Formspree, Basin, or a Vercel serverless function) that emails the shop and optionally texts the service writer. Add vehicle year/make/model and a "preferred day" field.
2. **Click-to-text** button next to click-to-call. Younger customers text first.
3. **Real reviews.** Pull Google reviews with names and dates (SocialCRM's review tool, or a widget like Elfsight / Google's own embed). Show the live star count and link to "Leave a review".
4. **Real photos.** 8,000 sq ft, 9 lifts, 11 bays and the team. Stock-free. This matters more than any animation.
5. **Full service list** with one page per core service (brakes, tires & alignment, diagnostics, custom exhaust, A/C, transmission, fleet, marine). Each page targets "[service] West Salem" in search.
6. **Hours, logo, map** fixed and self-hosted. Years-in-business computed from 1996 in JS.
7. **Structured data**: `schema.org/AutoRepair` with address, geo, hours, phone, review rating. Rename title/copy to "West Salem".
8. **Warranty and financing pages.** Explain the 1 yr / 12k mile warranty and the financing options you'll offer through 360 Payments / 1stMile.
9. **Point the domain at the new site** and keep WhirLocal as a listing, not the homepage.

### Tier 2 – Turn the site into a tool (Mitchell 1 add-ons, 1–3 months)
1. **Book Online** as the primary hero CTA, powered by Book It Now (or AutoOps). Also enable the Google Business Profile "Book" button so people schedule straight from Maps without ever reaching the site.
2. **Text-to-pay** via 360 Payments. Add a "Pay My Invoice" page and an "After-hours pickup" explainer.
3. **Digital inspections** via OneFlow. Add a "How our inspections work" section with a sample report; this is your "honest shop" proof.
4. **Automated reminders and service-due texts** from SocialCRM, driven by Manager SE vehicle history.
5. **Reviews on autopilot**: SocialCRM asks every customer after the RO closes.

### Tier 3 – Cutting edge for a shop this size (3–6 months)
1. **Vehicle-aware homepage.** Customer enters year/make/model once; the site shows the factory maintenance schedule for that mileage and a "Book this service" button. (Data source: a maintenance-schedule API such as CarMD or a vendor that already has Mitchell data rights, since ProDemand's own data API is partner-only.)
2. **AI service assistant.** A chat widget that answers "do you work on diesels", "how long does an alignment take", "what does a check-engine diagnostic cost", and hands off to booking or text. Trained only on the shop's own content so it can't invent prices.
3. **Fleet / commercial page** with a dedicated fleet booking form and net-30 info. Marine too, since nobody else in West Salem advertises it online.
4. **Live availability banner**: "Next opening: Thursday 9:30 AM" pulled from Book It Now, shown in the hero.
5. **Spanish-language version** of key pages. Marion County is roughly a quarter Hispanic.
6. **Status transparency**: the DVI portal and text-to-pay links already give customers a "where's my car" view. Promote it as "You'll get a text with photos before we touch anything."
7. **Google Business Profile as a second front door**: booking, messaging, Q&A, photos and posts kept in sync by SocialCRM.

### What NOT to build
- A custom scheduler or custom payment portal. No API, PCI burden, and it would never talk to Manager SE.
- A public technician / bay board. Internal data.
- A customer login system. Everything a customer needs is delivered by text link.

---

## 4. Questions to settle before spending money
1. Does the shop already subscribe to **SocialCRM**? If yes, Book It Now, reviews and reminders may be a small upsell. If no, compare the SocialCRM bundle against AutoOps + a standalone review tool.
2. Who is the **current card processor**? Switching to 360 Payments (or 1stMile / Global Payments) is what unlocks text-to-pay. Check contract termination terms.
3. Does the shop run **Manager SE on-prem** and is it current? The newer integrations assume a recent version.
4. Do you want **live self-booking** (Book It Now / AutoOps) or **request-and-approve** (Online Appointments)? Shops that over-book bays usually start with request-and-approve for 90 days.
5. Who owns the **domain** and the Google Business Profile today?

---

---

## 5. Competitive landscape and the "stay on Mitchell 1 or switch" question

A separate competitive write-up (October 2026) reports that In His Name Automotive (West Salem) and AJ's Auto Repair (Salem) run Tekmetric and actively promote digital vehicle inspections with photo/video and text-link approvals, that Ledoux's uses SMS lead capture and service-interval texts, and that the rest of the local market (T&R, Westgate, Mike's Bellinger, P&M) is on older desktop setups without two-way texting. **I could not independently verify the specific stacks of those shops.** Treat the vendor claims as plausible but unconfirmed. The direction is right regardless: DVI plus automated texting is the retention and ARO lever, and most of the local market has not adopted it.

That write-up recommends Tekmetric or Shop-Ware as the "core engine". That is a bigger decision than a website feature, so here is a direct comparison of what each path gives Harold's.

### What Mitchell 1 already covers (no platform switch)
| Capability | Mitchell 1 answer | Gap vs Tekmetric |
|---|---|---|
| Interactive DVI with photos/video, red/yellow/green, text link, item-by-item approval | **OneFlow Inspections** (launched Sept 2025, integrated with Manager SE Job View) | None material |
| Declined / deferred work saved to the customer record | OneFlow saves declined items and can schedule future service and send reminders from Manager SE | None |
| Two-way texting from the shop | **MessageCenter** (Manager SE 7.5+): templates from Work-In-Progress, Order, Revision, Appointment and MPI screens, threads saved | Texts are **template-driven and sent by staff**; Tekmetric fires status texts automatically on status change |
| Appointment reminders, thank-you + review request | SocialCRM automated texts/emails | None |
| Service reminders based on vehicle history | SocialCRM service reminders | None |
| Online booking with real-time availability | SocialCRM Book It Now, or AutoOps | None |
| Text-to-pay, after-hours pickup, digital signature | 360 Payments integration | None |
| **Predictive follow-up on declined work** (projected miles/day, "your pads will hit 2mm this month") | Not native. **AutoVitals** does this and integrates with Manager SE; Kukui and Steer also integrate | Tekmetric does not do mileage projection natively either; shops layer AutoVitals/Steer on top of it too |
| Fully automated status texts (checked in, inspection ready, parts arrived, ready for pickup + pay link) | Partly: staff click a template at each step | **This is the real gap.** |

### Recommendation
**Do not switch shop management systems in the first 6 to 12 months of new ownership.** A system-of-record migration during an ownership transition stacks staff retraining, data conversion and process change on top of everything else. Mitchell 1 plus OneFlow Inspections, SocialCRM (or AutoVitals for DVI-driven follow-ups) and 360 Payments reaches roughly 80 to 90 percent of the Tekmetric workflow with no migration. The one real gap, fully automatic status texts, is a staff habit problem solved with MessageCenter templates and a checklist.

Set a **decision gate at month 6**: price the Mitchell 1 bundle (Manager SE + OneFlow + SocialCRM/Book It Now + texting) against Tekmetric (published from $179/mo, unlimited users, no contract, migration of customers/vehicles/history included). If the Mitchell 1 quote is materially higher or OneFlow is not in daily use by then, Tekmetric becomes the better path and the website needs no changes to accommodate it, because every customer-facing feature below is backend-agnostic.

### The predictive declined-work workflow, concretely
1. Tech rates front pads 4mm in OneFlow (yellow). Customer declines on the oil-change visit.
2. OneFlow stores the item as deferred on the vehicle record in Manager SE.
3. Follow-up engine (AutoVitals, Kukui or Steer; SocialCRM for simpler time-based reminders) projects wear from visit-to-visit mileage and sends a text with a link to the original inspection photos and a Book It Now slot.
4. Customer books; the appointment lands in Manager SE with the deferred job already attached.

The website's job in this loop is only step 3's landing page: a branded "view your inspection and book" page, which the vendors provide.

---

## 6. Website moves that follow from this (backend-agnostic)

Add to Tier 1 or Tier 2 of the roadmap above:

1. **"No Surprises. See What We See."** section. A real screenshot of a OneFlow (or AutoVitals) report with annotated brake and tire photos, a three-step strip (we inspect, you get a text with photos, you approve only what you want) and a line about the 30-point inspection on every visit. This is the single clearest differentiator over the legacy shops and parity with the Tekmetric shops.
2. **"Ready for Pickup" convenience block.** Text when checked in, text with inspection, text when ready, pay from your phone, keys in the after-hours lockbox. Pair it with the warranty badge.
3. **SMS opt-in lead magnet.** "Text SAVE to (503) 365-9702 for $20 off your first visit" plus a web form that captures mobile number and vehicle. Compliance is not optional here: the form needs express written consent language, STOP/HELP instructions, message frequency and a link to a privacy policy, and the sending number must be registered for 10DLC through whichever platform sends the texts (SocialCRM, AutoVitals, Kukui or Steer all handle this). Do not send marketing texts from a personal cell.
4. **Vehicle-history teaser.** "Every inspection, photo and invoice saved to your vehicle's record. Ask us for your history any time." Costs nothing, signals the system is modern.
5. **Service-interval content.** A 30/60/90k page per common make (Subaru, Toyota, Honda, Ford, GM) with a Book Online button. This feeds the reminder texts and ranks for "Subaru 60k service West Salem".


---

## 7. Retention and CRM program (on Mitchell 1)

Incorporates the owner's earlier research on running modern workflows without leaving Manager SE. Corrections and compliance flags are called out inline.

### Stack map
| Capability | Native Mitchell 1 | Third-party that integrates with Manager SE |
|---|---|---|
| Two-way texting, status updates | MessageCenter (templates from WIP, Order, Revision, Appointment, MPI screens) | Steer / MechanicAdvisor |
| Digital vehicle inspection | **OneFlow / Manager SE Inspections** (Sept 2025). Note: the older tablet DVI, Mobile Manager Pro, is a Bolt On Technology product, not Mitchell 1's own; it still works with Manager SE but OneFlow is the forward path | AutoVitals, Bolt On Mobile Manager Pro |
| Reminders, campaigns, reviews | SocialCRM (service reminders, text/email campaigns, postcards, review engine via SureCritic) | Kukui (local data connector pulls RO data) |
| Fleet accounts | Manager SE fleet features (fleet integration enhancements shipped by Mitchell 1) | — |

### Programs, in priority order
1. **Deferred-work re-engagement.** Deferred items from OneFlow sit on the vehicle record. Configure SocialCRM (or Kukui/AutoVitals) to text at 60 and 90 days with the original inspection link and a Book It Now slot. Sample copy is in the owner's research; keep it under 160 characters and lead with the measurement ("rear pads at 4mm").
2. **Three status texts per visit** from MessageCenter templates: checked in, inspection ready, ready for pickup with the 360 Payments link. Make it a service-writer checklist item, since Manager SE does not fire these automatically. The 7:30 AM "we got your keys from the drop box" text is a fourth template sent at morning check-in; it cannot be automated by the drop box itself.
3. **Post-service review request.** SocialCRM sends a thank-you text with a review link after the RO closes. **Do not gate reviews.** The proposed "4 to 5 stars goes to Google, 3 or lower goes to a private form" flow is review gating. Google's policy forbids selectively soliciting positive reviews and can remove the shop's entire review history for it; the FTC Consumer Reviews rule (effective Oct 2024) carries civil penalties of up to about $51,000 per violation for suppressing negative reviews. Compliant version: every customer gets the same public review link, with a separate, always-visible "Talk to the manager directly" option on the site and in the text. SureCritic (inside SocialCRM) publishes all reviews, which is the point.
4. **Maintenance club.** Yearly membership (for example $149: 2 synthetic oil changes, 2 rotations, 2 digital inspections, 10% off repairs up to $100). Manager SE tracks it with a package item and a customer discount code; there is no native membership module, so keep the rules simple enough for a service writer to apply by hand. Run the math on synthetic oil cost before pricing it; at today's prices two synthetic changes alone can approach the fee.
5. **Lapsed-customer win-back.** SocialCRM filters customers with no visit in 9 to 12 months and sends the "we miss your [Year Make Model]" text with a free safety inspection offer.
6. **Seasonal trip-check promos.** Spring "Coast & Mountain Road-Trip Inspection", late-fall "Winter Readiness Check". Each gets a landing page and a Book It Now service.
7. **New-mover direct mail.** SocialCRM postcards or a list vendor, 3 to 5 mile radius, $25 off first visit. Pair with a matching Google Ads geo campaign.
8. **Fleet outreach.** West Salem trades (plumbers, electricians, landscapers): priority morning turnaround, digital inspection logs per vehicle, monthly invoicing through Manager SE fleet accounts.

### Website pages this adds
- `/maintenance-club` with online signup (name, mobile, vehicle) feeding the CRM.
- `/fleet` with a fleet quote form and the inspection-log pitch.
- `/specials` with the current seasonal check and the first-visit voucher.
- `/review` with one public review link and a manager-contact form side by side (never gated).
- The SMS voucher form from section 6, with the consent language described there.


## Sources
- Mitchell 1 Book It Now press release: https://mitchell1.com/press/socialcrm-book-it-now-new-shop-marketing-services/
- Book It Now May 2026 enhancements (Snap-on): https://www.snapon.com/Snap-on-Files/News-Business-Units/News-Tools/2026/Mitchell-1-Enhances-SocialCRM-Book-it-Now-with-New-Scheduling-and-Appointment-Recovery-Features.pdf
- Book It Now Online Scheduler / pricing display: https://www.vehicleservicepros.com/industry-news/news/55389808/mitchell-1-expands-socialcrm-book-it-now-with-online-scheduler
- Online Appointments (request-based): https://mitchell1.com/shopconnection/upgrade-your-management-system-for-instant-online-appointment-scheduling/
- Manager SE Integrated Payments: https://mitchell1.com/manager-se/integrated-payment/
- 360 Payments partnership: https://www.ratchetandwrench.com/site-placement/latest-news/news/55277028/mitchell-1-partnership-with-360-payments-introduces-text-to-pay-function-for-manager-se
- Manager SE OneFlow Inspections: https://mitchell1.com/manager-se-inspections/
- SocialCRM overview: https://mitchell1.com/socialcrm/
- Mitchell 1 partner API program (third-party profile): https://github.com/api-evangelist/mitchell1
- AutoOps + Mitchell 1: https://www.autoops.com/home-1
- Manager SE pricing reports: https://www.capterra.com/p/145351/Manager-SE/ and https://shoptechscore.com/mitchell-1-review/
- Manager SE MessageCenter texting: https://mitchell1.com/press/mitchell-1-improves-productivity-solutions-built-text-messaging/
- OneFlow Inspections deferred work: https://autosphere.ca/mechanical/2025/09/09/mitchell-1-launches-manager-se-inspections-feature/
- Tekmetric vs Mitchell 1 (vendor page, pricing and migration claims): https://www.tekmetric.com/comparisons/tekmetric-vs-mitchell
- AutoVitals partner integrations: https://www.autovitals.com/partner-integration/
- Google / FTC review gating rules: https://www.socialpilot.co/reviews/blogs/review-gating
- Bolt On Mobile Manager Pro for Manager SE: https://www.underhoodservice.com/mitchell-1-introduces-mobile-managerpro/
- Current live site (WhirLocal redirect): https://whirlocal.io/company/harolds-quality-auto-repair-inc/
