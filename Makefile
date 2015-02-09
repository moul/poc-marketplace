all:	devserver

_build:
	fig build

html regenerate serve publish github:	_build
	fig run pelican make $@

help clean:
	$(MAKE) -C pelican $@

github:	publish
	@echo "FIXME: todo"
	# include pelican/Makefile
	# ghp-import -m "Generate Pelican site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	# git push origin $(GITHUB_PAGES_BRANCH)
	exit 1

devserver:	_build
	fig up pelican

.PHONY: help html clean regenerate serve devserver publish github
