#!/usr/bin/env python3
"""
TVPrime4K FR — Static page builder.
Generates subpages from a shared layout with per-page content.
"""
import os
import pathlib
import textwrap

ROOT = pathlib.Path(__file__).parent
WA = "4478888892117"
EMAIL = "contact@tvprime4k.com"
PHONE_DISPLAY = "+44 7888 8892117"


def wa(msg: str) -> str:
    from urllib.parse import quote
    return f"https://wa.me/{WA}?text={quote(msg)}"


NAV = """<nav class="nav">
  <div class="container nav-inner">
    <a href="/" class="logo">TVPrime<span class="mark">4K</span></a>
    <button class="nav-mobile-toggle" id="navToggle" aria-label="Menu">☰</button>
    <div class="nav-links" id="navLinks">
      <a href="/tarifs/">Tarifs</a>
      <a href="/chaines/">Chaînes</a>
      <a href="/appareils/">Appareils</a>
      <a href="/faq/">FAQ</a>
      <a href="{wa_contact}" class="nav-whatsapp" target="_blank" rel="noopener">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01S14.69 2 12.04 2zm0 18.15c-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.264 8.264 0 01-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24 2.2 0 4.27.86 5.82 2.42a8.183 8.183 0 012.41 5.83c.02 4.54-3.68 8.23-8.22 8.23z"/></svg>
        WhatsApp
      </a>
    </div>
  </div>
</nav>""".replace("{wa_contact}", wa("Bonjour, j'ai une question sur TVPrime4K."))

PROMO_BAR = """<div class="promo-bar" id="promoBar">
  🎁 <strong>Offre de lancement</strong> — 20% sur l'abonnement 12 mois · Code<span class="code">BIENVENUE20</span>
  <button class="promo-close" id="promoClose" aria-label="Fermer">×</button>
</div>"""

FOOTER = """<footer>
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-logo">TVPrime<span class="mark">4K</span></div>
        <p class="footer-tag">Le meilleur abonnement IPTV en 4K pour la France et le monde francophone. Sport, cinéma, séries et chaînes françaises.</p>
        <div class="pay-logos">
          <span class="pay-logo">PayPal</span>
          <span class="pay-logo">Visa</span>
          <span class="pay-logo">Mastercard</span>
          <span class="pay-logo">SEPA</span>
          <span class="pay-logo">Bitcoin</span>
          <span class="pay-logo">USDT</span>
        </div>
      </div>
      <div class="footer-col">
        <h4>Navigation</h4>
        <ul>
          <li><a href="/tarifs/">Tarifs</a></li>
          <li><a href="/chaines/">Chaînes</a></li>
          <li><a href="/appareils/">Appareils</a></li>
          <li><a href="/faq/">FAQ</a></li>
          <li><a href="/#garantie">Garantie</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Légal</h4>
        <ul>
          <li><a href="/cgv/">CGV</a></li>
          <li><a href="/confidentialite/">Confidentialité</a></li>
          <li><a href="/mentions-legales/">Mentions légales</a></li>
        </ul>
      </div>
      <div class="footer-col footer-contact">
        <h4>Contact</h4>
        <ul>
          <li><a href="{wa_contact}" target="_blank" rel="noopener"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" style="color: var(--whatsapp)"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01S14.69 2 12.04 2z"/></svg> {phone}</a></li>
          <li><a href="mailto:{email}"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--accent)"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><path d="M22 6l-10 7L2 6"/></svg> {email}</a></li>
          <li style="color: var(--fg-dim); font-size: 0.82rem; margin-top: 8px;">Réponse en moins de 10 minutes · 7j/7</li>
        </ul>
      </div>
    </div>

    <div class="seo-links">
      <h4>Nos pages</h4>
      <div class="seo-links-grid">
        <a href="/iptv-paris/">IPTV Paris</a>
        <a href="/iptv-lyon/">IPTV Lyon</a>
        <a href="/iptv-marseille/">IPTV Marseille</a>
        <a href="/iptv-sport-france/">IPTV Sport France</a>
        <a href="/iptv-4k-france/">IPTV 4K France</a>
        <a href="/iptv-pas-cher/">IPTV Pas Cher</a>
        <a href="/chaines/">Chaînes françaises</a>
        <a href="/appareils/">Appareils compatibles</a>
        <a href="/tarifs/">Tarifs & formules</a>
        <a href="/faq/">Questions fréquentes</a>
      </div>
    </div>

    <div class="footer-bottom">
      <div>© 2026 TVPrime4K — Tous droits réservés</div>
      <div>Service de streaming conforme aux réglementations européennes. Nous respectons les droits d'auteur et la propriété intellectuelle.</div>
    </div>
  </div>
</footer>""".replace("{wa_contact}", wa("Bonjour, j'ai une question sur TVPrime4K.")).replace("{phone}", PHONE_DISPLAY).replace("{email}", EMAIL)

FLOATING = """<a href="{wa_contact}" class="wa-bubble" target="_blank" rel="noopener" aria-label="Contacter sur WhatsApp">
  <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01S14.69 2 12.04 2zm0 18.15c-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.264 8.264 0 01-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24 2.2 0 4.27.86 5.82 2.42a8.183 8.183 0 012.41 5.83c.02 4.54-3.68 8.23-8.22 8.23z"/></svg>
</a>""".replace("{wa_contact}", wa("Bonjour, j'ai une question sur TVPrime4K."))

MOBILE_STICKY = """<div class="mobile-sticky">
  <div class="mobile-sticky-price">Dès <strong>49,99€</strong>/an</div>
  <a href="/tarifs/" class="btn btn-primary">Commander →</a>
</div>"""

EXIT_MODAL = """<div class="modal-backdrop" id="exitModal">
  <div class="modal">
    <button class="modal-close" data-close aria-label="Fermer">×</button>
    <div class="modal-eyebrow">🎁 Offre flash</div>
    <h3>Ne partez pas sans votre réduction</h3>
    <p style="font-size: 0.9rem; color: var(--fg-muted); margin: 0;">12 mois · 2 écrans — serveur Premium inclus</p>
    <div class="modal-price"><span class="new">79€</span><span class="old">99€</span></div>
    <ul class="modal-features">
      <li>55 000+ chaînes & 90 000+ VOD</li>
      <li>Full HD, 4K & technologie anti-gel</li>
      <li>Support WhatsApp 24/7</li>
      <li>Garantie 7 jours satisfait ou remboursé</li>
    </ul>
    <a href="{wa_flash}" class="btn btn-whatsapp" target="_blank" rel="noopener" data-close>Profiter de l'offre — 79€</a>
    <button class="modal-dismiss" data-close>Non merci, je continue ma visite</button>
  </div>
</div>""".replace("{wa_flash}", wa("Bonjour, je souhaite profiter de l'offre flash : 12 mois 2 écrans Premium à 79€. Merci !"))


PRICING_BLOCK = """<section id="tarifs" class="section section-alt">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Tarifs</div>
      <h2>Choisissez votre <em>formule</em></h2>
      <p>Paiement unique · Aucun renouvellement automatique · Garantie 7 jours sur toutes les offres.</p>
    </div>

    <div class="pricing-controls">
      <div class="toggle-group" id="serverToggle">
        <button class="toggle-btn active" data-server="standard">Standard</button>
        <button class="toggle-btn" data-server="premium">Premium Serveur</button>
      </div>
      <div class="toggle-group" id="screensToggle">
        <button class="toggle-btn active" data-screens="1">1 écran</button>
        <button class="toggle-btn" data-screens="2">2 écrans</button>
        <button class="toggle-btn" data-screens="3">3 écrans</button>
        <button class="toggle-btn" data-screens="4">4 écrans</button>
      </div>
    </div>

    <div class="plans-grid" id="plansGrid"></div>

    <div class="lifetime">
      <div>
        <div class="eyebrow">💎 Offre à vie</div>
        <div class="lifetime-title">Forfait à vie — un seul paiement, pour toujours</div>
        <p class="lifetime-sub">Plus de renouvellement à gérer. Payez une fois, gardez l'accès tant que le service est maintenu.</p>
      </div>
      <div class="lifetime-cta">
        <div class="lifetime-price">99€</div>
        <a href="{wa_lifetime}" class="btn btn-whatsapp" target="_blank" rel="noopener">Commander à vie</a>
      </div>
    </div>
  </div>
</section>""".replace("{wa_lifetime}", wa("Bonjour, je souhaite commander le FORFAIT À VIE — Standard à 99€. Merci !"))


GUARANTEE_BLOCK = """<section id="garantie" class="section">
  <div class="container">
    <div class="guarantee">
      <div class="shield"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l9 4v6c0 5.5-4 10-9 11-5-1-9-5.5-9-11V6l9-4z"/><path d="M9 12l2 2 4-4" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
      <div>
        <h2>Garantie satisfait ou remboursé — <em>7 jours</em></h2>
        <p>Testez TVPrime4K sans engagement. Si le service ne vous convient pas, pour n'importe quelle raison, nous vous remboursons intégralement dans les 7 jours. Pas de questions, pas de parcours compliqué.</p>
      </div>
    </div>
  </div>
</section>"""


FINAL_CTA = """<section class="final-cta">
  <div class="container final-cta-inner">
    <h2>Prêt à passer à l'<em>IPTV premium</em> ?</h2>
    <p>Rejoignez les 12 400+ foyers francophones qui ont déjà choisi TVPrime4K.</p>
    <div class="cta-row">
      <a href="/tarifs/" class="btn btn-primary">Choisir mon abonnement →</a>
      <a href="{wa_info}" class="btn btn-whatsapp" target="_blank" rel="noopener">💬 Parler sur WhatsApp</a>
    </div>
  </div>
</section>""".replace("{wa_info}", wa("Bonjour, je souhaite en savoir plus sur TVPrime4K."))


def page(title, description, canonical, body, extra_head="", simple=False):
    """Build a full HTML page."""
    return f"""<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <meta name="theme-color" content="#0a0d14">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="fr" href="{canonical}">
  <link rel="alternate" hreflang="x-default" href="https://tvprime4k.com/">

  <meta property="og:type" content="website">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:site_name" content="TVPrime4K">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">

  <link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..700;1,9..144,300..600&family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap">
  <link rel="stylesheet" href="/assets/css/main.css">
{extra_head}</head>
<body>

{PROMO_BAR}
{NAV}

{body}

{FOOTER}
{FLOATING}
{MOBILE_STICKY}
{EXIT_MODAL}

<script src="/assets/js/main.js"></script>
</body>
</html>
"""


# -----------------------------------------------------------------------------
# City pages (template-based)
# -----------------------------------------------------------------------------
CITIES = [
    {
        "slug": "paris",
        "name": "Paris",
        "team": "PSG",
        "match": "PSG — OM",
        "local": "Suivez chaque match du PSG au Parc des Princes en direct, en 4K, sans coupure. Pour les Parisiens exigeants, TVPrime4K regroupe Canal+, beIN Sports, RMC Sport et toutes les chaînes françaises dans un seul abonnement.",
        "neighborhoods": "Du 1er au 20ème arrondissement, en banlieue (Boulogne, Neuilly, Saint-Denis, Vincennes) ou en région parisienne, le service fonctionne partout en France métropolitaine sur fibre, ADSL et 4G/5G.",
    },
    {
        "slug": "lyon",
        "name": "Lyon",
        "team": "OL",
        "match": "OL — PSG",
        "local": "Les matchs de l'Olympique Lyonnais au Groupama Stadium, les derbies contre Saint-Étienne, le rugby du LOU, le basket de l'ASVEL — tout le sport local et national en 4K avec TVPrime4K.",
        "neighborhoods": "Que vous soyez à la Croix-Rousse, à la Part-Dieu, à Vaise, dans le Vieux Lyon ou dans l'ouest lyonnais (Écully, Tassin), le service fonctionne sur votre connexion fibre Orange, Free, SFR ou Bouygues.",
    },
    {
        "slug": "marseille",
        "name": "Marseille",
        "team": "OM",
        "match": "OM — PSG",
        "local": "L'OM au Vélodrome, le Classique contre le PSG, les matchs de Ligue 1 et de Ligue des champions — en 4K, sans décalage ni gel d'image. TVPrime4K regroupe tout le sport français avec le soleil marseillais en bonus.",
        "neighborhoods": "Des Catalans au Prado, de la Joliette au Panier, de la Pointe-Rouge à Saint-Henri, le service passe sur toutes les connexions internet marseillaises.",
    },
]


def city_page(city):
    body = f"""<section class="hero hero-slim">
  <div class="container hero-inner">
    <div>
      <div class="eyebrow">IPTV {city['name']} · {city['team']} en 4K</div>
      <h1>Abonnement IPTV à <em>{city['name']}</em> — Le meilleur IPTV France</h1>
      <p class="hero-sub">55 000 chaînes et 90 000 films & séries en 4K. Sport, cinéma, VOD, chaînes françaises. Compatible toutes les Smart TV, Fire Stick, Android, iOS. Garantie 7 jours.</p>
      <div class="cta-row">
        <a href="/tarifs/" class="btn btn-primary">Voir les forfaits →</a>
        <a href="{wa(f"Bonjour, je souhaite un essai TVPrime4K pour {city['name']}. Merci !")}" class="btn btn-whatsapp" target="_blank" rel="noopener">💬 Essai sur WhatsApp</a>
      </div>
      <div class="trust-row">
        <span><span class="check">✓</span> Garantie 7 jours</span>
        <span><span class="check">✓</span> Activation instantanée</span>
        <span><span class="check">✓</span> Paiement sécurisé</span>
      </div>
    </div>
  </div>
</section>

<section class="stats">
  <div class="container stats-grid">
    <div><div class="stat-num">55 000<em>+</em></div><div class="stat-label">Chaînes</div></div>
    <div><div class="stat-num">90 000<em>+</em></div><div class="stat-label">Films & séries</div></div>
    <div><div class="stat-num">12 400<em>+</em></div><div class="stat-label">Clients actifs</div></div>
    <div><div class="stat-num">4,7<em>/5</em></div><div class="stat-label">Note moyenne</div></div>
    <div><div class="stat-num">7 ans</div><div class="stat-label">D'expérience</div></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">À {city['name']}</div>
      <h2>Pourquoi TVPrime4K à <em>{city['name']}</em></h2>
    </div>
    <div class="local-block">
      <h3>Le sport local et national en 4K</h3>
      <p>{city['local']}</p>
      <h3>Partout dans {city['name']}</h3>
      <p>{city['neighborhoods']}</p>
      <h3>Installation simple, support en français</h3>
      <p>Vos identifiants arrivent par e-mail en 10 à 15 minutes. Compatible IPTV Smarters Pro, VLC, Perfect Player et toutes les applications M3U/Xtream. Notre équipe vous guide par WhatsApp si l'installation pose problème.</p>
    </div>
  </div>
</section>

{PRICING_BLOCK}

{GUARANTEE_BLOCK}

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Autres villes</div>
      <h2>IPTV dans d'autres <em>villes françaises</em></h2>
    </div>
    <div class="seo-links-grid" style="max-width: 820px; margin: 0 auto;">
      <a href="/iptv-paris/">IPTV Paris</a>
      <a href="/iptv-lyon/">IPTV Lyon</a>
      <a href="/iptv-marseille/">IPTV Marseille</a>
      <a href="/iptv-sport-france/">IPTV Sport France</a>
      <a href="/iptv-4k-france/">IPTV 4K France</a>
      <a href="/iptv-pas-cher/">IPTV Pas Cher</a>
    </div>
  </div>
</section>

{FINAL_CTA}"""

    return page(
        title=f"IPTV {city['name']} 2026 — Meilleur abonnement IPTV France 4K | TVPrime4K",
        description=f"Abonnement IPTV à {city['name']} : 55 000 chaînes, 90 000 films & séries en 4K. Sport, cinéma, chaînes françaises. Garantie 7 jours. Dès 24,99€.",
        canonical=f"https://fr.tvprime4k.com/iptv-{city['slug']}/",
        body=body,
    )


# -----------------------------------------------------------------------------
# Modifier pages
# -----------------------------------------------------------------------------
MODIFIERS = [
    {
        "slug": "iptv-sport-france",
        "h1": "IPTV Sport France — <em>beIN, Canal+, RMC Sport</em>",
        "title": "IPTV Sport France 2026 — beIN Sports, Canal+ Foot, Ligue 1 en 4K | TVPrime4K",
        "description": "IPTV Sport France : tous les matchs de Ligue 1, Ligue des champions, beIN Sports, Canal+ Sport, RMC Sport en 4K. Zéro buffering. Garantie 7 jours.",
        "eyebrow": "Sport 4K · Zéro buffering",
        "intro": "L'IPTV faite pour le sport : toutes les grandes compétitions en Full HD et 4K, sur des serveurs anti-gel testés pendant les plus gros matchs de la saison.",
        "sections": [
            ("Toutes les grandes compétitions", "Ligue 1 Uber Eats, Ligue des champions UEFA, Europa League, Premier League, Liga, Serie A, Bundesliga, Coupe du monde, Euro — tous les grands rendez-vous du football en direct et en 4K."),
            ("Tennis, rugby, F1, basket", "Roland-Garros, Wimbledon, l'US Open, le Tour de France, le Top 14, les 6 Nations, la Formule 1, la NBA, l'EuroLigue — le sport sous toutes ses formes dans un seul abonnement."),
            ("Les chaînes sport incluses", "beIN Sports 1 à 3, Canal+ Sport, Canal+ Foot, RMC Sport, Eurosport 1 & 2, L'Équipe, et les chaînes sport étrangères (Sky Sports, ESPN, DAZN) pour les expatriés et les fans de sports internationaux."),
            ("Serveurs anti-gel pour le direct", "Les soirées sport sont le vrai test d'une IPTV. Notre infrastructure européenne est dimensionnée pour tenir la charge aux heures de pointe, avec moins de 15 ms de latence sur les flux français."),
        ],
    },
    {
        "slug": "iptv-4k-france",
        "h1": "IPTV 4K France — <em>Ultra HD</em> sur tous les écrans",
        "title": "IPTV 4K France 2026 — Streaming Ultra HD stable sur Smart TV | TVPrime4K",
        "description": "IPTV 4K France : plus de 2 000 chaînes et 90 000 films en Ultra HD. Compatible Samsung, LG, Sony, Fire TV 4K. Serveurs stables. Garantie 7 jours.",
        "eyebrow": "Ultra HD · 4K UHD",
        "intro": "Le 4K sans compromis. Films, séries, grandes compétitions sportives et documentaires en Ultra HD, sur votre Smart TV 4K, Fire TV Stick 4K ou Apple TV 4K.",
        "sections": [
            ("Plus de 2 000 chaînes en 4K", "Les chaînes premium sport, cinéma et documentaires sont diffusées en vraie 4K Ultra HD à 50 fps quand elles le proposent à la source. Le reste du catalogue est en Full HD ou HD selon la chaîne."),
            ("90 000 films & séries en 4K", "Le catalogue VOD est en 4K pour les blockbusters récents, Full HD pour les autres titres. Mises à jour quotidiennes avec les sorties cinéma, Netflix, Disney+, HBO et Prime Video."),
            ("Infrastructure dimensionnée pour le 4K", "Serveurs européens avec bande passante dédiée. Un flux 4K consomme 25-30 Mbps, notre infrastructure encaisse sans ralentir le reste de votre connexion."),
            ("Compatibilité 4K vérifiée", "Testé sur Samsung QLED/OLED, LG OLED C/G, Sony Bravia 4K, Fire TV Stick 4K Max, Apple TV 4K, Nvidia Shield Pro, et toutes les box Android TV 4K récentes."),
        ],
    },
    {
        "slug": "iptv-pas-cher",
        "h1": "IPTV Pas Cher — <em>24,99€ les 3 mois</em>, sans compromis",
        "title": "IPTV Pas Cher France 2026 — Abonnement dès 24,99€ | TVPrime4K",
        "description": "IPTV pas cher mais fiable : 24,99€ les 3 mois, 54,99€ l'année. 55 000 chaînes, 90 000 VOD, 4K, garantie 7 jours. Pas de renouvellement automatique.",
        "eyebrow": "Prix clair · Pas de pièges",
        "intro": "Un abonnement IPTV pas cher ne doit pas être un abonnement raté. Nos tarifs sont parmi les plus bas du marché, sans sacrifier la qualité des serveurs ni l'étendue du catalogue.",
        "sections": [
            ("Les prix les plus bas du marché français", "24,99€ pour 3 mois, 39,99€ pour 6 mois, 54,99€ pour 12 mois, 89,99€ pour 24 mois. Soit ~4,58€/mois sur l'offre annuelle — moins qu'un café par semaine."),
            ("Un seul paiement, pas de pièges", "Pas de prélèvement automatique. Pas de frais cachés. Le prix affiché est le prix final. Nous vous enverrons un e-mail avant l'expiration — à vous de décider."),
            ("Pourquoi aussi pas cher ?", "Pas de magasin physique, pas de publicité TV, une équipe réduite qui gère tout en direct. Nous passons les économies sur le prix, pas sur la qualité des flux."),
            ("Garantie 7 jours même sur le forfait pas cher", "Toutes les formules — y compris le 3 mois à 24,99€ — sont couvertes par la garantie satisfait ou remboursé de 7 jours. Testez sans risque."),
        ],
    },
]


def modifier_page(mod):
    sections_html = "\n".join(f"""      <h3>{t}</h3>
      <p>{p}</p>""" for t, p in mod["sections"])

    body = f"""<section class="hero hero-slim">
  <div class="container hero-inner">
    <div>
      <div class="eyebrow">{mod['eyebrow']}</div>
      <h1>{mod['h1']}</h1>
      <p class="hero-sub">{mod['intro']}</p>
      <div class="cta-row">
        <a href="/tarifs/" class="btn btn-primary">Voir les forfaits →</a>
        <a href="{wa(f"Bonjour, je souhaite en savoir plus sur TVPrime4K.")}" class="btn btn-whatsapp" target="_blank" rel="noopener">💬 Parler sur WhatsApp</a>
      </div>
      <div class="trust-row">
        <span><span class="check">✓</span> Garantie 7 jours</span>
        <span><span class="check">✓</span> Activation instantanée</span>
        <span><span class="check">✓</span> Serveurs stables</span>
      </div>
    </div>
  </div>
</section>

<section class="stats">
  <div class="container stats-grid">
    <div><div class="stat-num">55 000<em>+</em></div><div class="stat-label">Chaînes</div></div>
    <div><div class="stat-num">90 000<em>+</em></div><div class="stat-label">Films & séries</div></div>
    <div><div class="stat-num">12 400<em>+</em></div><div class="stat-label">Clients actifs</div></div>
    <div><div class="stat-num">4,7<em>/5</em></div><div class="stat-label">Note moyenne</div></div>
    <div><div class="stat-num">7 ans</div><div class="stat-label">D'expérience</div></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">En détail</div>
      <h2>Ce qui fait la <em>différence</em></h2>
    </div>
    <div class="local-block">
{sections_html}
    </div>
  </div>
</section>

{PRICING_BLOCK}

{GUARANTEE_BLOCK}

{FINAL_CTA}"""

    return page(
        title=mod["title"],
        description=mod["description"],
        canonical=f"https://fr.tvprime4k.com/{mod['slug']}/",
        body=body,
    )


# -----------------------------------------------------------------------------
# Supporting pages
# -----------------------------------------------------------------------------
def tarifs_page():
    body = f"""<section class="breadcrumb">
  <div class="container"><a href="/">Accueil</a><span class="sep">/</span>Tarifs</div>
</section>

<section class="hero hero-slim">
  <div class="container hero-inner">
    <div>
      <div class="eyebrow">Tarifs TVPrime4K</div>
      <h1>Tarifs et <em>formules</em> IPTV France</h1>
      <p class="hero-sub">Comparez toutes nos formules — standard et premium, de 1 à 4 écrans. Paiement unique, aucun renouvellement automatique, garantie 7 jours.</p>
    </div>
  </div>
</section>

{PRICING_BLOCK}

{GUARANTEE_BLOCK}

{FINAL_CTA}"""

    return page(
        title="Tarifs IPTV France 2026 — Formules dès 24,99€ | TVPrime4K",
        description="Toutes les formules TVPrime4K : standard et premium, 1 à 4 écrans, 3 à 24 mois. Lifetime à 99€. Garantie 7 jours. Dès 24,99€.",
        canonical="https://fr.tvprime4k.com/tarifs/",
        body=body,
    )


def chaines_page():
    body = """<section class="breadcrumb">
  <div class="container"><a href="/">Accueil</a><span class="sep">/</span>Chaînes</div>
</section>

<section class="hero hero-slim">
  <div class="container hero-inner">
    <div>
      <div class="eyebrow">Catalogue chaînes</div>
      <h1>Toutes les <em>chaînes françaises</em> et internationales</h1>
      <p class="hero-sub">TNT française complète, bouquets sport, cinéma, documentaires, jeunesse. Plus les chaînes européennes, arabes, nord-américaines, asiatiques. 55 000+ chaînes.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">France</div>
      <h2>Les grandes chaînes <em>françaises</em></h2>
      <p>La TNT française complète, en Full HD. Replay sur 7 jours pour les grandes chaînes.</p>
    </div>
    <div class="channel-grid">
      <div class="channel-cell">TF1</div>
      <div class="channel-cell">France 2</div>
      <div class="channel-cell">France 3</div>
      <div class="channel-cell">France 4</div>
      <div class="channel-cell">France 5</div>
      <div class="channel-cell">M6</div>
      <div class="channel-cell">Arte</div>
      <div class="channel-cell">C8</div>
      <div class="channel-cell">TMC</div>
      <div class="channel-cell">TFX</div>
      <div class="channel-cell">W9</div>
      <div class="channel-cell">6ter</div>
      <div class="channel-cell">NRJ 12</div>
      <div class="channel-cell">RMC Story</div>
      <div class="channel-cell">CNEWS</div>
      <div class="channel-cell">BFM TV</div>
      <div class="channel-cell">LCI</div>
      <div class="channel-cell">France Info</div>
      <div class="channel-cell">Gulli</div>
      <div class="channel-cell">Chérie 25</div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Sport</div>
      <h2>Toutes les chaînes <em>sport</em></h2>
      <p>Ligue 1, Ligue des champions, Premier League, Liga, Serie A, Roland-Garros, Tour de France, Formule 1, NBA.</p>
    </div>
    <div class="channel-grid">
      <div class="channel-cell">Canal+ Sport</div>
      <div class="channel-cell">Canal+ Foot</div>
      <div class="channel-cell">beIN Sports 1</div>
      <div class="channel-cell">beIN Sports 2</div>
      <div class="channel-cell">beIN Sports 3</div>
      <div class="channel-cell">RMC Sport 1</div>
      <div class="channel-cell">RMC Sport 2</div>
      <div class="channel-cell">Eurosport 1</div>
      <div class="channel-cell">Eurosport 2</div>
      <div class="channel-cell">L'Équipe</div>
      <div class="channel-cell">Infosport+</div>
      <div class="channel-cell">La chaîne L1</div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Cinéma & séries</div>
      <h2>Films et séries en <em>4K</em></h2>
      <p>Toutes les grandes chaînes cinéma + 90 000 films & séries en VOD, mises à jour tous les jours.</p>
    </div>
    <div class="channel-grid">
      <div class="channel-cell">Canal+</div>
      <div class="channel-cell">Canal+ Cinéma</div>
      <div class="channel-cell">Canal+ Séries</div>
      <div class="channel-cell">OCS Max</div>
      <div class="channel-cell">OCS City</div>
      <div class="channel-cell">OCS Choc</div>
      <div class="channel-cell">Ciné+ Premier</div>
      <div class="channel-cell">Ciné+ Frisson</div>
      <div class="channel-cell">Ciné+ Classic</div>
      <div class="channel-cell">Paramount Ch.</div>
      <div class="channel-cell">13ème Rue</div>
      <div class="channel-cell">AB1</div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">International</div>
      <h2>Chaînes <em>internationales</em></h2>
      <p>Europe, pays arabes, Amérique du Nord, Asie — toutes les grandes régions couvertes.</p>
    </div>
    <div class="channel-grid">
      <div class="channel-cell">RTBF (BE)</div>
      <div class="channel-cell">RTL Belgique</div>
      <div class="channel-cell">RTS (CH)</div>
      <div class="channel-cell">TV5 Monde</div>
      <div class="channel-cell">RAI (IT)</div>
      <div class="channel-cell">RTVE (ES)</div>
      <div class="channel-cell">ARD (DE)</div>
      <div class="channel-cell">BBC One</div>
      <div class="channel-cell">Sky Sports</div>
      <div class="channel-cell">Al Jazeera</div>
      <div class="channel-cell">MBC</div>
      <div class="channel-cell">Rotana</div>
      <div class="channel-cell">TVA (CA)</div>
      <div class="channel-cell">RDS</div>
      <div class="channel-cell">ESPN (US)</div>
      <div class="channel-cell more"><span class="count">+55 000</span><span class="label">autres</span></div>
    </div>
    <div class="channel-cta">
      <a href="https://wa.me/4478888892117?text=Bonjour%2C%20je%20souhaite%20recevoir%20la%20liste%20compl%C3%A8te%20des%20cha%C3%AEnes%20TVPrime4K.%20Merci%20!" class="btn btn-whatsapp" target="_blank" rel="noopener">💬 Demander la liste complète</a>
    </div>
  </div>
</section>

""" + PRICING_BLOCK + FINAL_CTA

    return page(
        title="Chaînes IPTV TVPrime4K — TF1, M6, Canal+, beIN Sports, RMC Sport",
        description="Liste des chaînes TVPrime4K : toute la TNT française, bouquets sport (Canal+, beIN, RMC), cinéma (OCS, Ciné+), international. 55 000+ chaînes au total.",
        canonical="https://fr.tvprime4k.com/chaines/",
        body=body,
    )


def appareils_page():
    body = """<section class="breadcrumb">
  <div class="container"><a href="/">Accueil</a><span class="sep">/</span>Appareils</div>
</section>

<section class="hero hero-slim">
  <div class="container hero-inner">
    <div>
      <div class="eyebrow">Appareils compatibles</div>
      <h1>Un abonnement, <em>tous vos écrans</em></h1>
      <p class="hero-sub">Smart TV, box IPTV, mobile, tablette, ordinateur — TVPrime4K fonctionne partout, sans décodeur à acheter. Installation en 2 à 10 minutes.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="devices-grid">
      <div class="device-category">
        <h3>Smart TV</h3>
        <ul class="device-list">
          <li>Samsung (Tizen) — 2017+</li>
          <li>LG (webOS) — 2017+</li>
          <li>Sony Bravia (Android TV)</li>
          <li>TCL, Hisense, Philips</li>
          <li>Toutes Smart TV récentes</li>
        </ul>
      </div>
      <div class="device-category">
        <h3>Box & Stick</h3>
        <ul class="device-list">
          <li>Amazon Fire TV Stick / 4K / 4K Max</li>
          <li>Apple TV HD / 4K</li>
          <li>MAG 254, 322, 420, 520</li>
          <li>Formuler Z / Z8 / Z11</li>
          <li>Box Android TV (Nvidia Shield…)</li>
        </ul>
      </div>
      <div class="device-category">
        <h3>Mobile & tablette</h3>
        <ul class="device-list">
          <li>iPhone (iOS 12+)</li>
          <li>iPad</li>
          <li>Smartphone Android (6+)</li>
          <li>Tablette Android</li>
          <li>Via IPTV Smarters Pro / TiviMate</li>
        </ul>
      </div>
      <div class="device-category">
        <h3>Ordinateur</h3>
        <ul class="device-list">
          <li>Windows (7, 10, 11)</li>
          <li>Mac (macOS)</li>
          <li>Linux (via VLC)</li>
          <li>Chromebook</li>
          <li>Navigateur web direct</li>
        </ul>
      </div>
    </div>
    <div class="devices-foot" style="margin-top: 40px;">
      <p>Besoin d'aide pour l'installation ? Notre équipe vous guide étape par étape sur WhatsApp — en moyenne 10 minutes du paiement au premier match.</p>
      <a href="https://wa.me/4478888892117?text=Bonjour%2C%20j%27ai%20besoin%20d%27aide%20pour%20l%27installation%20de%20TVPrime4K." class="btn btn-whatsapp" target="_blank" rel="noopener">Aide installation WhatsApp</a>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Applications</div>
      <h2>Applications <em>compatibles</em></h2>
      <p>TVPrime4K fonctionne avec tous les lecteurs IPTV populaires.</p>
    </div>
    <div class="features-grid">
      <div class="feature"><h3>IPTV Smarters Pro</h3><p>L'application la plus utilisée en France. Interface claire, EPG détaillé, favoris, replay.</p></div>
      <div class="feature"><h3>TiviMate</h3><p>La référence sur Android TV / Fire TV. Interface moderne, catch-up, enregistrement.</p></div>
      <div class="feature"><h3>VLC Media Player</h3><p>Pour les ordinateurs. Lit la playlist M3U sans configuration.</p></div>
      <div class="feature"><h3>Perfect Player</h3><p>Alternative légère, Xtream Codes, parfait pour les anciennes box Android.</p></div>
    </div>
  </div>
</section>

""" + GUARANTEE_BLOCK + FINAL_CTA

    return page(
        title="Appareils compatibles TVPrime4K — Smart TV, Fire Stick, iPhone, Android",
        description="Compatible Samsung, LG, Sony, Fire TV Stick, Apple TV, MAG, iPhone, iPad, Android, Windows, Mac. Installation en 10 minutes. Support WhatsApp 24/7.",
        canonical="https://fr.tvprime4k.com/appareils/",
        body=body,
    )


def faq_page():
    faqs = [
        ("Comment vais-je recevoir mon abonnement ?", "Après confirmation du paiement, vous recevez vos identifiants IPTV et le lien M3U par e-mail en 5 à 15 minutes. Un guide d'installation détaillé pour votre appareil est joint. Pensez à vérifier le dossier spam."),
        ("Quels appareils sont compatibles ?", "Smart TV (Samsung, LG, Sony, TCL, Hisense, Philips), Fire TV Stick, Apple TV, MAG, Formuler, box Android, iPhone, iPad, smartphone Android, tablette, Windows, Mac, Linux. Compatible IPTV Smarters Pro, TiviMate, VLC, Perfect Player et tous les lecteurs M3U/Xtream."),
        ("Combien d'écrans puis-je utiliser en même temps ?", "L'abonnement standard est pour 1 écran à la fois. Nos formules multi-écrans permettent 2, 3 ou 4 connexions simultanées — idéal pour les familles. Vous pouvez installer l'application sur autant d'appareils que vous voulez, seule la lecture simultanée est limitée."),
        ("Les chaînes françaises (TF1, M6, Canal+, beIN) sont-elles incluses ?", "Oui. Toute la TNT française (TF1, France 2/3/5, M6, Arte, C8, TMC, W9, 6ter, etc.), les bouquets Canal+, beIN Sports, RMC Sport, OCS, Ciné+, les chaînes jeunesse (Gulli, Boomerang), documentaires (Discovery, Nat Geo, History) et toutes les chaînes européennes, arabes et nord-américaines."),
        ("Y a-t-il un essai gratuit ?", "Nous proposons un essai de 24h sur demande via WhatsApp pour tester la qualité avant l'achat. En plus, tous les abonnements sont couverts par la garantie satisfait ou remboursé de 7 jours."),
        ("Comment est fait le paiement ? Est-ce sécurisé ?", "Nous acceptons PayPal, carte bancaire (Visa/Mastercard), virement SEPA et cryptomonnaie (Bitcoin, USDT). Tous les paiements passent par des processeurs sécurisés. Nous ne stockons aucune donnée de carte."),
        ("Puis-je demander un remboursement ?", 'Oui. La garantie satisfait ou remboursé de 7 jours couvre toutes les formules. Si le service ne vous convient pas, écrivez-nous sur WhatsApp ou à contact@tvprime4k.com et nous procédons au remboursement intégral, sans justification à fournir. <a id="remboursement"></a>'),
        ("Quelle vitesse Internet faut-il ?", "Minimum 10 Mbps pour la HD, 25 Mbps pour la 4K. La fibre optique est idéale mais la plupart des connexions ADSL récentes suffisent largement en Full HD. En 4G/5G, un bon signal permet aussi de regarder en Full HD."),
        ("L'abonnement se renouvelle-t-il automatiquement ?", "Non. Aucun prélèvement automatique. Vous payez une seule fois pour la durée choisie. Avant l'expiration, nous vous envoyons un e-mail pour vous proposer de renouveler — mais vous êtes libre."),
        ("L'IPTV est-elle légale en France ?", "L'IPTV en tant que technologie est parfaitement légale. Nous proposons un service de streaming conforme aux réglementations européennes. Vous êtes responsable de l'utilisation du service conformément aux lois en vigueur dans votre pays de résidence."),
        ("Puis-je utiliser TVPrime4K depuis l'étranger ?", "Oui. Le service fonctionne partout dans le monde avec une connexion internet correcte. Les expatriés français au Canada, au Royaume-Uni, en Belgique, en Suisse, au Maroc ou ailleurs retrouvent leurs chaînes françaises comme à la maison, sans VPN nécessaire."),
        ("Que faire si l'image gèle ou coupe ?", "Vérifiez d'abord votre connexion internet (idéalement 25+ Mbps en 4K). Si le problème persiste, redémarrez votre application IPTV, puis votre box ou TV. Si vous constatez des coupures régulières, contactez-nous sur WhatsApp — nous pouvons vous basculer sur un serveur plus proche de votre région."),
    ]
    faq_html = "\n".join(f'      <div class="faq-item"><button class="faq-q">{q}</button><div class="faq-a">{a}</div></div>' for q, a in faqs)

    body = f"""<section class="breadcrumb">
  <div class="container"><a href="/">Accueil</a><span class="sep">/</span>FAQ</div>
</section>

<section class="hero hero-slim">
  <div class="container hero-inner">
    <div>
      <div class="eyebrow">Questions fréquentes</div>
      <h1>Toutes les réponses sur <em>TVPrime4K</em></h1>
      <p class="hero-sub">Si votre question n'est pas ici, écrivez-nous sur WhatsApp — on répond en moyenne en moins de 10 minutes, 7j/7.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="faq-list" id="faqList">
{faq_html}
    </div>
  </div>
</section>

{FINAL_CTA}"""

    return page(
        title="FAQ TVPrime4K — Questions fréquentes IPTV France",
        description="Toutes les réponses sur TVPrime4K : installation, compatibilité, paiement, remboursement, légalité, écrans simultanés. Support WhatsApp 7j/7.",
        canonical="https://fr.tvprime4k.com/faq/",
        body=body,
    )


# -----------------------------------------------------------------------------
# Legal pages (prose)
# -----------------------------------------------------------------------------
def mentions_page():
    body = """<section class="breadcrumb">
  <div class="container"><a href="/">Accueil</a><span class="sep">/</span>Mentions légales</div>
</section>
<article class="container prose">
  <h1>Mentions légales</h1>
  <p>Conformément aux dispositions des articles 6-III et 19 de la Loi n°2004-575 du 21 juin 2004 pour la Confiance dans l'économie numérique, dite L.C.E.N., nous vous informons des informations légales suivantes.</p>

  <h2>Éditeur du site</h2>
  <p>Le site <strong>fr.tvprime4k.com</strong> est édité par TVPrime4K.</p>
  <ul>
    <li><strong>Nom commercial :</strong> TVPrime4K</li>
    <li><strong>Contact :</strong> contact@tvprime4k.com</li>
    <li><strong>Téléphone / WhatsApp :</strong> +44 7888 8892117</li>
  </ul>

  <h2>Hébergement</h2>
  <p>Le site est hébergé sur une infrastructure européenne respectant le RGPD.</p>

  <h2>Propriété intellectuelle</h2>
  <p>L'ensemble des éléments présents sur ce site (textes, images, logos, chartes graphiques) est protégé par le droit de la propriété intellectuelle. Toute reproduction, représentation, modification, publication, adaptation sans autorisation préalable est interdite.</p>

  <h2>Droits d'auteur et contenus diffusés</h2>
  <p>TVPrime4K propose un service de streaming conforme aux réglementations européennes. Nous respectons les droits d'auteur et la propriété intellectuelle. L'utilisateur est responsable de l'utilisation du service conformément aux lois en vigueur dans son pays de résidence.</p>

  <h2>Responsabilité</h2>
  <p>Les informations présentes sur le site sont fournies à titre indicatif. TVPrime4K ne saurait être tenu responsable des erreurs ou omissions, ni des dommages directs ou indirects résultant de l'utilisation du site.</p>

  <h2>Contact</h2>
  <p>Pour toute question : <a href="mailto:contact@tvprime4k.com">contact@tvprime4k.com</a> ou WhatsApp au <a href="https://wa.me/4478888892117">+44 7888 8892117</a>.</p>
</article>
"""
    return page(
        title="Mentions légales — TVPrime4K",
        description="Mentions légales du site fr.tvprime4k.com — informations éditeur, hébergement, propriété intellectuelle.",
        canonical="https://fr.tvprime4k.com/mentions-legales/",
        body=body,
    )


def cgv_page():
    body = """<section class="breadcrumb">
  <div class="container"><a href="/">Accueil</a><span class="sep">/</span>CGV</div>
</section>
<article class="container prose">
  <h1>Conditions générales de vente</h1>
  <p>Les présentes Conditions Générales de Vente régissent les relations contractuelles entre TVPrime4K et toute personne physique ou morale souscrivant à un abonnement sur le site fr.tvprime4k.com.</p>

  <h2>1. Objet</h2>
  <p>TVPrime4K propose un service d'accès à des contenus de streaming vidéo via internet (IPTV), accessible par abonnement selon les formules présentées sur le site.</p>

  <h2>2. Formules et prix</h2>
  <p>Les tarifs sont indiqués en euros, toutes taxes comprises. Les formules disponibles — 3 mois, 6 mois, 12 mois, 24 mois, à vie — sont présentées sur la page <a href="/tarifs/">Tarifs</a>. Le prix affiché est le prix final : aucun frais caché, aucun prélèvement automatique.</p>

  <h2>3. Commande et paiement</h2>
  <p>La commande se fait via WhatsApp au <a href="https://wa.me/4478888892117">+44 7888 8892117</a>. Les moyens de paiement acceptés sont : PayPal, carte bancaire (Visa, Mastercard), virement SEPA, cryptomonnaie (Bitcoin, USDT).</p>

  <h2>4. Livraison</h2>
  <p>Après confirmation du paiement, les identifiants IPTV sont transmis par e-mail dans un délai de 5 à 15 minutes. Un guide d'installation est joint.</p>

  <h2>5. Garantie satisfait ou remboursé — 7 jours</h2>
  <p>Vous disposez d'un délai de 7 jours à compter de la réception de vos identifiants pour demander le remboursement intégral de votre abonnement, sans justification. La demande doit être envoyée par e-mail à contact@tvprime4k.com ou via WhatsApp. Le remboursement est effectué sous 48 à 72 heures ouvrées sur le moyen de paiement d'origine.</p>

  <h2>6. Durée et renouvellement</h2>
  <p>L'abonnement est valable pour la durée souscrite. Aucun renouvellement automatique n'est appliqué. Avant l'expiration, un e-mail de rappel est envoyé — le renouvellement est à l'initiative du client.</p>

  <h2>7. Obligations du client</h2>
  <p>Le client s'engage à utiliser le service pour un usage personnel et conformément aux lois en vigueur dans son pays de résidence.</p>

  <h2>8. Responsabilité</h2>
  <p>TVPrime4K met en œuvre les moyens techniques pour assurer la disponibilité du service, sans garantie de disponibilité ininterrompue en cas de maintenance, de pannes externes ou de force majeure.</p>

  <h2>9. Droit applicable</h2>
  <p>Les présentes CGV sont soumises au droit européen. Tout litige fera l'objet d'une tentative de règlement amiable avant toute procédure judiciaire.</p>

  <h2>10. Contact</h2>
  <p>Pour toute question : <a href="mailto:contact@tvprime4k.com">contact@tvprime4k.com</a>.</p>
</article>
"""
    return page(
        title="CGV — Conditions générales de vente | TVPrime4K",
        description="Conditions générales de vente TVPrime4K : formules, paiement, garantie 7 jours, renouvellement, responsabilités.",
        canonical="https://fr.tvprime4k.com/cgv/",
        body=body,
    )


def privacy_page():
    body = """<section class="breadcrumb">
  <div class="container"><a href="/">Accueil</a><span class="sep">/</span>Confidentialité</div>
</section>
<article class="container prose">
  <h1>Politique de confidentialité</h1>
  <p>TVPrime4K accorde une grande importance à la protection de vos données personnelles, conformément au Règlement Général sur la Protection des Données (RGPD).</p>

  <h2>Données collectées</h2>
  <p>Nous collectons uniquement les données nécessaires au traitement de votre commande :</p>
  <ul>
    <li>Adresse e-mail (pour l'envoi des identifiants IPTV)</li>
    <li>Numéro WhatsApp (pour le support)</li>
    <li>Données de paiement (traitées par nos prestataires sécurisés, non stockées sur nos serveurs)</li>
  </ul>

  <h2>Utilisation des données</h2>
  <p>Vos données sont utilisées exclusivement pour :</p>
  <ul>
    <li>Traiter votre commande et vous livrer vos identifiants</li>
    <li>Assurer le support client</li>
    <li>Vous envoyer un rappel avant l'expiration de votre abonnement</li>
  </ul>
  <p>Vos données ne sont jamais vendues ni cédées à des tiers à des fins commerciales.</p>

  <h2>Conservation</h2>
  <p>Les données de commande sont conservées pendant 3 ans à des fins de garantie et de support. Vous pouvez demander leur suppression à tout moment.</p>

  <h2>Vos droits</h2>
  <p>Conformément au RGPD, vous disposez des droits suivants :</p>
  <ul>
    <li>Droit d'accès à vos données</li>
    <li>Droit de rectification</li>
    <li>Droit à l'effacement</li>
    <li>Droit d'opposition au traitement</li>
    <li>Droit à la portabilité</li>
  </ul>
  <p>Pour exercer ces droits : <a href="mailto:contact@tvprime4k.com">contact@tvprime4k.com</a>.</p>

  <h2>Cookies</h2>
  <p>Le site utilise uniquement des cookies techniques (session) nécessaires à son fonctionnement. Aucun cookie publicitaire ou de tracking tiers n'est utilisé par défaut.</p>

  <h2>Sécurité</h2>
  <p>Toutes les communications passent par HTTPS. Les paiements sont traités par des prestataires certifiés PCI-DSS (PayPal, Stripe, etc.).</p>

  <h2>Contact DPO</h2>
  <p>Pour toute question relative à vos données personnelles : <a href="mailto:contact@tvprime4k.com">contact@tvprime4k.com</a>.</p>
</article>
"""
    return page(
        title="Politique de confidentialité — TVPrime4K",
        description="Politique de confidentialité TVPrime4K : données collectées, utilisation, conservation, vos droits RGPD.",
        canonical="https://fr.tvprime4k.com/confidentialite/",
        body=body,
    )


def not_found_page():
    body = f"""<section class="hero">
  <div class="container hero-inner" style="grid-template-columns: 1fr; text-align: center;">
    <div>
      <div class="eyebrow" style="justify-content: center;">Erreur 404</div>
      <h1 style="margin-bottom: 24px;">Cette page <em>n'existe pas</em></h1>
      <p class="hero-sub" style="margin: 0 auto 36px; text-align: center;">La page que vous cherchez a peut-être été déplacée ou n'existe plus. Revenez à l'accueil ou contactez-nous sur WhatsApp.</p>
      <div class="cta-row" style="justify-content: center;">
        <a href="/" class="btn btn-primary">Retour à l'accueil →</a>
        <a href="{wa("Bonjour, j'ai une question sur TVPrime4K.")}" class="btn btn-whatsapp" target="_blank" rel="noopener">💬 Nous contacter</a>
      </div>
    </div>
  </div>
</section>
"""
    return page(
        title="Page introuvable — TVPrime4K",
        description="La page que vous cherchez n'existe pas. Retour à l'accueil TVPrime4K.",
        canonical="https://fr.tvprime4k.com/404.html",
        body=body,
    )


# -----------------------------------------------------------------------------
# Build everything
# -----------------------------------------------------------------------------
def write(path: str, content: str):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print(f"  ✓ {path}")


def main():
    print("Building TVPrime4K FR static site…")

    # Supporting pages
    write("tarifs/index.html", tarifs_page())
    write("chaines/index.html", chaines_page())
    write("appareils/index.html", appareils_page())
    write("faq/index.html", faq_page())

    # City pages
    for city in CITIES:
        write(f"iptv-{city['slug']}/index.html", city_page(city))

    # Modifier pages
    for mod in MODIFIERS:
        write(f"{mod['slug']}/index.html", modifier_page(mod))

    # Legal
    write("mentions-legales/index.html", mentions_page())
    write("cgv/index.html", cgv_page())
    write("confidentialite/index.html", privacy_page())

    # 404
    write("404.html", not_found_page())

    print("Done.")


if __name__ == "__main__":
    main()
