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

Couldn't test... even when working directly in the command line:

```
$ diffenator gfonts-qa/currently-hosted-fonts/ibmplexsanscondensed/IBMPlexSansCondensed-Bold.ttf IBM-Plex-Sans-Condensed/fonts/complete/ttf/IBMPlexSansCondensed-Bold.ttf -r gfonts-qa/currently-hosted-fonts/ibmplexsanscondensed/IBMPlexSansCondensed-Bold-diffs  -ol 200
-------------------------------------------------------------
INFO:diffenator.diff:'diff_nametable'  0.09 ms
INFO:diffenator.diff:'diff_attribs'  0.15 ms
INFO:diffenator.diff:'diff_glyphs'  1.77 ms
INFO:diffenator.diff:'diff_kerning'  212.96 ms
INFO:diffenator.diff:'diff_metrics'  1.26 ms
INFO:diffenator.diff:'diff_marks'  15.11 ms
INFO:diffenator.diff:'diff_marks'  0.54 ms
**Diffenator**
```

It did create the requested folder for output gifs, but this folder was empty.

#### Mono

Similar to Sans Condensed, diffenator didn't really check Mono styles.

```
$ diff-fonts gfonts-qa/currently-hosted-fonts/ibmplexmono IBM-Plex-Mono/fonts/complete/ttf
-------------------------------------------------------------
diffing IBMPlexMono-Bold.ttf
WARNING:diffenator.dump:Font doesn't have a GPOS kern feature
WARNING:diffenator.dump:Font doesn't have a GPOS kern feature
INFO:diffenator.diff:'diff_nametable'  0.10 ms
INFO:diffenator.diff:'diff_attribs'  0.15 ms
INFO:diffenator.diff:'diff_glyphs'  2.95 ms
INFO:diffenator.diff:'diff_kerning'  0.68 ms
INFO:diffenator.diff:'diff_metrics'  1.42 ms
INFO:diffenator.diff:'diff_marks'  19.13 ms
INFO:diffenator.diff:'diff_marks'  0.54 ms
**Diffenator**
```

#### Devanagari, Hebrew, Thai

These members of the Plex family will be completely new to Google Fonts.

## Diffbrowsers

Browser testing & Cross-platform testing:
https://github.com/googlefonts/diffbrowsers

Requires a BrowserStack account, so Marc will have to run these checks (or I could, with credentials).