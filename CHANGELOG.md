# Changelog

Versions describe the website, independently of its dependency versions. Dates and
tags are assigned when a release is verified on production, not when a PR merges.

## Unreleased

### 2.2.1 — Publishing and security maintenance

Prepared for the first formally tracked release; production deployment is not yet
verified. No historical deployment or release tag is implied.

- Replace the retired kastner-ml publishing hop with the campus e4e-website runner;
  add pinned infrastructure, convergence, and weekly system updates (#373).
- Align deployment with the tested Node 22 and image-tool setup (#374).
- Update jekyll-feed, jekyll-redirect-from, and jekyll-seo-tag with upstream security
  fixes (#370–372).
- Establish VERSION as the version source, display it in the footer, include it in
  deployment metadata, and add a verified-production release workflow.

## Retrospective change groups

These groups document work already merged. They are not claims that separate
numbered releases were deployed, and no backdated tags are created.

### 2.2.0 — Mangrove refresh

- Refresh the Mangrove page with accessible scrolling images (#365).

### 2.1.0 — Content and accessibility refresh

- Update recruitment, archived projects, contact details, alumni, spelling, and
  copyright information (#346–351, #353, #358–359).
- Improve gallery links, accessibility, heading hierarchy, and responsive
  presentation slides (#354, #357, #360–361, #368).
- Add media coverage to Publications (#364).
- Record deployed commits, align Ruby and cross-platform builds, exclude development
  files, and maintain dependencies and build tooling (#345, #352, #355–356,
  #362–363, #366–367).

### 2.0.0 — Historical baseline

- Website 2.0 before the October 2026 maintenance work (before #345–350).
