# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
from docutils import nodes
from sphinx.application import Sphinx
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx_design.shared import create_component

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'COLIBRE Documentation'
copyright = '2026, The COLIBRE Team'
author = 'Rob McGibbon & John Helly'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_design",
    "sphinxcontrib.mermaid",
    # Render equations more quickly, which is needed for our large property tables
    "sphinxcontrib.katex",
]

templates_path = ['_templates']
exclude_patterns = []

html_sidebars = {
    "**": [
        "globaltoc.html",  # Site contents
        "localtoc.html",   # Page contents
    ]
}

html_favicon = '_static/favicon.ico'


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
def _highlight_role(background, extra_style=""):
    """Return a docutils role function that wraps text in a highlighted <span>."""

    def role(name, rawtext, text, lineno, inliner, options=None, content=None):
        style = (
            f"background-color: {background};"
            " color: black;"
            " padding: 1px 4px;"
            " border-radius: 3px;"
            " font-family: monospace;"
            f"{extra_style}"
        )
        html = f'<span style="{style}">{text}</span>'
        # raw() node so the HTML passes through unchanged; latex() node is a
        # plain-text fallback for PDF builds.
        node = nodes.raw("", html, format="html")
        latex_node = nodes.raw("", text, format="latex")
        return [node, latex_node], []

    return role


class MinorIssueDropdowns(SphinxPostTransform):
    """Render sections of the known issues page with italic titles as dropdowns.

    Keeping them as sections until this point means they still appear in the
    page contents, and can be linked to with a plain :ref:.
    """

    # Must run before the sphinx_design transform which renders the dropdowns
    default_priority = 198
    formats = ("html",)

    def run(self):
        if self.env.docname != "issues/index":
            return
        for section in list(self.document.findall(nodes.section)):
            title = section[0]
            if len(title) != 1 or not isinstance(title[0], nodes.emphasis):
                continue
            dropdown = create_component(
                "dropdown",
                opened=False,
                type="dropdown",
                has_title=True,
                icon=None,
                chevron=None,
                container_classes=["sd-mb-3"],
                title_classes=[],
                body_classes=[],
            )
            dropdown += nodes.rubric("", "", *title[0].children, ids=section["ids"])
            dropdown.extend(section.children[1:])
            section.replace_self(dropdown)


def setup(app: Sphinx):
    app.add_post_transform(MinorIssueDropdowns)
    app.add_role("avail", _highlight_role("#c8e6c9"))     # light green
    app.add_role("snaponly", _highlight_role("#bbdefb"))  # light blue
    # Add a strikethrough for colourblind folks to distinguish red/green
    app.add_role("unavail", _highlight_role("#ffcdd2", " text-decoration: line-through;"))  # light red

