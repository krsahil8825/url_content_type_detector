# pylint: disable=invalid-name
"""
Sphinx configuration for URL Content Type Detector documentation.
"""

from __future__ import annotations

import os
import sys
from importlib.metadata import PackageNotFoundError, version as pkg_version

# Add src/ to path so autodoc can import your package
sys.path.insert(0, os.path.abspath("../src"))

project = "URL Content Type Detector"
author = "Kumar Sahil"

# Version handling (from setuptools-scm / git tags)

try:
    release = pkg_version("url-content-type-detector")
except PackageNotFoundError:
    # Fallback when package is not installed (local build)
    release = "0.0.0"

version = release


# Extensions

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

autosummary_generate = True

napoleon_google_docstring = True
napoleon_numpy_docstring = False

autodoc_typehints = "description"
autodoc_member_order = "bysource"


# Intersphinx (FIXED)
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "requests": ("https://krsahil8825.github.io/url_content_type_detector/", None),
}


# Paths & patterns

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# HTML output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 3,
}
