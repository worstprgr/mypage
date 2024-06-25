.PHONY: all build update tar

all: build update tar

build:
	@echo "Building project ..."
	@echo "Building main css file (green)"
	npx tailwindcss -i src/static/css/tw_green.css -o src/static/css/green.css
	python recolor.py green amber
	python recolor.py green teal
	python recolor.py green slate
	@echo "Build Done!"

update:
	@echo "Updating entries ..."
	python generate.py

dev-css:
	@echo "Dev Mode ..."
	npx tailwindcss -i src/static/css/tw_green.css -o src/static/css/green.css --watch

dev-html:
	cd src && python live.py index

tar:
	@echo "Archiving project ..."
	tar --exclude-from=exclude.txt -czf adam.tar.gz src

