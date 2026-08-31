from PIL import Image, ImageFilter
import numpy as np

SRC='/home/user/shechterlab-website/nycchromatinclub/assets/media/logo/nyc-chromatin-club.png'
im = Image.open(SRC).convert('RGBA')
a = np.array(im).astype(np.int16)

lum = a[:, :, :3].mean(axis=2)
ink = ((a[:, :, 3] > 10) & (lum < 235)).astype(np.float32)

# Remove the wordmark. Its roundels measure x 469-732, y 9-54; the tallest
# skyline spire in that neighbourhood is at x=400 reaching y=48, so masking
# from x=462 down to y=60 takes the type and leaves the spire intact.
ink[:60, 462:] = 0.0
# Drop the mirrored reflection: the hero wants a skyline, not a mirror.
ink[250:, :] = 0.0

ys, xs = np.nonzero(ink)
top, bot, left, right = ys.min(), ys.max(), xs.min(), xs.max()
sil = Image.fromarray((ink[top:bot + 1, left:right + 1] * 255).astype(np.uint8), 'L')

W, H = 2400, 1100
grad = np.zeros((H, W, 3), dtype=np.uint8)
for y in range(H):
    t = y / (H - 1)
    grad[y, :, :] = [int(c0 + (c1 - c0) * t) for c0, c1 in zip((0, 20, 56), (0, 56, 132))]
bg = Image.fromarray(grad, 'RGB')

# Warm glow low-left so the brand orange lives in the art, not only the buttons.
yy, xx = np.mgrid[0:H, 0:W]
d = np.sqrt(((yy - H * 0.92) / (W * 0.42)) ** 2 + ((xx - W * 0.26) / (W * 0.42)) ** 2)
fall = np.clip(1.0 - d, 0, 1) ** 2
gp = np.zeros((H, W, 3), dtype=np.float32)
for i, c in enumerate((255, 102, 0)):
    gp[:, :, i] = fall * c * 0.30
bg = Image.fromarray(np.clip(np.array(bg).astype(np.float32) + gp, 0, 255).astype(np.uint8), 'RGB')

sw = W
sh = int(sil.height * sw / sil.width)
sk = sil.resize((sw, sh), Image.LANCZOS)

# Dimmer, larger, offset copy behind reads as haze/depth.
mask2 = Image.new('L', (W, H), 0)
sk2 = sk.resize((int(sw * 1.12), int(sh * 1.12)), Image.LANCZOS)
mask2.paste(sk2.point(lambda v: int(v * 0.11)), (-int(sw * 0.09), H - int(sh * 1.12) - 30))
bg = Image.composite(Image.new('RGB', (W, H), (110, 160, 230)), bg, mask2.filter(ImageFilter.GaussianBlur(2)))

mask = Image.new('L', (W, H), 0)
mask.paste(sk.point(lambda v: int(v * 0.28)), (0, H - sh))
bg = Image.composite(Image.new('RGB', (W, H), (150, 195, 255)), bg, mask)

out = '/home/user/shechterlab-website/nycchromatinclub/assets/media/hero-skyline.jpg'
bg.save(out, quality=88, optimize=True)
print('wrote', out)
