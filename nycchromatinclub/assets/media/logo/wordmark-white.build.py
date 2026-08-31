from PIL import Image
import numpy as np

SRC='/home/user/shechterlab-website/nycchromatinclub/assets/media/logo/nyc-chromatin-club.png'
im = Image.open(SRC).convert('RGBA')

# The wordmark lockup only — the orange N roundel starts at x=469 and the
# type runs to the right edge, all within y 0-58. Cropping from 468 rather
# than 462 avoids catching a sliver of skyline. The skyline itself is
# excluded because the hero background already IS the skyline.
crop = im.crop((468, 0, 1000, 58))

# Upscale BEFORE deriving the mask: Lanczos interpolates smoothly, so the
# alpha ramp below lands on soft edges. Thresholding first and upscaling
# after just enlarges the staircase.
crop = crop.resize((crop.width * 3, crop.height * 3), Image.LANCZOS)
a = np.array(crop).astype(np.float32)

lum = a[:, :, :3].mean(axis=2)
# Soft ramp rather than a hard cut: fully opaque below 195, fading out by
# 240, which anti-aliases every edge instead of stair-stepping it.
alpha = np.clip((240.0 - lum) / 45.0, 0.0, 1.0) * (a[:, :, 3] / 255.0)

out = np.zeros(a.shape, dtype=np.uint8)
out[:, :, :3] = 255                      # white ink
out[:, :, 3] = (alpha * 255).astype(np.uint8)

img = Image.fromarray(out, 'RGBA')
img = img.crop(img.getbbox())
dest = '/home/user/shechterlab-website/nycchromatinclub/assets/media/logo/wordmark-white.png'
img.save(dest)
print('wrote', dest, img.size)
