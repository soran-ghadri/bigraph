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
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))
import sphinx_rtd_theme
from datetime import datetime
from pygments.styles.friendly import FriendlyStyle


# -- Project information -----------------------------------------------------

project = 'Bigraph'
copyright = f"2019-{datetime.now().year}, Soran Ghadri"
author = 'Soran Ghadri'


FriendlyStyle.background_color = "#f3f2f1"

# The full version, including alpha/beta/rc tags
release = 'rc1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    'sphinx.ext.mathjax',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

napoleon_use_rtype = False

napoleon_include_init_with_doc = True
napoleon_google_docstring = True
napoleon_use_param = True
napoleon_use_ivar = True

pygments_style = "friendly"



# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'english'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
html_title = "Bigraph Documentation"
html_show_sourcelink = False
html_baseurl = "https://github.com/bi-graph/bigraph"
# html_show_copyright = False
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme_options = {
    'prev_next_buttons_location': 'both',
    'style_nav_header_background': '#F5A603',
    'navigation_depth': 4,
    "collapse_navigation": True,
    "sticky_navigation": False,
    "logo_only": True,
    "display_version": True,
    "style_external_links": True,
    "titles_only": True,
}

napoleon_use_param = False