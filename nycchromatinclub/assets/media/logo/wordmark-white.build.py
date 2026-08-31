#!/usr/bin/env python3
"""Build the white knockout wordmark used on the dark hero.

Run from the repo root:  python3 assets/media/logo/wordmark-white.build.py
Requires: pillow, numpy.

The wordmark lockup only — the skyline is excluded because the hero
background already is one. Its bounds are found from the orange "N"
roundel rather than hardcoded, so a re-exported logo still works.

The letters inside the N/Y/C roundels are white in the source, so they are
not "ink" and stay transparent: the navy behind shows through them, which
is what keeps the roundels reading as roundels instead of solid blobs.
"""
from PIL import Image
import numpy as np
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'nyc-chromatin-club.png')
OUT = os.path.join(HERE, 'wordmark-white.png')

im = Image.open(SRC).convert('RGBA')
a = np.array(im).astype(np.int16)
R, G, B, A = a[:, :, 0], a[:, :, 1], a[:, :, 2], a[:, :, 3]

orange = (A > 10) & (R > 200) & (G > 40) & (G < 170) & (B < 90)
oy, ox = np.nonzero(orange)
pad = max(1, int(im.width * 0.002))
left = max(0, ox.min() - pad)
bottom = min(im.height, oy.max() + pad)
crop = im.crop((left, 0, im.width, bottom))

# Upscale BEFORE deriving the mask when the source is small: Lanczos
# interpolates smoothly so the alpha ramp lands on soft edges. Thresholding
# first and enlarging after just magnifies the staircase.
if crop.width < 1200:
    f = int(np.ceil(1200 / crop.width))
    crop = crop.resize((crop.width * f, crop.height * f), Image.LANCZOS)

c = np.array(crop).astype(np.float32)
lum = c[:, :, :3].mean(axis=2)
# Soft ramp rather than a hard cut: opaque below 195, fading out by 240.
alpha = np.clip((240.0 - lum) / 45.0, 0.0, 1.0) * (c[:, :, 3] / 255.0)

out = np.zeros(c.shape, dtype=np.uint8)
out[:, :, :3] = 255
out[:, :, 3] = (alpha * 255).astype(np.uint8)

img = Image.fromarray(out, 'RGBA')
img = img.crop(img.getbbox())
if img.width > 1800:
    img = img.resize((1800, round(img.height * 1800 / img.width)), Image.LANCZOS)
img.save(OUT)
print('wrote', OUT, img.size)
