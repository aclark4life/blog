# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "Blog"
copyright = " 2022 Jeffrey A. Clark, 'Alex'"
author = " Jeffrey A. Clark, 'Alex'"

# The short X.Y version
version = ""

# The full version, including alpha/beta/rc tags
release = ""


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "lib"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# RSS
extensions.append("sphinxcontrib.newsfeed")

# https://alabaster.readthedocs.io/en/latest/customization.html
html_theme_options = {
    "show_powered_by": False,
    "show_relbars": True,
    "logo_name": True,
    "font_family": "Helvetica",
    "donate_url": "https://www.patreon.com/headstraight",
    "extra_nav_links": {"Now": "/now/index.html", "RSS": "/index.rss",},
    "github_user": "aclark4life",
    "github_button": True,
}

html_sidebars = {
    "**": ["about.html", "searchbox.html", "donate.html", "navigation.html",]
}
html_show_sourcelink = False

html_permalinks = True
html_permalinks_icon = "←"


html_favicon = "images/aclark-jobs.jpg"

html_title = "Blog"
