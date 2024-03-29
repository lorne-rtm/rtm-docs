# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Raptoreum'
copyright = '2024, Raptoreum'
author = 'Raptoreum Team'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    #"sphinx.ext.rediraffe",
    "sphinx_design",
    "sphinx_copybutton",
    #"autoapi.extension",
    # custom extensions
    #"_extension.gallery_directive",
    #"_extension.component_directive",
    # For extension examples and demos
    "myst_parser",
    #"ablog",
    #"jupyter_sphinx",
    #"sphinxcontrib.youtube",
    #"nbsphinx",
    #"numpydoc",
    "sphinx_togglebutton",
    #"jupyterlite_sphinx",
    "sphinx_favicon",
    "hoverxref.extension",
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
            "url": "https://discor.gg/raptoreum",
            "icon": "fab fa-discord",
        },
        {
            "name": "YouTube",
            "url": "https://www.youtube.com/@RaptoreumOfficial",
            "icon": "fab fa-youtube-square",
        },
    ],
    "logo": {
        "image_light": "_static/logo_dark.svg",  # Logo for light mode
        "image_dark": "_static/logo_light.svg",  # Logo for dark mode
    },
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Silence warnings from unknown files on epub build
suppress_warnings = ['epub.unknown_project_files']

html_sidebars = {
    "index": ["sidebar-main.html"],
    "**": ["sidebar-nav-bs"]
}

html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]