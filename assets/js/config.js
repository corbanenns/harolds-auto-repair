/*
 * Harold's Quality Auto Repair – site configuration
 *
 * Every integration point on the site reads from this object, so connecting
 * Mitchell 1 add-ons and other services means editing values here only.
 * Leave a value empty ("" or null) and the site falls back gracefully
 * (e.g. the booking page shows the request form instead of the live scheduler).
 */
window.HAROLDS = {
  // Business basics
  name: "Harold's Quality Auto Repair",
  phone: "503-365-9702",
  phoneDisplay: "(503) 365-9702",
  address1: "675 Bartell Dr NW",
  city: "Salem",
  state: "OR",
  zip: "97304",
  foundedYear: 1996,
  hours: [
    ["Monday – Friday", "7:00 AM – 5:00 PM"],
    ["Saturday", "Closed"],
    ["Sunday", "Closed"]
  ],
  hours_es: [
    ["Lunes – Viernes", "7:00 AM – 5:00 PM"],
    ["Sábado", "Cerrado"],
    ["Domingo", "Cerrado"]
  ],
  // Weekday open/close used for the "Open today" line in the top bar (24h, Mon–Fri)
  weekdayOpen: 7, weekdayClose: 17,

  // Texting. Replace smsNumber with the 10DLC-registered number issued by
  // SocialCRM (or whichever platform sends marketing texts). Until then it
  // falls back to the shop line for conversational texts only.
  smsNumber: "503-365-9702",
  smsKeyword: "SAVE",
  firstVisitOffer: "$20 off your first visit",

  // Online booking: SocialCRM Book It Now, AutoOps, or SocialCRM Online
  // Appointments link. When set, every "Book Online" button opens it and the
  // booking page shows it in place of the request form.
  bookingUrl: "",
  // Optional: paste an embed snippet (iframe or script) instead of a link.
  bookingEmbed: "",

  // Payments: hosted payment page from 360 Payments / 1stMile / Global
  // Payments, if the processor offers one. Text-to-pay links are sent from
  // Manager SE and do not need this.
  payUrl: "",

  // Reviews: the Google "write a review" short link from the Business Profile
  // (or the SureCritic / SocialCRM review link). Same link for every customer.
  reviewUrl: "",
  googleRating: null,        // e.g. 4.7 – verify against the Business Profile
  googleReviewCount: null,   // e.g. 180

  // Forms: endpoint that accepts a JSON POST (Formspree, Basin, a Vercel
  // function, or a SocialCRM lead endpoint). Empty = forms show a
  // "call or text us" notice instead of pretending to send.
  formEndpoint: "",

  // Google Maps embed URL generated from maps.google.com → Share → Embed a map
  mapEmbed: "https://www.google.com/maps?q=675+Bartell+Dr+NW,+Salem,+OR+97304&output=embed"
};
