# Adam
This is my personal site. It's a static page with some generator scripts.  

## Generators
### `recolor.py`
*Recolor* takes an tailwind css file and converts it to a new file, with a new color theme.

### `generate.py`
*Generate* updates/inserts the text sections on my site, so I don't have to work with the whole
html file, if I want to change the text contents.  

If I want to make changes to the structure of the site, I have to edit the `src/template.html`, since 
the script takes the template and renders it as `index.html`.  

## Developing
I'm using [LivePy](https://github.com/worstprgr/livepy) for auto-refreshing my browser, if a file changed.  

```text
make            -> builds the projects and archives it as tarball
make update     -> creates/updates the text content from "/entries/" to the index.html
make dev-css    -> starts the tailwind build server
make dev-html   -> starts LivePy
```

## Dependencies
- Tailwind CSS


