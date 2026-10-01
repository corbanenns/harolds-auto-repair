#!/usr/bin/env python3
"""Build the static site.

  python3 build.py

English page sources live in src/pages/, Spanish in src/pages/es/. Each page
begins with a JSON block in an HTML comment:
  <!-- {"title": "...", "description": "...", "path": "/book"} -->
Pages are wrapped with src/layout.html, whose {{t.key}} tokens are filled from
the STRINGS table below for the page's language. Output goes to the repo root
(English) and es/ (Spanish) and is committed, so Vercel needs no build step.
"""
import json, re, pathlib

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src"
PAGES = SRC / "pages"
DOMAIN = "https://www.haroldsautorepair.com"

STRINGS = {
  "en": {
    "lang": "en", "p": "", "skip": "Skip to content", "switch_label": "Español", "switch_lang": "es",
    "nav_services": "Services", "nav_oil": "Oil Change & Maintenance", "nav_brakes": "Brake Service", "nav_tires": "Tires & Alignment",
    "nav_diag": "Check Engine & Diagnostics", "nav_engine": "Engine & Transmission", "nav_ac": "A/C & Heating", "nav_exhaust": "Custom Exhaust",
    "nav_marine": "Marine & Boat Motors", "nav_fleet": "Fleet & Corporate", "nav_fleet_short": "Fleet & Corporate", "nav_inspections": "Inspections", "nav_club": "Maintenance Club", "nav_club_short": "Maintenance Club",
    "nav_specials": "Specials", "nav_pay": "Pay Invoice", "nav_about": "About", "nav_contact": "Contact", "book": "Book Online", "book_short": "Book Online", "menu": "Menu",
    "cta_h": "Ready when you are.", "cta_p": "Book online in under a minute, or call and talk to a real service advisor. Mon–Fri 7–5, West Salem.",
    "call": "Call", "text": "Text", "text_us": "Text us",
    "f_blurb": "Independent auto repair in West Salem since 1996. ASE Master Certified technicians, BBB Accredited, NAPA AutoCare Center. Every repair backed by our 1 year / 12,000 mile warranty.",
    "f_services": "Services", "f_customers": "Customers", "f_hours": "Hours", "f_book": "Book Online", "f_inspections": "How Digital Inspections Work",
    "f_pay": "Pay My Invoice", "f_club": "Maintenance Club", "f_specials": "Specials & Coupons", "f_review": "Leave a Review", "f_warranty": "Warranty & Financing",
    "f_fleet": "Fleet Service", "f_corporate": "Corporate Accounts", "f_keydrop": "After-hours key drop available.", "f_paylink": "Pay by text and pick up after close.",
    "f_rights": "All rights reserved.", "f_privacy": "Privacy & SMS Terms", "f_badges": "BBB Accredited · ASE Certified · NAPA AutoCare Center",
    "ab_call": "Call", "ab_text": "Text", "ab_book": "Book",
  },
  "es": {
    "lang": "es", "p": "/es", "skip": "Ir al contenido", "switch_label": "English", "switch_lang": "en",
    "nav_services": "Servicios", "nav_oil": "Cambio de aceite y mantenimiento", "nav_brakes": "Frenos", "nav_tires": "Llantas y alineación",
    "nav_diag": "Check engine y diagnóstico", "nav_engine": "Motor y transmisión", "nav_ac": "Aire acondicionado y calefacción", "nav_exhaust": "Escape a medida",
    "nav_marine": "Motores marinos", "nav_fleet": "Flotillas y empresas", "nav_fleet_short": "Empresas", "nav_inspections": "Inspecciones", "nav_club": "Club de mantenimiento", "nav_club_short": "Membresía",
    "nav_specials": "Ofertas", "nav_pay": "Pagar factura", "nav_about": "Nosotros", "nav_contact": "Contacto", "book": "Reservar en línea", "book_short": "Reservar", "menu": "Menú",
    "cta_h": "Cuando usted diga.", "cta_p": "Reserve en línea en menos de un minuto, o llame y hable con un asesor de servicio. Lun–Vie 7–5, West Salem.",
    "call": "Llamar", "text": "Texto", "text_us": "Envíenos un texto",
    "f_blurb": "Taller mecánico independiente en West Salem desde 1996. Técnicos con certificación ASE Master, acreditados por el BBB, centro NAPA AutoCare. Cada reparación respaldada por nuestra garantía de 1 año / 12,000 millas.",
    "f_services": "Servicios", "f_customers": "Clientes", "f_hours": "Horario", "f_book": "Reservar en línea", "f_inspections": "Cómo funcionan las inspecciones digitales",
    "f_pay": "Pagar mi factura", "f_club": "Club de mantenimiento", "f_specials": "Ofertas y cupones", "f_review": "Dejar una reseña", "f_warranty": "Garantía y financiamiento",
    "f_fleet": "Servicio de flotillas", "f_corporate": "Cuentas empresariales", "f_keydrop": "Buzón de llaves disponible fuera de horario.", "f_paylink": "Pague por texto y recoja después del cierre.",
    "f_rights": "Todos los derechos reservados.", "f_privacy": "Privacidad y términos de SMS", "f_badges": "Acreditado BBB · Certificación ASE · Centro NAPA AutoCare",
    "ab_call": "Llamar", "ab_text": "Texto", "ab_book": "Reservar",
  },
}

LAYOUT = (SRC / "layout.html").read_text()

def page_lang(src_path):
    rel = src_path.relative_to(PAGES)
    return ("es", rel.relative_to("es")) if rel.parts[0] == "es" else ("en", rel)

def render(src_path):
    raw = src_path.read_text()
    m = re.match(r"\s*<!--\s*(\{.*?\})\s*-->", raw, re.S)
    if not m:
        raise SystemExit(f"{src_path}: missing meta comment")
    meta = json.loads(m.group(1))
    content = raw[m.end():].strip("\n")
    lang, rel = page_lang(src_path)
    t = STRINGS[lang]
    path = meta["path"]
    # alternate-language path (mirrored slugs)
    alt_path = path[3:] or "/" if lang == "es" else ("/es" + path if path != "/" else "/es")
    alt_src = (PAGES / rel) if lang == "es" else (PAGES / "es" / rel)
    hreflang = ""
    if alt_src.exists():
        en_path, es_path = (alt_path, path) if lang == "es" else (path, alt_path)
        hreflang = (f'<link rel="alternate" hreflang="en" href="{DOMAIN}{en_path}">\n'
                    f'  <link rel="alternate" hreflang="es" href="{DOMAIN}{es_path}">\n'
                    f'  <link rel="alternate" hreflang="x-default" href="{DOMAIN}{en_path}">')
    jsonld = ""
    if meta.get("jsonld"):
        jsonld = '<script type="application/ld+json">' + json.dumps(meta["jsonld"], indent=2, ensure_ascii=False) + "</script>"
    html = LAYOUT
    vals = {"title": meta["title"], "description": meta["description"], "path": path, "content": content,
            "jsonld": jsonld, "hreflang": hreflang, "alt_path": alt_path if alt_src.exists() else (alt_path if lang == "en" else "/"),
            "domain": DOMAIN, "body_class": meta.get("body_class", "")}
    for k, v in vals.items():
        html = html.replace("{{" + k + "}}", v)
    for k, v in t.items():
        html = html.replace("{{t." + k + "}}", v)
    leftover = re.findall(r"\{\{[a-z_.]+\}\}", html)
    if leftover:
        raise SystemExit(f"{src_path}: unresolved tokens {sorted(set(leftover))}")
    out = ROOT / ("es" / rel if lang == "es" else rel)
    # a page whose name matches a sibling directory (services.html + services/) becomes that directory's index
    if (PAGES / rel.parent / rel.stem).is_dir():
        out = out.parent / rel.stem / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    return path

def main():
    paths = [render(p) for p in sorted(PAGES.rglob("*.html"))]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path in paths:
        if path.endswith("/privacy"):
            continue
        sm.append(f"  <url><loc>{DOMAIN}{path}</loc></url>")
    sm.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sm) + "\n")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    print(f"{len(paths)} pages built")

if __name__ == "__main__":
    main()
