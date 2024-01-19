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
