"""Publie une version : lit le repère de chaque .bin du dossier et écrit manifest.json.
Usage : python publier.py "notes de version (facultatif)"  — puis déposer les fichiers sur GitHub."""
import json, re, sys, pathlib
d = pathlib.Path(__file__).parent; notes = sys.argv[1] if len(sys.argv) > 1 else ''
man = {}
for f in sorted(d.glob('*.bin')):
    m = re.search(rb'TUSI-FW:(v[0-9]+)\|([^|]*)\|([^|]*)\|', f.read_bytes())
    if not m: print('ignoré (pas un firmware Tusi) :', f.name); continue
    hw, ver, build = (x.decode() for x in m.groups())
    man[hw] = {'version': ver, 'build': build, 'url': f.name, 'notes': notes}
    print(f'{hw} : {ver} du {build} -> {f.name}')
(d / 'manifest.json').write_text(json.dumps(man, ensure_ascii=False, indent=2), encoding='utf-8')
print('manifest.json écrit')
