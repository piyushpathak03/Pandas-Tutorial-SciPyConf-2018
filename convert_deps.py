"""
Convert the conda environment.yml to a pip requirements.txt
"""
import yaml

exclude = {'python=3.6.6', 'nomkl'}
rename = {'pytables': 'tables'}

with open("environment.yml") as f:
    dev = yaml.load(f)

required = dev['dependencies']
required = [rename.get(dep, dep).replace("=", "==") for dep in required
            if not isinstance(dep, dict)
            and dep not in exclude]
pip, = [x for x in dev['dependencies'] if isinstance(x, dict)]
required.extend(pip['pip'])


with open("requirements.txt", 'wt') as f:
    f.write('\n'.join(required))
