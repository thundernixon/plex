# Regression testing before merge

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

## Diffbrowsers

Browser testing & Cross-platform testing:
https://github.com/googlefonts/diffbrowsers

Requires a BrowserStack account, so Marc will have to run these checks (or I could, with credentials).