# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Raptoreum'
copyright = '2024, Raptoreum'
author = 'Raptoreum Team'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/Raptor3um/raptoreum",
            "icon": "fab fa-github-square",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/raptoreum",
            "icon": "fab fa-twitter-square",
        },
        {
            "name": "Discord",
            "url": "https://discor.gg/raptoreum,
            "icon": "fab fa-discord",
        },
        {
            "name": "YouTube",
            "url": "https://www.youtube.com/@RaptoreumOfficial",
            "icon": "fab fa-youtube-square",
        },
    ],
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
