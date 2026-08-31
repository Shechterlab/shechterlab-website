#!/usr/bin/env python3
"""Build the home-page hero background from the club logo.

Run from the repo root:  python3 assets/media/hero-skyline.build.py
Requires: pillow, numpy.

Everything is derived from the logo at run time rather than hardcoded, so
this still works if the logo is re-exported at a different resolution.
Two features are located automatically:

  * the wordmark, found via the orange "N" roundel, so it can be masked
    off — the hero wants the skyline alone;
  * the waterline, found as the widest row of ink, so the mirrored
    reflection below it can be dropped.
"""
from PIL import Image, ImageFilter
import numpy as np
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'logo', 'nyc-chromatin-club.png')
OUT = os.path.join(HERE, 'hero-skyline.jpg')

im = Image.open(SRC).convert('RGBA')
a = np.array(im).astype(np.int16)
R, G, B, A = a[:, :, 0], a[:, :, 1], a[:, :, 2], a[:, :, 3]

lum = a[:, :, :3].mean(axis=2)
ink = ((A > 10) & (lum < 235)).astype(np.float32)

# --- mask the wordmark -------------------------------------------------
orange = (A > 10) & (R > 200) & (G > 40) & (G < 170) & (B < 90)
oy, ox = np.nonzero(orange)
if len(ox):
    margin = max(2, int(im.width * 0.006))
    ink[: oy.max() + margin, max(0, ox.min() - margin):] = 0.0

# --- drop the mirrored reflection --------------------------------------
rows = ink.sum(axis=1)
waterline = int(np.max(np.nonzero(rows > rows.max() * 0.80)))
ink[waterline + 2:, :] = 0.0

ys, xs = np.nonzero(ink)
sil = Image.fromarray(
    (ink[ys.min():ys.max() + 1, xs.min():xs.max() + 1] * 255).astype(np.uint8), 'L')

# --- compose -----------------------------------------------------------
W, H = 2400, 1100
grad = np.zeros((H, W, 3), dtype=np.uint8)
for y in range(H):
    t = y / (H - 1)
    grad[y, :, :] = [int(c0 + (c1 - c0) * t) for c0, c1 in zip((0, 20, 56), (0, 56, 132))]
bg = Image.fromarray(grad, 'RGB')

# Warm glow low-left, so the brand orange lives in the art and not only on
# the buttons sitting over it.
yy, xx = np.mgrid[0:H, 0:W]
d = np.sqrt(((yy - H * 0.92) / (W * 0.42)) ** 2 + ((xx - W * 0.26) / (W * 0.42)) ** 2)
fall = np.clip(1.0 - d, 0, 1) ** 2
gp = np.zeros((H, W, 3), dtype=np.float32)
for i, c in enumerate((255, 102, 0)):
    gp[:, :, i] = fall * c * 0.30
bg = Image.fromarray(np.clip(np.array(bg).astype(np.float32) + gp, 0, 255).astype(np.uint8), 'RGB')

sh = int(sil.height * W / sil.width)
sk = sil.resize((W, sh), Image.LANCZOS)

# A dimmer, larger, offset copy behind the main skyline reads as haze.
mask2 = Image.new('L', (W, H), 0)
sk2 = sk.resize((int(W * 1.12), int(sh * 1.12)), Image.LANCZOS)
mask2.paste(sk2.point(lambda v: int(v * 0.11)), (-int(W * 0.09), H - int(sh * 1.12) - 30))
bg = Image.composite(Image.new('RGB', (W, H), (110, 160, 230)), bg,
                     mask2.filter(ImageFilter.GaussianBlur(2)))

mask = Image.new('L', (W, H), 0)
mask.paste(sk.point(lambda v: int(v * 0.28)), (0, H - sh))
bg = Image.composite(Image.new('RGB', (W, H), (150, 195, 255)), bg, mask)

bg.save(OUT, quality=88, optimize=True)
print('wrote', OUT, bg.size, '(waterline row', waterline, 'of', im.height, ')')
