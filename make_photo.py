#!/usr/bin/env python3
"""Deterministic photo for post-x-promote-make-your-own-bounty-01.
Deep navy-to-teal gradient + the REAL make.fun ghost (press-kit mark-1024.png)
in the middle of the scene. No network, no wall clock, fixed seed.
Output: photo.png (1200x1200) next to this script.
"""
import hashlib
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W = H = 1200
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
GHOST = "ghost-mark-1024.png"

random.seed(42)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def bg_color(y):
    top = (13, 20, 54)
    mid = (10, 60, 88)
    bot = (8, 110, 120)
    t = y / H
    if t < 0.5:
        return lerp(top, mid, t / 0.5)
    return lerp(mid, bot, (t - 0.5) / 0.5)


img = Image.new("RGB", (W, H))
d = ImageDraw.Draw(img)

# --- background gradient ---
for y in range(H):
    d.line([(0, y), (W, y)], fill=bg_color(y))

# --- faint dots ---
for _ in range(130):
    x = random.randint(0, W - 1)
    y = random.randint(0, H - 1)
    r = random.choice([1, 1, 2, 2, 3])
    shade = lerp(bg_color(y), (255, 255, 255), 0.16)
    d.ellipse([x - r, y - r, x + r, y + r], fill=shade)

# --- ghost shadow + real ghost ---
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
shd = ImageDraw.Draw(shadow)
shd.ellipse([400, 890, 800, 935], fill=(0, 0, 0, 110))
shadow = shadow.filter(ImageFilter.GaussianBlur(8))
img = Image.alpha_composite(img.convert("RGBA"), shadow)
ghost = Image.open(GHOST).convert("RGBA").resize((540, 540), Image.LANCZOS)
img.paste(ghost, (330, 360), ghost)
d = ImageDraw.Draw(img)


def fit_font(text, size, max_w):
    while size > 20:
        f = ImageFont.truetype(FONT, size)
        if d.textlength(text, font=f) <= max_w:
            return f
        size -= 4
    return ImageFont.truetype(FONT, size)


def outlined_text(cx, y, text, font, fill, stroke_w=10):
    d.text((cx, y), text, font=font, fill=fill, anchor="ma",
           stroke_width=stroke_w, stroke_fill=(8, 10, 30))


# --- headline ---
f1 = fit_font("BIKIN BOUNTY", 130, 1120)
outlined_text(W // 2, 55, "BIKIN BOUNTY", f1, (255, 255, 255))
f2 = fit_font("SENDIRI", 130, 1120)
outlined_text(W // 2, 195, "SENDIRI", f2, (255, 214, 100))

# --- subline ---
f3 = fit_font("Hadiahnya kamu yang tentuin.", 58, 1120)
outlined_text(W // 2, 955, "Hadiahnya kamu yang tentuin.", f3, (255, 255, 255), 7)

# --- make.fun pill ---
d.rounded_rectangle([400, 1055, 800, 1135], radius=40, fill=(255, 255, 255),
                    outline=(8, 10, 30), width=5)
f4 = ImageFont.truetype(FONT, 58)
d.text((600, 1095), "make.fun", font=f4, fill=(230, 0, 126), anchor="mm")

img.convert("RGB").save("photo.png", "PNG")
data = open("photo.png", "rb").read()
print("saved photo.png", img.size, "sha256", hashlib.sha256(data).hexdigest()[:16])
