"""usage: python3 contact_sheet.py frames_dir out.jpg [scale=0.5]  (4 columns)"""
import sys, glob
from PIL import Image
fs = sorted(glob.glob(sys.argv[1] + '/*.jpg') + glob.glob(sys.argv[1] + '/*.png'))
ims = [Image.open(f).convert('RGB') for f in fs]
s = float(sys.argv[3]) if len(sys.argv) > 3 else 0.5
w, h = int(ims[0].width * s), int(ims[0].height * s); cols = 4; rows = (len(ims) + cols - 1) // cols
out = Image.new('RGB', (w * cols, h * rows))
for i, im in enumerate(ims): out.paste(im.resize((w, h)), ((i % cols) * w, (i // cols) * h))
out.save(sys.argv[2], quality=85); print(len(ims), 'frames')
