# Website 2.0
## To Edit:
Please use https://vscode.dev/github/UCSD-E4E/website2.0

## Developer Get Started
1. Follow the instructions at https://jekyllrb.com/docs/installation/ to install the Jekyll generator on your machine.
2. Follow the instructions at http://www.graphicsmagick.org/README.html#installation to install GraphicsMagick on your machine.
3. Follow the instructions at https://docs.npmjs.com/downloading-and-installing-node-js-and-npm to install Node.js and npm on your machine
4. Run `npm ci` in this repository root
5. Run `bundle install` in this repository root
6. Run `npx gulp watch` in this repository root to deploy a live server to http://localhost:4000

~~Dev deployment target: https://ucsd-e4e.github.io/website2.0/~~

## Other gulp commands
- `npx gulp build` performs a single static build of the site
- `npx gulp build -j "<INSERT JEKYLL ARGS>"` creates a build of the site with custom jekyll arugments

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
