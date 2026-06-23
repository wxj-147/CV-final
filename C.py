from PIL import Image

img = Image.open("C_clean.png").convert("RGBA")

# 1. 中心裁剪为正方形
w, h = img.size
side = min(w, h)
left = (w - side) // 2
top = (h - side) // 2
img = img.crop((left, top, left + side, top + side))

# 2. resize 到 1024（或 512）
img = img.resize((1024, 1024), Image.LANCZOS)

img.save("C_clean_1k.png")