# example from https://github.com/googlefonts/fontdiffenator

from diffenator import DiffFonts
from diffenator.font import InputFont

font_a = InputFont('IBM-Plex-Sans/fonts/complete/ttf/IBMPlexSans-Bold.ttf')
font_b = InputFont(
    'gfonts-qa/currently-hosted-fonts/ibmplexsans/IBMPlexSans-Bold.ttf')
DiffFonts(font_a, font_b)

# for font in newfolder:
#   find font of same name in oldFolder
#   then make diff
#
# save diff to unique directory?


# def main():
#     parser = argparse.ArgumentParser(description=__doc__)
#     parser.add_argument("--folder", nargs="+", required=True)
#     args = parser.parse_args()

#     for font in args.fonts:
#         ttfont = TTFont(font)
#         fix_isFixedPitch(ttfont)

#         new_font = font + ".fix"
#         print("Saving font to {}".format(new_font))
#         ttfont.save(new_font)


# if __name__ == "__main__":
#     main()
