"""Copy all source mission assets into public/ during GitHub Actions build."""
from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
ROOT=Path(__file__).resolve().parents[1]
URL='https://codeload.github.com/seki999/AWS_Cloud_Ops_Adventure_Android/zip/refs/heads/main'
with urlopen(URL,timeout=120) as r: data=r.read()
with ZipFile(BytesIO(data)) as z:
    names=[n for n in z.namelist() if '/app/src/main/assets/' in n and not n.endswith('/')]
    assert any(n.endswith('/catalog.json') for n in names),'Missing catalog'
    assert len([n for n in names if '/missions/aws-' in n])==60,'Expected 60 missions'
    for n in names:
        rel=n.split('/app/src/main/assets/',1)[1]
        out=ROOT/'public'/rel
        out.parent.mkdir(parents=True,exist_ok=True)
        out.write_bytes(z.read(n))
print('Copied',len(names),'assets')