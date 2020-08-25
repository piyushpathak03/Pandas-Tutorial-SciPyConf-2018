SRC  = $(wildcard notebooks/*.ipynb)

strip:
	nbstripout notebooks/*.ipynb

requirements.txt: environment.yml
	python convert_deps.py
