/* Harold's Quality Auto Repair – shared behaviour. Reads window.HAROLDS (config.js). */
(function () {
  var C = window.HAROLDS || {};
  var LANG = (document.documentElement.lang || "en").slice(0, 2);
  var ES = LANG === "es";
  var PFX = ES ? "/es" : "";
  var T = ES ? {
    forms_off: "Los formularios en línea aún no están conectados. Llámenos o envíe un texto al ",
    forms_off2: " y con gusto le atendemos.",
    sending: "Enviando…", sent: "¡Gracias! Nos comunicaremos con usted en breve.",
    failed: "Algo salió mal al enviar. Por favor llame o envíe un texto al ",
    open_sched: "Abrir el programador en línea", on_google: " en Google", reviews: " reseñas",
    open_today: "Abierto hoy ", closed_today: "Cerrado hoy", until: "hasta las ", opens: "Abre el lunes 7:00 AM"
  } : {
    forms_off: "Online forms aren't connected yet. Call or text us at ",
    forms_off2: " and we'll take care of you.",
    sending: "Sending…", sent: "Thanks! We'll get back to you shortly.",
    failed: "Something went wrong sending that. Please call or text ",
    open_sched: "Open the online scheduler", on_google: " on Google", reviews: " reviews",
    open_today: "Open today ", closed_today: "Closed today", until: "until ", opens: "Opens Monday 7:00 AM"
  };
  var telHref = "tel:" + (C.phone || "");
  var smsHref = "sms:" + (C.smsNumber || C.phone || "");
  var smsOfferHref = smsHref + "?&body=" + encodeURIComponent(C.smsKeyword || "SAVE");

  function $all(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }

  /* ---- Fill config-driven text and links ---- */
  $all("[data-phone]").forEach(function (el) { el.textContent = C.phoneDisplay || ""; });
  $all("[data-tel]").forEach(function (el) { el.setAttribute("href", telHref); });
  $all("[data-sms]").forEach(function (el) { el.setAttribute("href", smsHref); });
  $all("[data-sms-offer]").forEach(function (el) { el.setAttribute("href", smsOfferHref); });
  $all("[data-sms-keyword]").forEach(function (el) { el.textContent = C.smsKeyword || "SAVE"; });
  $all("[data-offer]").forEach(function (el) { el.textContent = C.firstVisitOffer || ""; });
  $all("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
  $all("[data-years-since]").forEach(function (el) {
    el.textContent = (new Date().getFullYear() - (C.foundedYear || 1996)) + "+";
  });
  $all("[data-address]").forEach(function (el) {
    el.innerHTML = (C.address1 || "") + "<br>" + (C.city || "") + ", " + (C.state || "") + " " + (C.zip || "");
  });
  $all("[data-address-inline]").forEach(function (el) { el.textContent = (C.address1 || "") + ", " + (C.city || "") + ", " + (C.state || ""); });
  $all("[data-hours-today]").forEach(function (el) {
    var d = new Date(), day = d.getDay(), h = d.getHours();
    var fmt = function (n) { return (n > 12 ? n - 12 : n) + ":00 " + (n >= 12 ? "PM" : "AM"); };
    if (day >= 1 && day <= 5) el.textContent = (h < (C.weekdayClose || 17)) ? T.open_today + T.until + fmt(C.weekdayClose || 17) : T.closed_today;
    else el.textContent = T.closed_today + " · " + T.opens;
  });
  $all("[data-hours]").forEach(function (el) {
    el.innerHTML = ((ES && C.hours_es) || C.hours || []).map(function (h) { return "<tr><td>" + h[0] + "</td><td>" + h[1] + "</td></tr>"; }).join("");
  });
  $all("[data-map]").forEach(function (el) {
    if (C.mapEmbed) el.innerHTML = '<iframe src="' + C.mapEmbed + '" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade" title="Map to Harold\'s Quality Auto Repair"></iframe>';
  });

  /* ---- Booking: live scheduler when configured, request form otherwise ---- */
  $all("[data-book]").forEach(function (el) {
    if (C.bookingUrl) { el.setAttribute("href", C.bookingUrl); el.setAttribute("target", "_blank"); el.setAttribute("rel", "noopener"); }
    else { el.setAttribute("href", PFX + (el.getAttribute("data-book") || "/book")); }
  });
  var embedHost = document.getElementById("booking-embed");
  var requestForm = document.getElementById("booking-request");
  if (embedHost && requestForm) {
    if (C.bookingEmbed) { embedHost.innerHTML = C.bookingEmbed; embedHost.classList.remove("hidden"); requestForm.classList.add("hidden"); }
    else if (C.bookingUrl) {
      embedHost.innerHTML = '<a class="btn btn-primary btn-lg" href="' + C.bookingUrl + '" target="_blank" rel="noopener">' + T.open_sched + '</a>';
      embedHost.classList.remove("hidden");
    }
  }

  /* ---- Pay link, review link ---- */
  $all("[data-pay]").forEach(function (el) {
    if (C.payUrl) { el.setAttribute("href", C.payUrl); el.setAttribute("target", "_blank"); el.setAttribute("rel", "noopener"); }
    else { el.classList.add("hidden"); }
  });
  $all("[data-pay-missing]").forEach(function (el) { if (C.payUrl) el.classList.add("hidden"); });
  $all("[data-review]").forEach(function (el) {
    if (C.reviewUrl) { el.setAttribute("href", C.reviewUrl); el.setAttribute("target", "_blank"); el.setAttribute("rel", "noopener"); }
    else { el.classList.add("hidden"); }
  });
  $all("[data-review-missing]").forEach(function (el) { if (C.reviewUrl) el.classList.add("hidden"); });
  $all("[data-rating]").forEach(function (el) {
    if (C.googleRating) {
      el.innerHTML = '<span class="stars" aria-hidden="true">★★★★★</span> <strong>' + C.googleRating + '</strong>' + T.on_google +
        (C.googleReviewCount ? ' <span class="muted">(' + C.googleReviewCount + T.reviews + ')</span>' : "");
    } else { el.classList.add("hidden"); }
  });

  /* ---- Forms: JSON POST to the configured endpoint ---- */
  $all("form[data-form]").forEach(function (form) {
    var status = form.querySelector("[data-status]");
    function show(kind, html) { if (!status) return; status.className = "notice " + kind; status.innerHTML = html; status.classList.remove("hidden"); }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var data = {}; new FormData(form).forEach(function (v, k) { data[k] = v; });
      data.form = form.getAttribute("data-form"); data.page = location.pathname; data.lang = LANG; data.submitted_at = new Date().toISOString();
      if (!C.formEndpoint) {
        show("warn", T.forms_off + "<a " + 'href="' + telHref + '">' + (C.phoneDisplay || "") + "</a>" + T.forms_off2);
        return;
      }
      var btn = form.querySelector("[type=submit]"); if (btn) { btn.disabled = true; btn.dataset.label = btn.textContent; btn.textContent = T.sending; }
      fetch(C.formEndpoint, { method: "POST", headers: { "Content-Type": "application/json", "Accept": "application/json" }, body: JSON.stringify(data) })
        .then(function (r) { if (!r.ok) throw new Error(r.status); form.reset(); show("ok", form.getAttribute("data-success") || T.sent); track("form_submit", { form: data.form }, "form", "Lead"); })
        .catch(function () { show("warn", T.failed + "<a " + 'href="' + telHref + '">' + (C.phoneDisplay || "") + "</a>."); })
        .then(function () { if (btn) { btn.disabled = false; btn.textContent = btn.dataset.label; } });
    });
  });

  /* ---- Analytics & ad tags (only when configured) ---- */
  var GA = C.ga4MeasurementId, ADS = C.googleAdsId, PX = C.metaPixelId, LABELS = C.googleAdsConversions || {};
  function script(src) { var sc = document.createElement("script"); sc.async = true; sc.src = src; document.head.appendChild(sc); }
  if (GA || ADS) {
    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
    gtag("js", new Date());
    if (GA) gtag("config", GA);
    if (ADS) gtag("config", ADS);
    script("https://www.googletagmanager.com/gtag/js?id=" + (GA || ADS));
  }
  if (PX) {
    if (!window.fbq) { var n = window.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); }; n.push = n; n.loaded = true; n.version = "2.0"; n.queue = []; }
    script("https://connect.facebook.net/en_US/fbevents.js");
    fbq("init", PX); fbq("track", "PageView");
  }
  function track(name, params, adsKey, fbEvent) {
    params = params || {}; params.language = LANG;
    if (window.gtag && (GA || ADS)) {
      gtag("event", name, params);
      if (ADS && LABELS[adsKey]) gtag("event", "conversion", { send_to: ADS + "/" + LABELS[adsKey] });
    }
    if (window.fbq && PX && fbEvent) fbq("track", fbEvent, params);
    document.dispatchEvent(new CustomEvent("harolds:track", { detail: { name: name, params: params } }));
  }
  window.HAROLDS_TRACK = track;
  $all("[data-tel]").forEach(function (el) { el.addEventListener("click", function () { track("call_click", { location: el.closest("section,header,footer,nav") ? el.closest("section,header,footer,nav").className.split(" ")[0] : "" }, "call", "Contact"); }); });
  $all("[data-sms],[data-sms-offer]").forEach(function (el) { el.addEventListener("click", function () { track("text_click", { offer: el.hasAttribute("data-sms-offer") }, "text", "Contact"); }); });
  $all("[data-book]").forEach(function (el) { el.addEventListener("click", function () { track("book_click", { live_scheduler: !!C.bookingUrl }, "book", "Schedule"); }); });

  /* ---- Nav ---- */
  var toggle = document.querySelector(".nav-toggle"), nav = document.querySelector(".nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () { var open = nav.classList.toggle("open"); toggle.setAttribute("aria-expanded", open ? "true" : "false"); });
  }
  var path = location.pathname.replace(/\/index\.html$/, "/").replace(/\.html$/, "");
  $all(".nav a:not(.nav-lang)").forEach(function (a) {
    var href = a.getAttribute("href"); if (!href || href.charAt(0) !== "/") return;
    if (href === path || (href !== "/" && href !== "/es" && path.indexOf(href) === 0)) a.setAttribute("aria-current", "page");
  });
  /* Header shrink on scroll */
  var hdr = document.querySelector(".site-header");
  window.addEventListener("scroll", function () { if (hdr) hdr.classList.toggle("scrolled", window.scrollY > 40); }, { passive: true });
  /* Reveal on scroll */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }); }, { threshold: 0.12 });
    $all(".reveal").forEach(function (el) { io.observe(el); });
  } else { $all(".reveal").forEach(function (el) { el.classList.add("in"); }); }

  /* ---- Prefill service from ?service= on the booking page ---- */
  var svc = new URLSearchParams(location.search).get("service");
  var svcField = document.querySelector("select[name=service]");
  if (svc && svcField) { Array.prototype.forEach.call(svcField.options, function (o) { if (o.value.toLowerCase() === svc.toLowerCase()) svcField.value = o.value; }); }
})();
