/* Harold's Quality Auto Repair – shared behaviour. Reads window.HAROLDS (config.js). */
(function () {
  var C = window.HAROLDS || {};
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
  $all("[data-hours]").forEach(function (el) {
    el.innerHTML = (C.hours || []).map(function (h) { return "<tr><td>" + h[0] + "</td><td>" + h[1] + "</td></tr>"; }).join("");
  });
  $all("[data-map]").forEach(function (el) {
    if (C.mapEmbed) el.innerHTML = '<iframe src="' + C.mapEmbed + '" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade" title="Map to Harold\'s Quality Auto Repair"></iframe>';
  });

  /* ---- Booking: live scheduler when configured, request form otherwise ---- */
  $all("[data-book]").forEach(function (el) {
    if (C.bookingUrl) { el.setAttribute("href", C.bookingUrl); el.setAttribute("target", "_blank"); el.setAttribute("rel", "noopener"); }
    else { el.setAttribute("href", el.getAttribute("data-book") || "/book"); }
  });
  var embedHost = document.getElementById("booking-embed");
  var requestForm = document.getElementById("booking-request");
  if (embedHost && requestForm) {
    if (C.bookingEmbed) { embedHost.innerHTML = C.bookingEmbed; embedHost.classList.remove("hidden"); requestForm.classList.add("hidden"); }
    else if (C.bookingUrl) {
      embedHost.innerHTML = '<a class="btn btn-primary btn-lg" href="' + C.bookingUrl + '" target="_blank" rel="noopener">Open the online scheduler</a>';
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
      el.innerHTML = '<span class="stars" aria-hidden="true">★★★★★</span> <strong>' + C.googleRating + '</strong> on Google' +
        (C.googleReviewCount ? ' <span class="muted">(' + C.googleReviewCount + ' reviews)</span>' : "");
    } else { el.classList.add("hidden"); }
  });

  /* ---- Forms: JSON POST to the configured endpoint ---- */
  $all("form[data-form]").forEach(function (form) {
    var status = form.querySelector("[data-status]");
    function show(kind, html) { if (!status) return; status.className = "notice " + kind; status.innerHTML = html; status.classList.remove("hidden"); }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var data = {}; new FormData(form).forEach(function (v, k) { data[k] = v; });
      data.form = form.getAttribute("data-form"); data.page = location.pathname; data.submitted_at = new Date().toISOString();
      if (!C.formEndpoint) {
        show("warn", "Online forms aren't connected yet. Call or text us at <a " + 'href="' + telHref + '">' + (C.phoneDisplay || "") + "</a> and we'll take care of you.");
        return;
      }
      var btn = form.querySelector("[type=submit]"); if (btn) { btn.disabled = true; btn.dataset.label = btn.textContent; btn.textContent = "Sending…"; }
      fetch(C.formEndpoint, { method: "POST", headers: { "Content-Type": "application/json", "Accept": "application/json" }, body: JSON.stringify(data) })
        .then(function (r) { if (!r.ok) throw new Error(r.status); form.reset(); show("ok", form.getAttribute("data-success") || "Thanks! We'll get back to you shortly."); })
        .catch(function () { show("warn", "Something went wrong sending that. Please call or text <a " + 'href="' + telHref + '">' + (C.phoneDisplay || "") + "</a>."); })
        .then(function () { if (btn) { btn.disabled = false; btn.textContent = btn.dataset.label; } });
    });
  });

  /* ---- Nav ---- */
  var toggle = document.querySelector(".nav-toggle"), nav = document.querySelector(".nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () { var open = nav.classList.toggle("open"); toggle.setAttribute("aria-expanded", open ? "true" : "false"); });
  }
  var path = location.pathname.replace(/\/index\.html$/, "/").replace(/\.html$/, "");
  $all(".nav a").forEach(function (a) {
    var href = a.getAttribute("href"); if (!href || href.charAt(0) !== "/") return;
    if (href === path || (href !== "/" && path.indexOf(href) === 0)) a.setAttribute("aria-current", "page");
  });

  /* ---- Prefill service from ?service= on the booking page ---- */
  var svc = new URLSearchParams(location.search).get("service");
  var svcField = document.querySelector("select[name=service]");
  if (svc && svcField) { Array.prototype.forEach.call(svcField.options, function (o) { if (o.value.toLowerCase() === svc.toLowerCase()) svcField.value = o.value; }); }
})();
