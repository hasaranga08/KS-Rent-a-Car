# KS Rent a Car Sri Lanka Website

A clean, modern, mobile-first, and responsive static website for **KS Rent a Car Sri Lanka** ([https://www.srilankacarrents.com](https://www.srilankacarrents.com)).

## Features
- **Zero Runtime Dependencies**: Standard static HTML5, CSS3, and modern vanilla JavaScript. No Node.js, PHP, or database required for deployment.
- **Mobile-First Responsive Design**: Optimized for smartphones, tablets, and desktops with smooth navigation and touch-friendly targets.
- **Direct WhatsApp Integration**: Pre-configured WhatsApp contact buttons pointing directly to `+94 77 719 3915`.
- **Formspree Quotation & Enquiry Form**: Client-side validated rental enquiry form with automated WhatsApp fallback.
- **Comprehensive Fleet & Services Pages**:
  - `index.html`: Homepage featuring hero banner, quick quote finder, popular fleet, services, trust badges, FAQ preview, and enquiry form.
  - `vehicles.html`: Detailed vehicle catalog featuring Toyota Premio, Allion 260/240, Honda Vezel, Toyota IST, Suzuki WagonR, Toyota Raize, Toyota KDH (Flat & High Roof), and Honda Fit.
  - `services.html`: Self-drive, Chauffeur-driven, Airport transfers, Long-term & Short-term rentals, and Tourist transportation.
  - `wedding-car-hire.html`: Dedicated wedding car packages, luxury sedans, and guest vans.
  - `about.html`: Company overview, standards, and islandwide delivery coverage.
  - `faq.html`: 12 comprehensive questions and answers with Schema.org `FAQPage` structured data.
  - `contact.html`: Contact directory, business information, and enquiry form.
  - `privacy-policy.html`: Customer privacy terms.
  - `terms.html`: Rental terms, licensing details, and driver requirements.
- **SEO & Social Optimization**: OpenGraph metadata, Twitter cards, meta descriptions, semantic headings, canonical tags, `sitemap.xml`, and `robots.txt`.

---

## Configuration & Placeholders

Search and replace the following placeholder tokens across the HTML files:

| Placeholder | Location | Description |
|---|---|---|
| `FORM_ENDPOINT` | Configured across all enquiry forms | Active Formspree endpoint: `https://formspree.io/f/mkjgbonn` |
| `BUSINESS_EMAIL_HERE` | `contact.html` | Your official business email address (e.g., `info@srilankacarrents.com`) |
| `BUSINESS_ADDRESS_HERE` | `contact.html` | Your registered office address in Sri Lanka (e.g., Colombo / Katunayake) |

### Updating WhatsApp Number
The WhatsApp number `+94 77 719 3915` is linked as `https://wa.me/94777193915`. To change it, find `94777193915` and replace with your new country code and phone digits.

### Replacing Vehicle Images
Place high-resolution photos of your fleet in `assets/images/vehicles/` using the following filenames:
- `toyota premio.jpg`
- `toyota allion 260.jpg`
- `toyota allion 240.jpg`
- `honda-vezel.jpg`
- `toyota-ist.jpg`
- `suzuki-wagon-r.jpg`
- `toyota-raize.jpg`
- `toyota-kdh-flat-roof.jpg`
- `toyota-kdh-high-roof.jpg`
- `honda-fit.jpg`

---

## Deployment Instructions

### Option 1: cPanel File Manager (Shared Hosting)
1. Log in to your cPanel hosting account.
2. Open **File Manager** and navigate to the root web folder (usually `public_html` or the folder for `srilankacarrents.com`).
3. Upload all the files and folders:
   - `index.html`
   - `vehicles.html`
   - `services.html`
   - `wedding-car-hire.html`
   - `about.html`
   - `faq.html`
   - `contact.html`
   - `privacy-policy.html`
   - `terms.html`
   - `robots.txt`
   - `sitemap.xml`
   - `favicon.svg`
   - `assets/` folder (including `css/`, `js/`, and `images/`)
4. Verify that file permissions for HTML files are set to `0644` and folders to `0755`.
5. Visit `https://www.srilankacarrents.com` in your browser.

### Option 2: GitHub Pages
1. Create a repository on GitHub (e.g., `srilankacarrents` or `username.github.io`).
2. Push all the static files to the `main` or `gh-pages` branch.
3. In GitHub, navigate to **Settings** > **Pages**.
4. Under **Branch**, select `main` (root) and click **Save**.
5. If using a custom domain (`srilankacarrents.com`):
   - Enter `srilankacarrents.com` under **Custom domain** and save.
   - Configure your DNS provider with the GitHub Pages A records (`185.199.108.153`, etc.) or CNAME record.
   - Check **Enforce HTTPS**.

---

## Local Development & Preview
To run the local preview using Vite:
```bash
npm install
npm run build
```
The output files will be compiled cleanly into the `dist/` directory, ready to copy or deploy anywhere.
