#!/usr/bin/env python3
"""Render the site's 'VR' favicon in EB Garamond, the heading face.

One mark for every context: the ground is the site's terracotta accent, which
holds its edge against both light and dark browser chrome, so there's no need
for a light/dark pair (and none of the `media`-on-icon-link fragility that
came with one).

Writes a 32px PNG, a 180px apple-touch-icon, and a multi-size favicon.ico at
the site root so the browser's automatic /favicon.ico request is satisfied.
Drawn supersampled at 512px and downsampled so the serif stems survive at tab
size.

After running this, bump `favicon_version` in _config.yml — browsers cache
favicons far more stubbornly than they cache pages.

Usage: python3 scripts/make_favicon.py   (needs Pillow and EB Garamond)
"""
import pathlib
import sys

from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/truetype/ebgaramond/EBGaramond12-Bold.ttf"
SS = 512           # supersampled canvas
TEXT = "VR"
RADIUS = 0.20      # corner radius as a fraction of the canvas
FILL_W = 0.68      # target glyph width as a fraction of the canvas

GROUND = (168, 90, 58, 255)   # #a85a3a, the site's accent
INK = (248, 246, 241, 255)    # #f8f6f1, the site's paper

REPO = pathlib.Path(__file__).resolve().parent.parent


def fit_font(draw, target_w):
    """Largest font size whose rendered TEXT fits target_w."""
    lo, hi = 8, SS
    while lo < hi:
        mid = (lo + hi + 1) // 2
        f = ImageFont.truetype(FONT, mid)
        box = draw.textbbox((0, 0), TEXT, font=f)
        if box[2] - box[0] <= target_w:
            lo = mid
        else:
            hi = mid - 1
    return ImageFont.truetype(FONT, lo)


def main():
    if not pathlib.Path(FONT).exists():
        sys.exit(f"font not found: {FONT}\nInstall EB Garamond or edit FONT.")

    img = Image.new("RGBA", (SS, SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, SS - 1, SS - 1], radius=int(SS * RADIUS), fill=GROUND)

    font = fit_font(d, SS * FILL_W)
    # Centre on the ink bbox rather than the font's line box, so the optical
    # centre of the glyphs lands in the middle of the square.
    l, t, r, b = d.textbbox((0, 0), TEXT, font=font)
    d.text(((SS - (r - l)) / 2 - l, (SS - (b - t)) / 2 - t), TEXT, font=font, fill=INK)

    img.resize((32, 32), Image.LANCZOS).save(REPO / "assets/img/favicon.png")
    img.resize((180, 180), Image.LANCZOS).save(REPO / "assets/img/apple-touch-icon.png")
    img.resize((48, 48), Image.LANCZOS).save(
        REPO / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

    print(f"font size {font.size}; wrote favicon.png, apple-touch-icon.png, favicon.ico")
    print("Now bump favicon_version in _config.yml.")


if __name__ == "__main__":
    main()
