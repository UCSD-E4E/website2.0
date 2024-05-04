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
    1. Desktop - 1280x720 through 4096x2160
    2. Mobile - 360x640 through 414x896
    3. Tablet - 601x962 through 1280x800
17. The website SHOULD NOT depend on JavaScript for page content.
18. The website page content SHALL NOT exceed 15MB.
19. The website MUST maintain existing navigable page links.
20. The website SHOULD provide page view analytics.
21. The website MUST NOT require more than 1 hour per month of touch time for maintenance.

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

## Adding Expeditions
1. Open [_data/expeditions.yml](_data/expeditions.yml) in VS Code.
2. At the end of the file, add the following:
```
- project: {project_name}
  location: {expedition_location}
  date: {YYYY-MM}
  year: {YYYY}
  month: {MMMM}
  lead:
    - {lead1}
    - {lead2}
  people:
    - {member1}
    - {member2}
    - {member3}
# below fields are optional
  link: {URL to blog post/news about expedition}
  media:
    - {public links to published image/video galleries}
  data:
    - {links to dataset, can be private}
  properties:
  # for internal use only, see developers for more information
```
3. Commit the updated `.yml` file and push.

## Images
Images MUST be placed in the following location: `/assets/{project}/`

Images SHOULD be named `YYYY-MM-DD_description_of_image.ext`.  If a date is not relevant (for example, a logo), then the date may be omitted.

Images SHOULD be placed in the markdown using the following: `{{ relative_path_to_image_from_assets | resize: final_size,webp,80 | absolute_url }}`.  See https://imagemagick.org/script/command-line-processing.php#geometry for a full description of the resize argument.

## Project Pages
To make a section for a project, one must do the following:
- In `projects/projects.md` add a new json object to the blurbs array. This looks like:
```
 - photo: "assets/projects-new_project-photo.png"
   text: "Description of project"
   project_name: "Name of Project"
   link: "/insert-project-link"
```
Where photo is the filepath to the project's blurb photo, text is a short description of the project, the project_name is the name of the project, and link is the path in the url the project will live
- Create a new markdown file called `insert_name_of_project.md`. At the top add the following head:
```
---
layout: project
permalink: /insert-project-link
title: Name of Project
category: project-categories
enable_nav: false
---
```
Where permalink is the same value as link in projects.md, title is whatever you want to call the project, category is the tag representing your project (note: this should be the category used in future news posts associated with the project)

Set enable_nav to false for now and you have the mimumum needed to start creating your project

#### OPTIONAL: Add a gallery and project post feed
Some projects have the added feature of including a news feed containing posts about that project and a gallery to show up some important photos from diffrent events in the project. To add these pages do the following:

- Set enable_nav to true in your project.md file
- Add two new files: `insert_name_of_project-media.md` and `insert_name_of_project-updates.md`
- In `insert_name_of_project-media.md` add the following:
```
---
layout: gallery
permalink: /insert-project-link
title: Name of Project
category: project-categories
enable_nav: true
grid: true
media: 
 - assets/project-photo-1.png
 - assets/project-photo-2.png
 - assets/project-photo-3.png
 - ...
---
```
Here there are two new paramters that diffrent from `insert_name_of_project.md`. ALL OTHER PARAMETERS SHOULD BE IDENTICAL TO `insert_name_of_project.md`
- layout: set this to gallery
- grid: true/false this controls the style of the gallery. Please see [Galleries](### Galleries)
- media: an array of file paths to images you want to include

Your gallery page on the website will be found at `/insert-project-link/media`

- Next go to `insert_name_of_project-updates.md` and add the following text at the top of the file:
---
layout: post_feed
permalink: /insert-project-link
title: Name of Project
category: project-categories
enable_nav: true
---
Fill in permalink, title, and category with the same values used in the respective variables for `insert_name_of_project.md` and `insert_name_of_project-media.md`. Keep layout as post_feed. 

Your post feed page on the website will be found at `/insert-project-link/project-updates`


## Components (Includes)
Jeykll allows for components to be embedded in markdown files. See [https://jekyllrb.com/docs/includes/](https://jekyllrb.com/docs/includes/)

### Images with Caption
Up to 3 images can be place in a row with a caption below the image with text centered. The number of images placed depends on number of src paramters passed. Note if you are using only 2 images, src3 will have no effect and if you are only using 1 image, src2 and src3 will have no effect. 

Params:
- src: The path of the frist image. Should always be used.
- src2: The path of the second image. Should only be used if user wants 2 or more images
- src2: The path of the thrid image. Should only be used if user wants 3 images
- caption: Text to put under all images 

Format:
{% include img_caption.html 
    src="/abs/path/to/source/1"
    src2="/abs/path/to/source/2"
    src3="/abs/path/to/source/3"
    caption="Text to include"
%}

### Galleries
Creates a photo gallery in the page. This can be either in a grid format where all images are set to 200 by 200 photos with cropping, or not grid where the images attempt to maintain thier full size and aspect ratios. 

Gallaries require passing in a list of images. Liquid doesn't allow for directly creating the list in the includes statement. To make a list of images you can put the list into the yaml section of the markdown file and access the files through there. For example
```
---
layout: gallery
permalink: /acoustic-species-identification/media
title: Acoustic Species Identification
category: acoustic-species-identification
enable_nav: true
grid: true
media: 
 - assets/acoustic_species_id/white_winged_becard_vocalization.png
 - assets/acoustic_species_id/2021-08-04_scripps_coastal_reserve_trail.jpg
 - assets/acoustic_species_id/2021-08-10_audiomoth.jpg
 - assets/acoustic_species_id/2021-08-10_mugen_blue_looking_at_audiomoth.jpg
 - assets/acoustic_species_id/2021-08-10_jacob_placing_audiomoth.jpg
 - assets/acoustic_species_id/2021-08-10_expedition_team.jpg
 - assets/acoustic_species_id/2021-08-04_jacob_searching.jpg
 - assets/acoustic_species_id/audiomoth_acoustic_array.png
---
```
The images will be accessed through `page.media`

Params:
- media: Array of file paths
- grid: true for grid, false or none for not grid. 

Format:
{% include gallery_component.html 
    media=page.media 
    grid=true 
%}

### Project Navigation Bar
ONLY USED FOR PROJECT LAYOUTS. MUST NOT BE USED IN MARKDOWN FILES.

Creates the nav bar for project pages, namely the main project make, the project's update page, and the project's gallery page.

Params:
- title: Name of main page
- url: the url of the project. There are two ways to get this information
    - {% assign project_url = page.permalink | append: "/" %} if on main project page
    - url=page.dir this will select everything between the domain name and the file page in url
- enable_nav: true or false, some projects don't have a navbar

Format:
{% include project_navigation.html 
    title="INSERT TITLE"
    url=project_url 
    enable_nav=true or false 
%}

