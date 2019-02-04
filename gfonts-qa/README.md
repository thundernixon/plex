# Regression testing before merge

PR at https://github.com/google/fonts/pull/1837

## FontBakery

Marc: it's not going to pass fontbakery; they have separate standards
- run every new static ttf against the ones we serve in diff browser
- just check for regressions/updates

## Diffenator

### Results show...

#### Sans
- There is a new "Text" weight
- The new fonts have many new glyphs, in particular, Greek
- The new fonts have much-improved placement of accents (see [marks_new.gif](gfonts-qa/currently-hosted-fonts/ibmplexsans/IBMPlexSans-SemiBold-diff_gifs/marks_new.gif))
- The new fonts have kerning between more pairs
- The new fonts make small refinements, e.g. the /gcaron uses a low-eared /g as a base to be more legible

#### Serif

- Similar readability refinements
- Added Text weight
- Glyphs appear to be slightly lighter in weight
- Only three new glyphs, rather than entire Greek alphabet as Sans has


#### Sans Condensed

Almost no changes

#### Mono

Similar to Sans Condensed, there are almost no changes here.

#### Devanagari, Hebrew, Thai

These members of the Plex family will be completely new to Google Fonts.


## Adding fonts to `google/fonts/ofl` directory

### Question 1: should `METADATA.pb` be modified to include "Text" weights?

I'm adding the fonts to the `google/fonts/ofl` directory, then running `gftools add-font` on the updated folders. The language subsets expanded in Plex Sans to include `subsets: "greek"`, but otherwise, the `METADATA` files are untouched aside from the addition of "Text" styles.

One caveat: `add-font` doesn't allow the "Text" weight that is now included in the fonts, so I am manually adding this to the `METADATA.pb` files.

I am setting the `weight` value as `450`, because this is the weight IBM has specified for this style: [Plex weights, used to generate CSS releases](https://github.com/IBM/plex/blob/80846f5512975b75ff76c7c122159b2a910a5174/scripts/data/weights.js).


```
fonts {
  name: "IBM Plex Sans Condensed"
  style: "normal"
  weight: 450
  filename: "IBMPlexSansCondensed-Text.ttf"
  post_script_name: "IBMPlexSansCond-Text"
  full_name: "IBM Plex Sans Condensed Text"
  copyright: "Copyright 2018 IBM Corp. All rights reserved."
}
fonts {
  name: "IBM Plex Sans Condensed"
  style: "italic"
  weight: 450
  filename: "IBMPlexSansCondensed-TextItalic.ttf"
  post_script_name: "IBMPlexSansCond-TextItalic"
  full_name: "IBM Plex Sans Condensed Text Italic"
  copyright: "Copyright 2018 IBM Corp. All rights reserved."
}
```

I assume these are important styles to include in the metadata, but if it will break things, I can remove these blocks.

**UPDATE: The current API doesn't support intermediate weights, so I had to reverse this.** 

### Question 2: Should the `description` HTML be modified to link to new Devanagari, Thai, and Hebrew versions of Plex?

Plex has new versions. Should these be called out in the `description` HTML, or is it good to leave the description as-is? What about for these new families, in which the description is copied over from Plex Sans?

I think it still works well as-is, but if it seems useful to update the descriptions, I can do so.


## Diffbrowsers

Browser testing & Cross-platform testing:
https://github.com/googlefonts/diffbrowsers

Requires a BrowserStack account, so Marc will have to run these checks (or I could, with credentials).