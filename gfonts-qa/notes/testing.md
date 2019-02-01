# Regression testing before merge

## FontBakery

Marc: it's not going to pass fontbakery; they have separate standards
- run every new static ttf against the ones we serve in diff browser
- just check for regressions/updates


## Diffenator

Testing at http://159.65.243.73/

- [ ] testing sans


### Results show...

#### Sans
- There is a new "Text" weight
- The new fonts have many new glyphs, in particular, Greek
- The new fonts have much-improved placement of accents (see [marks_new.gif](gfonts-qa/currently-hosted-fonts/ibmplexsans/IBMPlexSans-SemiBold-diff_gifs/marks_new.gif))
- The new fonts have kerning between more pairs
- The new fonts make small refinements, e.g. the /gcaron uses a low-eared /g as a base to be more legible


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

## Diffbrowsers

https://github.com/googlefonts/diffbrowsers

## Browser testing? Cross-platform testing?