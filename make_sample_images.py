from PIL import Image, ImageDraw, ImageFilter
import math, random
from pathlib import Path

out = Path('/mnt/data/photo_gallery_demo/photos')
out.mkdir(parents=True, exist_ok=True)
W, H = 1600, 1100
random.seed(42)

palettes = [
    ((232,222,207),(109,137,129),(53,68,69),(240,188,140)),
    ((218,231,236),(113,143,166),(48,72,91),(236,183,128)),
    ((236,224,226),(169,131,138),(92,79,88),(225,193,157)),
    ((228,234,218),(130,151,111),(62,81,57),(226,176,116)),
    ((224,219,235),(121,109,151),(62,53,79),(229,187,145)),
]

for idx, (sky, mid, dark, sun) in enumerate(palettes, start=1):
    img = Image.new('RGB',(W,H),sky)
    px = img.load()
    # soft vertical gradient
    for y in range(H):
        t=y/(H-1)
        target = tuple(int(sky[c]*(1-t*0.55)+mid[c]*(t*0.55)) for c in range(3))
        for x in range(W):
            px[x,y]=target
    d=ImageDraw.Draw(img,'RGBA')
    # sun/moon
    sx = int(W*(0.72 if idx%2 else 0.28)); sy=int(H*0.28)
    d.ellipse((sx-85,sy-85,sx+85,sy+85), fill=sun+(210,))
    # distant hills
    pts=[]
    base=int(H*0.63)
    for x in range(0,W+60,60):
        y=base + int(55*math.sin(x/210+idx)) + random.randint(-22,22)
        pts.append((x,y))
    pts += [(W,H),(0,H)]
    d.polygon(pts, fill=mid+(160,))
    # foreground hills
    pts2=[]
    base2=int(H*0.74)
    for x in range(0,W+50,50):
        y=base2 + int(80*math.sin(x/150+idx*0.7)) + random.randint(-28,28)
        pts2.append((x,y))
    pts2 += [(W,H),(0,H)]
    d.polygon(pts2, fill=dark+(225,))
    # subtle foreground motif per image
    if idx==1:
        for x in [180,245,305]:
            d.line((x,H*0.58,x-30,H*0.92), fill=(32,44,42,180), width=13)
            d.ellipse((x-55,H*0.57-18,x+15,H*0.57+38), fill=(42,67,59,180))
    elif idx==2:
        # minimalist shore reflection
        d.rectangle((0,int(H*0.82),W,H), fill=(59,86,104,100))
        for k in range(11):
            yy=int(H*0.84)+k*18
            d.line((W*0.12,yy,W*0.48,yy), fill=(245,230,198,35), width=4)
    elif idx==3:
        # architectural arches
        for x in [180,520,860,1200]:
            d.rounded_rectangle((x,int(H*0.56),x+210,int(H*0.96)),radius=95,fill=(56,48,55,85))
            d.rounded_rectangle((x+38,int(H*0.61),x+172,int(H*0.96)),radius=65,fill=sky+(160,))
    elif idx==4:
        # reeds
        for x in range(80,W,90):
            top=random.randint(int(H*0.55),int(H*0.73))
            d.line((x,H,x+random.randint(-25,25),top), fill=(48,68,44,180), width=5)
            d.ellipse((x-16,top-12,x+18,top+10), fill=(105,124,79,160))
    else:
        # abstract city lights
        for x in range(90,W,120):
            ht=random.randint(100,320)
            d.rounded_rectangle((x,H-ht-40,x+60,H),radius=12,fill=(44,37,58,115))
            for yy in range(H-ht, H-60, 42):
                d.rectangle((x+17,yy,x+29,yy+14),fill=(240,206,153,120))
    img = img.filter(ImageFilter.GaussianBlur(radius=0.35))
    img.save(out/f'{idx:02d}.jpg', quality=92, optimize=True)
