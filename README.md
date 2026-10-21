# Website 2.0

## Website versions and releases

`VERSION` is the single source for the website's stable `MAJOR.MINOR.PATCH`
version. Jekyll reads it into the footer; deployment records it alongside the
commit and timestamp in `last_deployed.txt`. Dependency versions are independent.

- **Major:** incompatible public URL, navigation, or content/data-format changes.
  Preserve existing URLs with redirects when possible.
- **Minor:** new pages/features or substantial backward-compatible improvements.
- **Patch:** content corrections, accessibility fixes, security/dependency updates,
  and build or publishing repairs.

Once activated, **Automatic website version** assigns one version to every merged
PR on `main`: patch by default, or minor/major with exactly one `version:minor` or
`version:major` PR label. `version:patch` is also accepted; conflicting/unknown
`version:*` labels fail validation. Closed, unmerged PRs consume no version.
Do not edit `VERSION` or `.github/versioning-state.json` by hand after activation.

The workflow reconciles merged PRs in `main`'s first-parent integration order and
commits `VERSION`, a linked changelog section per PR, and a processed-PR ledger.
Queued runs and retries cannot bump a PR twice. A run can catch up several PRs in
one metadata commit; each still receives its own version/changelog entry, while
the next build uses the latest version. Labels are read when a PR is first
processed; editing labels afterward does not rewrite assigned versions. Direct
pushes are recorded without consuming a PR version. Bot metadata commits do not
loop. The initial anchor is commit `5722091`; earlier PRs are not backfilled.

When enabled, the build workflow skips unprocessed `main` commits and builds the
App's metadata follow-up instead. Branch builds continue normally. Versioning
does not enable a disabled publishing workflow or publish a release tag. Deploy
`main`, verify the version/commit in the footer and `last_deployed.txt`, then run
**Release verified website** on that same commit. It still checks production
before creating `vX.Y.Z` and a GitHub Release. If `main` advances, deploy the new
commit first. Changelog versions are assignments, not claims of deployment.

### Activate automatic versioning (repository administrator)

The feature stays inactive until `AUTO_VERSIONING_ENABLED` is the literal `true`.
Until then, existing build/publish behavior is unchanged. This PR does not alter
repository settings, branch protections, or credentials.

1. Install a GitHub App for this repository with **Contents: read/write** and
   **Pull requests: read**. Configure Actions variable `APP_ID` and secret
   `APP_PRIVATE_KEY` (the same names used by the infrastructure pin workflow).
2. Permit that App to push to `main` and bypass the required-PR rule for its
   metadata commits. Keep human PR review requirements in place. These grants
   require an administrator; the default `GITHUB_TOKEN` cannot bypass protection.
   If the shared infrastructure App has broader access, prefer a dedicated App.
3. Enable **Automatic website version** and **Website versioning checks** if
   Actions workflows are disabled. Add **Website version policy** as a required PR
   check if desired, so conflicting version labels cannot merge. Create the optional
   `version:patch`, `version:minor`, and `version:major` labels before using them.
4. Set `AUTO_VERSIONING_ENABLED=true`, then manually dispatch **Automatic website
   version** on `main`. It catches up all PRs since the anchor, including this
   implementation PR, and its App-authenticated push triggers the normal build
   workflow if that workflow is enabled. No additional token or dispatch is used.
5. Verify the metadata commit, per-PR changelog sections, and build before relying
   on automatic publishing. A live merge/App-push test is required after setup;
   local tests cannot verify repository permissions or Actions activation.

If a run fails, fix the reported credentials/branch rules or PR labels and rerun
**Automatic website version**. Failed pushes never force-overwrite `main`; a
concurrent merge is fetched and recalculated. If repeated merges exhaust retries,
rerun the workflow. When enabled, version failures block a new site build rather
than deploying under an old version. Turning off the variable disables that gate
and restores the previous manual process; it does not roll back existing versions.

Run the local versioning tests with:

```sh
python3 -m unittest discover -s scripts -p 'test_auto_version.py'
```

Version 2.2.1 is the starting version for automation. Earlier 2.0.0–2.2.0 entries
are retrospective groupings, not claims of historical deployments or tags.

## To Edit:
Please use https://vscode.dev/github/UCSD-E4E/website2.0

## Developer Get Started
Use the Ruby version in `.ruby-version` (also used by CI) and the Bundler version in `Gemfile.lock`. Node.js, npm, and GraphicsMagick are also required.

### macOS and Linux
Install [rbenv and ruby-build](https://github.com/rbenv/rbenv#installation) and initialize rbenv in your shell. In this repository root:

```sh
rbenv install -s "$(cat .ruby-version)"
rbenv local "$(cat .ruby-version)"
gem install bundler -v 2.5.5
```

Install [Node.js and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) and [GraphicsMagick](http://www.graphicsmagick.org/README.html#installation) (plus ImageMagick for the image plugin) using your platform's package manager. Native gems may require compiler/build tools and development headers; follow your platform's Ruby installation prerequisites.

### Windows
Install [RubyInstaller with Devkit](https://rubyinstaller.org/downloads/) matching `.ruby-version`, run its `ridk install` setup, and install Node.js/npm and GraphicsMagick/ImageMagick. Ensure `ruby`, `bundle`, `node`, `npm`, and `gm` are available in a new terminal. Install Bundler with `gem install bundler -v 2.5.5`. The Windows-only `wdm` gem accelerates file watching; it is not required on macOS or Linux.

### Do I need make?

You do not run `make` to build or serve this website; use the Gulp commands below. However, installing Ruby or compiling native gems may require `make` and a compiler as part of your platform's build tools. Follow the [Jekyll installation prerequisites](https://jekyllrb.com/docs/installation/) and your Ruby installer's instructions rather than removing those tools.

### Build and serve
From this repository root:

```sh
npm ci
bundle _2.5.5_ install
npx gulp watch
```

Open http://localhost:4000. Run `npx gulp build` for a static build. If the lockfile's Bundler version changes, update the setup commands above to match it. The cross-platform build workflow verifies a clean installation with the configured Ruby version and GraphicsMagick.

~~Dev deployment target: https://ucsd-e4e.github.io/website2.0/~~

## Other gulp commands
- `npx gulp build` performs a single static build of the site
- `npx gulp build -j "<INSERT JEKYLL ARGS>"` creates a build of the site with custom jekyll arguments

## Checking hyperlinks
After building, run `python3 scripts/check_relative_links.py _site`. Internal hyperlinks must start with `/` (use Jekyll's `relative_url` or `absolute_url` filter). Fragment and query-only links, external URLs, and schemes such as `mailto:` are allowed. The check reports the generated page and line for each document-relative hyperlink.

Run the checker tests with `python3 -m unittest discover -s scripts -p 'test_*.py'`.

## Adding blog posts
Create a new file in `/_posts` with the following name: `{year}-{month}-{day}-{hyphenated-title}.md`.  For example: `2024-05-10-e4e-releases-new-jekyll-website.md`.

At the top of the file, add the following:
```
---
date: {year}-{month}-{day} {hour}:{minute}-{timezone offset}:00
layout: blog-post
title: {title}
categories:
 - news-and-updates
author: {your name}
featuredImage: {relative path to featured image}
tags:
- {additional tags}
---
```

For example:
```
---
date: 2024-05-07 21:45-07:00
layout: blog-post
title: Ronan Wallace Awarded Fulbright for Floods of Lubra
categories:
 - news-and-updates
author: Nathan Hui
featuredImage: assets/floods_of_lubra/fieldwork-nepal.jpg
tags:
- floods-of-lubra
- fulbright
---
```

Add the contents of your blog post after this preable, using the appropriate components.

Commit this and any included images to a new branch (we recommend using the same format as the blob post file name).  Request a review from one of the website admins and enable auto merge.

See also https://github.com/UCSD-E4E/website2.0/wiki
