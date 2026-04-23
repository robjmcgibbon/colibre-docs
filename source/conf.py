# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
from docutils import nodes
from sphinx.application import Sphinx

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'COLIBRE Documentation'
copyright = '2026, The COLIBRE Team'
author = 'John Helly & Rob McGibbon'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_design", "sphinxcontrib.mermaid"]

templates_path = ['_templates']
exclude_patterns = []

html_sidebars = {
    "**": [
        "globaltoc.html",  # Site contents
        "localtoc.html",   # Page contents
    ]
}



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']
html_title = 'COLIBRE Documentation'

# Keep the short title as plain text. The logo is injected by the custom
# layout template so Sphinx can generate the correct relative path on every
# page, including nested sections.
html_short_title = 'COLIBRE Data Products'

# Select the piccolo theme
html_theme = 'piccolo_theme'

# Customization
html_css_files = [
    'custom.css',
]
html_js_files = []


# Coloured inline roles for the SOAP property table.
def _highlight_role(background):
    """Return a docutils role function that wraps text in a highlighted <span>."""

    def role(name, rawtext, text, lineno, inliner, options=None, content=None):
        style = (
            f"background-color: {background};"
            " color: black;"
            " padding: 1px 4px;"
            " border-radius: 3px;"
            " font-family: monospace;"
        )
        html = f'<span style="{style}">{text}</span>'
        # raw() node so the HTML passes through unchanged; latex() node is a
        # plain-text fallback for PDF builds.
        node = nodes.raw("", html, format="html")
        latex_node = nodes.raw("", text, format="latex")
        return [node, latex_node], []

    return role


def setup(app: Sphinx):
    app.add_role("avail", _highlight_role("#c8e6c9"))     # light green
    app.add_role("snaponly", _highlight_role("#bbdefb"))  # light blue
    app.add_role("unavail", _highlight_role("#ffcdd2"))   # light red

