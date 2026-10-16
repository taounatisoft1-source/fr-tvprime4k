# TVPrime4K FR — Site statique

Landing page française pour **fr.tvprime4k.com** — site statique prêt à déployer sur n'importe quel hébergeur (Hostinger, OVH, SiteGround, Cloudflare Pages, Netlify, Vercel…).

## Structure

```
fr-tvprime4k/
├── index.html                        # Page d'accueil principale (13 sections)
├── 404.html
├── sitemap.xml
├── robots.txt
├── .htaccess                         # Config Apache
├── nginx.conf.example                # Config Nginx (référence)
├── _build.py                         # Builder des sous-pages (ne pas déployer)
│
├── assets/
│   ├── css/main.css                  # Styles partagés
│   ├── js/main.js                    # JS partagé (tarifs, FAQ, modal, nav)
│   └── img/
│       ├── favicon.svg
│       ├── logo.svg
│       └── og-image.svg
│
├── tarifs/index.html                 # Tarifs & formules
├── chaines/index.html                # Liste des chaînes
├── appareils/index.html              # Appareils compatibles
├── faq/index.html                    # FAQ étendue (12 questions)
│
├── iptv-paris/index.html             # Pages villes (SEO local)
├── iptv-lyon/index.html
├── iptv-marseille/index.html
│
├── iptv-sport-france/index.html      # Pages modificateurs (SEO long-tail)
├── iptv-4k-france/index.html
├── iptv-pas-cher/index.html
│
├── mentions-legales/index.html       # Pages légales
├── cgv/index.html
└── confidentialite/index.html
```

## Déploiement rapide

### Option 1 — Hostinger / cPanel / FTP (recommandé)

1. Zippe le dossier `fr-tvprime4k/` (sans `_build.py`)
2. Dans hPanel Hostinger : **File Manager → public_html** (ou le dossier de votre sous-domaine `fr.tvprime4k.com`)
3. Upload le zip et extraction sur place
4. Vérifie que `.htaccess` est bien à la racine (fichier caché — active l'affichage dans ton gestionnaire de fichiers)
5. Vérifie que le certificat SSL est actif pour `fr.tvprime4k.com`
6. Visite https://fr.tvprime4k.com — ça doit charger

### Option 2 — Cloudflare Pages / Netlify / Vercel (gratuit)

1. Pousse le dossier sur un repo Git (GitHub, GitLab)
2. Connecte Cloudflare Pages / Netlify / Vercel au repo
3. Build command: *(aucune — c'est du statique)*
4. Publish directory: `/` (la racine du repo)
5. Configure le domaine custom `fr.tvprime4k.com` dans le dashboard
6. Les redirections 301, headers et pretty URLs sont déjà pris en charge par ces plateformes

### Option 3 — VPS Nginx

1. Rsync le dossier vers `/var/www/fr.tvprime4k.com/`
2. Copie `nginx.conf.example` vers `/etc/nginx/sites-available/fr.tvprime4k.com`
3. Ajuste les chemins SSL (certificat Let's Encrypt via certbot)
4. `sudo ln -s /etc/nginx/sites-available/fr.tvprime4k.com /etc/nginx/sites-enabled/`
5. `sudo nginx -t && sudo systemctl reload nginx`

## Configuration DNS

Chez votre registrar (OVH, Namecheap, Cloudflare…), pour le domaine `tvprime4k.com` :

```
Type   Nom   Valeur
A      fr    <IP de votre serveur>
```

Ou si vous êtes derrière Cloudflare, utilisez un CNAME vers votre endpoint :

```
Type   Nom   Valeur
CNAME  fr    votre-site.pages.dev
```

Attendez 1–24h pour la propagation DNS.

## Modifier le contenu

### Numéro WhatsApp et email

Les deux sont codés en dur. Pour les changer :

1. **Numéro WhatsApp** — remplacer `4478888892117` dans :
   - `index.html` (plusieurs occurrences)
   - `_build.py` → constante `WA` en haut du fichier
   - `assets/js/main.js` → constante `WA_NUMBER`
   - Puis relancer `python3 _build.py` pour régénérer les sous-pages

2. **Email** — remplacer `contact@tvprime4k.com` dans :
   - `index.html`
   - `_build.py` → constante `EMAIL`
   - Relancer le build

### Prix

Prix tous définis dans `assets/js/main.js` → objet `PRICING`. Modifiez les valeurs et rechargez — la page recalculera tout automatiquement.

### Ajouter une page ville ou modifier

Dans `_build.py`, ajoutez une entrée au tableau `CITIES` ou `MODIFIERS`, puis :

```bash
python3 _build.py
```

La nouvelle page apparaît automatiquement avec le bon template. Pensez à l'ajouter à `sitemap.xml` et aux liens du footer.

## SEO — Prochaines étapes

Le site est pré-optimisé mais quelques actions manuelles restent :

1. **Google Search Console** — ajouter la propriété `fr.tvprime4k.com`, soumettre `sitemap.xml`
2. **Google Analytics** — insérer le code GA4 avant `</head>` dans `index.html` et les sous-pages
3. **Meta Pixel / TikTok Pixel** — même méthode si vous faites de la pub sociale
4. **Trustpilot ou Avis Vérifiés** — installer le widget pour générer les avis clients et activer les étoiles dans les résultats Google
5. **hreflang** — déjà configuré pour `.com`, `.de`, `.fr`. Vérifier que les trois domaines pointent bien les uns vers les autres (reciprocal)
6. **Guest posts** — placer 2-3 articles sponsorisés sur `lepetitjournal.com` / `presseagence.fr` (voir doc Research)

## Développement local

```bash
# Lancer un serveur local pour prévisualiser
cd fr-tvprime4k
python3 -m http.server 8000

# Puis ouvrir http://localhost:8000
```

## Fichiers à ne pas déployer

- `_build.py` — bloqué par `.htaccess` et `nginx.conf.example`, mais ne le pushez pas en production si vous le pouvez
- `README.md` — pas critique, mais inutile en prod

## Support

Toute question ou modification : repasser sur la conversation Claude pour itérer.

---
© 2026 TVPrime4K
