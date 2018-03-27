from os import path

here = path.abspath(path.dirname(__file__))

version_file = path.join(here, 'version.txt')
with open(version_file, 'r') as f:
    version = f.read()
    version_parts = list(map(int, version.split('.')))
    version_parts[-1] += 1
    version = '.'.join(map(str, version_parts))

with open(version_file, 'w') as f:
    f.write(version)
