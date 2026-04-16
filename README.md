# Documentation for the FLAMINGO simulations

This repository contains incomplete sphinx documentation for FLAMINGO.

## Building

To build the html documentation:
```
pip install sphinx piccolo_theme sphinx_design sphinxcontrib_mermaid
make html
```

## Testing

The built in python http server can be used to view the built pages. In the top level source directory:
```
cd build
ln -s html flamingo
python -m http.server 8020
```
Then point your web browser at http://localhost:8020/flamingo/ . The
symlink is there to make python serve the pages with the same prefix
as they have on the real server (necessary due to some slightly hacky
theme customization).

In this configuration links to the file browser will not work because
the API server is not present but the documentation should all
appear.
