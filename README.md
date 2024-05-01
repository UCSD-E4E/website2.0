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
8. The website SHOULD have a time to first byte less than 200 ms when loaded in the US with a 100 Mbps link.
9. The website MUST allow users to easily post updates.
10. The website MUST allow programmatic generation of pages.
    1. For example, GitHub Actions should be able to edit and publish a page to reflect current expeditions, students, alumni, etc.
11. The website MUST automatically execute backups.
    1. The website SHOULD be able to store backups into the E4E NAS.
12. The website MUST automatically update software.
13. The website MUST allow users to easily edit pages.
14. The website MUST allow users to upload and publish images, videos, and documents.
15. The website MUST function on the following systems:
    1. Chrome (Current version and previous 3 months)
    2. FireFox (Current version and previous 3 months)
    3. Safari (Current version and previous 3 months)
16. The website MUST function on the following form factors:
    1. Desktop - 1280x720 through 1920x1080
    2. Mobile - 360x640 through 414x896
    3. Tablet - 601x962 through 1280x800
17. The website SHOULD NOT depend on JavaScript for page content.
18. The website page content SHALL NOT exceed 15MB.
19. The website MUST maintain existing navigable page links.
20. The website SHOULD provide page view analytics.
21. The website MUST NOT require more than 1 hour per month of touch time for maintenance.

## Developer Get Started
1. Follow the instructions at https://jekyllrb.com/docs/installation/ to install the Jekyll generator on your machine.
2. Run `jekyll serve --livereload --safe` in this repository root to deploy a live server to http://localhost:4000 or http://localhost:35729

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
