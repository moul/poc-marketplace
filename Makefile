all:	devserver

_build:
	fig build

html regenerate serve publish:	_build
	fig run pelican make $@

help clean:
	$(MAKE) -C pelican $@

github:	publish
	ghp-import -m "Generate Pelican site" pelican/output
	git push origin gh-pages

devserver:	_build
	fig up pelican

shell:	_build
	fig run pelican /bin/bash

.PHONY: help html clean regenerate serve devserver publish github
