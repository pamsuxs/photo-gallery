from pathlib import Path
import json

root = Path(__file__).resolve().parent
photos = root / 'photos'
exts = {'.jpg','.jpeg','.png','.webp','.gif','.avif'}
files = sorted(p for p in photos.iterdir() if p.suffix.lower() in exts)
items = [{"src": f"photos/{p.name}", "alt": p.stem.replace('_',' ').replace('-',' ')} for p in files]
(root/'gallery.json').write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'Updated gallery.json with {len(items)} photos.')
