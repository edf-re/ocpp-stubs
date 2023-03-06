SHELL=bash -o pipefail # Just in case

release:
	python -m pip install --upgrade pip twine setuptools build
	rm -rf dist
	python -m build
	twine upload dist/*
