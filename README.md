# Website 2.0
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119).
## Requirements
1. Users with administrative access MUST authenticate with multi-factor authentication.
2. User accounts MUST have expiration dates.
3. Individual users MUST have individual accounts.
4. The website MUST support HTTPS and an Organizational Validation certificate.
6. The website MUST allow for redirections.
    1. For example, https://e4e.ucsd.edu/join should redirect to https://docs.google.com/forms/d/e/1FAIpQLSdOa1xcK2mxjnEoOLQB_A0a0ERnyT_AGwdaxqG06R9meXnT5g/viewform.
7. The website SHOULD have less than 300 ms load time when loaded in the US with a 100 Mbps link.
8. The website MUST allow users to easily post updates.
9. The website MUST allow programmatic generation of pages.
    1. For example, GitHub Actions should be able to edit and publish a page to reflect current expeditions, students, alumni, etc.
10. The website MUST automatically execute backups.
    1. The website SHOULD be able to store backups into the E4E NAS.
11. The website MUST automatically update software.
12. The website MUST allow users to easily edit pages.
13. The website MUST allow users to upload and publish images, videos, and documents.
14. The website MUST function on the following systems:
    1. Chrome
    2. FireFox
    3. Safari
15. The website MUST NOT require more than 1 hour per month of touch time for maintenance.

## Developer Get Started
1. Follow the instructions at https://jekyllrb.com/docs/installation/ to install the Jekyll generator on your machine.
2. Follow the instructions at http://www.graphicsmagick.org/README.html#installation to install GraphicsMagick on your machine.
3. Run `bundle exec jekyll serve --livereload` in this repository root to deploy a live server to http://localhost:4000

Dev deployment target: https://ucsd-e4e.github.io/website2.0/

## Adding Publications
1. Open [_bibliography/publications.bib](_bibliography/publications.bib) in [JabRef](https://www.jabref.org/).
2. Add the new publication using the correct classification
    1. Books should use `@Book`
    2. PhD theses should `@PhdThesis` with `type` set to `PhD Thesis`
    3. MS theses should use `@MastersThesis` with `type` set to `MS Thesis`
    4. Patents should use `@Patent` with `number` set to the full US Patent number (e.g. `US0123456789`)
    5. Book chapters should use `@InBook`
    6. Conference papers should use `@InProceedings`
    7. Journal articles should use `@Article`
    8. All papers should include their abstract and keywords.
    9. All papers should include their DOI reference (if available).
    10. Where possible, include the non-DOI permalink to the article in the `url` field.
    11. If a copy is available on arXiV, please include the arXiV identifier in the `preprint` field.
3. Commit the updated `.bib` file and push to `main`