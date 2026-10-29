# TanSan-gog(Personal) public information site

Canonical site: https://simon5530.github.io/

This repository contains only the public static app information, privacy policy
and terms for a personal Gog/OpenClaw integration. It contains no application
backend, OAuth callback endpoint, account data, OAuth client files or tokens.

## Current files and publishing

- `index.html`: app homepage; `privacy/index.html`: privacy policy;
  `terms/index.html`: terms; `style.css`: local stylesheet.
- `.nojekyll`: serve these files directly, without a build tool or dependencies.
- GitHub Pages source: `main` branch, `/` directory, HTTPS.
- `verify_site.py`: dependency-free local checks; run `python3 verify_site.py`.

Google branding URLs are the homepage, `/privacy/` and `/terms/` on the above
origin. The proposed authorized domain is `simon5530.github.io`, subject to actual
Google acceptance. Search Console ownership must be proved using Google's own
verification file or meta tag; never fabricate a verification token.

Publishing the site does not publish the OAuth application, verify its brand,
verify sensitive scopes, or prove that refresh tokens are free of Testing expiry.
Those require separate Google-side readback.

## Editing and verification

Edit these canonical files in place. Before publication, review the exact diff
for private content and scan both the tree and all reachable Git history with
Gitleaks. Verify local links and the deployed pages. Keep private operational
receipts, identities beyond the public GitHub owner, credentials and setup logs
outside this repository. No analytics, external fonts, scripts, forms or OAuth
callbacks should be added to this informational site.

The privacy policy is also an operating constraint: before sending Google API
data to any configured external processing service, confirm its settings and
terms meet Google's Limited Use requirements, including no general-purpose
model training. If unverified, stop that transfer; do not claim this static
policy alone enforces or certifies provider behavior.

Official references:

- https://support.google.com/cloud/answer/15549049
- https://support.google.com/cloud/answer/13464323
- https://support.google.com/webmasters/answer/9008080
- https://developers.google.com/terms/api-services-user-data-policy
- https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
