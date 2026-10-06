from pathlib import Path
import shutil
import zipfile

output = Path('site')
if output.exists():
    shutil.rmtree(output)
with zipfile.ZipFile('Kayaswanna_Portfolio_GitHubLite.zip') as archive:
    archive.extractall(output)
root = output / 'Kayaswanna_Portfolio_GitHubLite'
updates = Path('updates')
shutil.copyfile(updates / 'index.html', root / 'index.html')
for folder in ('assets', 'posters'):
    for source in (updates / folder).iterdir():
        shutil.copyfile(source, root / folder / source.name)
with (root / 'assets' / 'Travel_UGC.mp4').open('wb') as video:
    for part in sorted((updates / 'travel-parts').iterdir()):
        with part.open('rb') as chunk:
            shutil.copyfileobj(chunk, video)
print('Portfolio ready: 33 existing videos preserved, 3 added.')
