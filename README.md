# Shopify Brand Insights (No Official Shopify API)

Scrapes a given Shopify storefront and returns a **Brand Context** JSON per the assignment:

- Whole Product Catalog (best-effort) ✅
- Hero Products (home page) ✅
- Privacy Policy (URL + excerpt) ✅
- Return / Refund Policies (URLs + excerpts) ✅
- Brand FAQs (URL + Q/A pairs when available) ✅
- Social Handles (IG, FB, TikTok, YouTube, X/Twitter) ✅
- Contact Details (emails, phones, contact page) ✅
- Brand Text Context (About URL + excerpt/meta) ✅
- Important Links (Order tracking, Contact us, Blog) ✅

**Error Contract**
- `401` if site is unreachable or not Shopify-like.
- `500` for internal errors.
- `400` if `website_url` missing.

## Run in GitHub Codespaces

1. Open the repo in Codespaces.
2. Terminal:
   ```bash
   python app.py
   You should then see something like: * Running on http://0.0.0.0:8000
   Once that appears:
	1.	In Codespaces, go to the PORTS tab.
	2.	Look for port 8000.
	3.	Click Open in Browser.
	4.	Add /static/index.html at the end of the URL to open the frontend.