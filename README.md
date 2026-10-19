# Website 2.0
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
