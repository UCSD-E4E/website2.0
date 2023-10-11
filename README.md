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
8. The website SHOULD have a time to first byte less than 200 ms.
9. The website MUST allow users to easily post updates.
10. The website MUST allow programmatic generation of pages.
    1. For example, GitHub Actions should be able to edit and publish a page to reflect current expeditions, students, alumni, etc.
11. The website MUST automatically execute backups.
    1. The website SHOULD be able to store backups into the E4E NAS.
12. The website MUST automatically update software.
13. The website MUST allow users to easily edit pages.
14. The website MUST allow users to upload and publish images, videos, and documents.
15. The website MUST function on the following systems:
    1. Chrome (Current version and previous)
    2. FireFox (Current version and previous)
    3. Safari (Current version and previous)
16. The website MUST function on the following form factors:
    1. Desktop - 1280x720 through 1920x1080
    2. Mobile - 360x640 through 414x896
    3. Tablet - 601x962 through 1280x800
17. The website MUST NOT depend on JavaScript for page content.
18. The website page content SHALL NOT exceed 15MB.
19. The website MUST maintain existing links.
20. The website SHOULD provide page view analytics.
21. The website MUST NOT require more than 1 hour per month of touch time for maintenance.
