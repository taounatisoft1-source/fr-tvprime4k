/* ==========================================================================
   TVPrime4K FR — Shared JavaScript
   Pricing engine · FAQ · Nav · Exit intent · Promo bar
   ========================================================================== */

(function () {
  "use strict";

  /* ---------- Config ---------- */
  const WA_NUMBER = "4478888892117";
  const PRICING = {
    standard: {
      1: { 1: 9.99,  3: 19.99, 6: 29.99, 12: 49.99, 24: 79.99 },
      2: { 1: 14.99, 3: 29.99, 6: 44.99, 12: 74.99, 24: 119.99 },
      3: { 1: 19.99, 3: 39.99, 6: 59.99, 12: 99.99, 24: 159.99 },
      4: { 1: 24.99, 3: 49.99, 6: 74.99, 12: 124.99, 24: 199.99 }
    },
    premium: {
      1: { 1: 12.99, 3: 23.99, 6: 36.99, 12: 59.99, 24: 99.99 },
      2: { 1: 19.99, 3: 34.99, 6: 54.99, 12: 89.99, 24: 149.99 },
      3: { 1: 24.99, 3: 44.99, 6: 74.99, 12: 119.99, 24: 199.99 },
      4: { 1: 29.99, 3: 54.99, 6: 89.99, 12: 149.99, 24: 249.99 }
    }
  };

  const DURATIONS = [
    { months: 1, label: "1 mois" },
    { months: 3, label: "3 mois" },
    { months: 6, label: "6 mois" },
    { months: 12, label: "12 mois", popular: true },
    { months: 24, label: "24 mois" }
  ];

  const STANDARD_FEATURES = [
    "+55 000 chaînes & +90 000 VOD",
    "Qualité SD / HD / Full HD / 4K",
    "Serveurs rapides et stables",
    "Contenu mis à jour chaque jour",
    "Compatible tous les appareils",
    "Garantie 7 jours satisfait ou remboursé"
  ];

  const PREMIUM_FEATURES = [
    "Serveur Premium — ultra-stable",
    "Catalogue VOD élargi",
    "+55 000 chaînes & VOD Premium",
    "Qualité SD / HD / Full HD / 4K",
    "Priorité sur serveurs Premium",
    "Compatible tous les appareils",
    "Garantie 7 jours satisfait ou remboursé"
  ];

  /* ---------- Helpers ---------- */
  function fmtPrice(n) { return n.toFixed(2).replace(".", ","); }

  function waLink(message) {
    return `https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(message)}`;
  }

  function orderMessage(duration, screens, server, price) {
    const serverLabel = server === "premium" ? " SERVEUR PREMIUM" : "";
    const screensLabel = screens > 1 ? ` ${screens} écrans` : " 1 écran";
    return `Bonjour, je viens de passer une commande sur votre site.\n\nProduit: FORFAIT ${duration} MOIS${serverLabel} —${screensLabel}\nPrix: ${fmtPrice(price)}€\n\nJe souhaite finaliser mon paiement. Merci !`;
  }

  /* ---------- Pricing table (optional per page) ---------- */
  function initPricing() {
    const grid = document.getElementById("plansGrid");
    const serverToggle = document.getElementById("serverToggle");
    const screensToggle = document.getElementById("screensToggle");
    if (!grid) return;

    let currentServer = "standard";
    let currentScreens = 1;

    function render() {
      const features = currentServer === "premium" ? PREMIUM_FEATURES : STANDARD_FEATURES;
      grid.innerHTML = DURATIONS.map(d => {
        const price = PRICING[currentServer][currentScreens][d.months];
        const monthly = (price / d.months).toFixed(2).replace(".", ",");
        const popularClass = d.popular ? " popular" : "";
        const badge = d.popular ? '<div class="plan-badge">🔥 Le plus populaire</div>' : "";
        const featuresList = features.map(f => `<li>${f}</li>`).join("");
        const [whole, decimal] = fmtPrice(price).split(",");
        const link = waLink(orderMessage(d.months, currentScreens, currentServer, price));
        return `
          <div class="plan${popularClass}">
            ${badge}
            <div class="plan-duration">${currentScreens === 1 ? "1 écran" : currentScreens + " écrans"}${currentServer === "premium" ? " · Premium" : ""}</div>
            <div class="plan-name">${d.label}</div>
            <div class="plan-price"><span class="amount">${whole}</span><span class="currency">,${decimal}€</span></div>
            <div class="plan-per">soit ~${monthly}€/mois · paiement unique</div>
            <ul class="plan-features">${featuresList}</ul>
            <a href="${link}" class="plan-btn" target="_blank" rel="noopener">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01S14.69 2 12.04 2z"/></svg>
              Commander
            </a>
            <div class="plan-foot">Paiement sécurisé · Activation 10 min</div>
          </div>
        `;
      }).join("");
    }

    if (serverToggle) {
      serverToggle.addEventListener("click", e => {
        const btn = e.target.closest(".toggle-btn");
        if (!btn) return;
        serverToggle.querySelectorAll(".toggle-btn").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        currentServer = btn.dataset.server;
        render();
      });
    }
    if (screensToggle) {
      screensToggle.addEventListener("click", e => {
        const btn = e.target.closest(".toggle-btn");
        if (!btn) return;
        screensToggle.querySelectorAll(".toggle-btn").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        currentScreens = parseInt(btn.dataset.screens, 10);
        render();
      });
    }

    render();
  }

  /* ---------- FAQ accordion ---------- */
  function initFAQ() {
    const list = document.getElementById("faqList");
    if (!list) return;
    list.addEventListener("click", e => {
      const q = e.target.closest(".faq-q");
      if (!q) return;
      q.parentElement.classList.toggle("open");
    });
  }

  /* ---------- Nav mobile toggle ---------- */
  function initNav() {
    const toggle = document.getElementById("navToggle");
    const links = document.getElementById("navLinks");
    if (!toggle || !links) return;
    toggle.addEventListener("click", () => links.classList.toggle("open"));
    links.addEventListener("click", e => {
      if (e.target.closest("a")) links.classList.remove("open");
    });
  }

  /* ---------- Promo bar close ---------- */
  function initPromo() {
    const bar = document.getElementById("promoBar");
    const close = document.getElementById("promoClose");
    if (!bar || !close) return;
    try {
      if (sessionStorage.getItem("tvp_promo_closed") === "1") bar.hidden = true;
    } catch (e) {}
    close.addEventListener("click", () => {
      bar.hidden = true;
      try { sessionStorage.setItem("tvp_promo_closed", "1"); } catch (e) {}
    });
  }

  /* ---------- Exit intent modal ---------- */
  function initExitIntent() {
    const modal = document.getElementById("exitModal");
    if (!modal) return;
    let shown = false;
    try {
      if (sessionStorage.getItem("tvp_modal_shown") === "1") shown = true;
    } catch (e) {}

    function show() {
      if (shown) return;
      shown = true;
      try { sessionStorage.setItem("tvp_modal_shown", "1"); } catch (e) {}
      modal.classList.add("open");
    }
    function hide() { modal.classList.remove("open"); }

    document.addEventListener("mouseout", e => {
      if (!e.relatedTarget && e.clientY <= 0) show();
    });

    let timer = null;
    if (window.innerWidth <= 820) {
      window.addEventListener("scroll", () => {
        if (shown || timer) return;
        const depth = (window.scrollY + window.innerHeight) / document.documentElement.scrollHeight;
        if (depth > 0.4) timer = setTimeout(show, 25000);
      }, { passive: true });
    }

    modal.addEventListener("click", e => {
      if (e.target === modal || e.target.closest("[data-close]")) hide();
    });
    document.addEventListener("keydown", e => {
      if (e.key === "Escape") hide();
    });
  }

  /* ---------- Smooth anchors ---------- */
  function initAnchors() {
    document.addEventListener("click", e => {
      const a = e.target.closest('a[href^="#"]');
      if (!a) return;
      const id = a.getAttribute("href").slice(1);
      if (!id) return;
      const el = document.getElementById(id);
      if (!el) return;
      e.preventDefault();
      el.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  }

  /* ---------- Boot ---------- */
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
  function boot() {
    initPricing();
    initFAQ();
    initNav();
    initPromo();
    initExitIntent();
    initAnchors();
  }
})();
