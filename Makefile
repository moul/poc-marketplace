all:	devserver

_build:
	fig build

help html clean regenerate serve publish github:	_build
	fig run pelican make $@

devserver:	_build
	fig up pelican

.PHONY: help html clean regenerate serve devserver publish github
