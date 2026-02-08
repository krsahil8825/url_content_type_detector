# pylint: disable=invalid-name
# pylint: disable=line-too-long
"""
Sphinx configuration for URL Content Type Detector documentation.
"""

from __future__ import annotations

import os
import sys
import shutil

from importlib.metadata import PackageNotFoundError, version as pkg_version

# Path setup
# Add src/ to path so autodoc can import your package
sys.path.insert(0, os.path.abspath("../src"))

# Project information
project = "URL Content Type Detector"
author = "Kumar Sahil"
description = (
    "A lightweight, efficient utility to determine the content type of any URL "
    "with minimal overhead"
)

# Version handling (from installed package / git tags)
try:
    release = pkg_version("url-content-type-detector")
except PackageNotFoundError:
    release = "0.0.0"

version = release

# Extensions
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx_sitemap",  # ✅ automatic sitemap generation
]

autosummary_generate = True

napoleon_google_docstring = True
napoleon_numpy_docstring = False

autodoc_typehints = "description"
autodoc_member_order = "bysource"

# Intersphinx
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
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

# Base URL (IMPORTANT)
# Use GitHub Pages URL as canonical so site survives custom-domain expiry
html_baseurl = "https://krsahil8825.github.io/url_content_type_detector/"

# Sitemap configuration
sitemap_filename = "sitemap.xml"
sitemap_url_scheme = "{link}"

# HTML metadata (SEO + Social)
html_title = "URL Content Type Detector - Detect Content Types from URLs"
html_favicon = "_static/icon.png"

html_meta = {
    "viewport": "width=device-width, initial-scale=1.0",
    "description": (
        "URL Content Type Detector - A lightweight, efficient Python utility "
        "to determine content types of URLs using HTTP HEAD requests"
    ),
    "keywords": (
        "url, content-type, detector, http, python, library, "
        "url-parser, content-detection, mime-type"
    ),
    "author": "Kumar Sahil",
    "og:type": "website",
    "og:title": "URL Content Type Detector",
    "og:description": (
        "Determine the content type of any URL with minimal overhead. "
        "Fast, efficient, and production-ready Python library"
    ),
    "og:url": "https://krsahil8825.github.io/url_content_type_detector/",
    "og:image": (
        "https://krsahil8825.github.io/url_content_type_detector/_static/icon.png"
    ),
    "twitter:card": "summary",
    "twitter:title": "URL Content Type Detector",
    "twitter:description": (
        "Lightweight Python utility for detecting URL content types "
        "with HTTP HEAD requests"
    ),
    "twitter:image": (
        "https://krsahil8825.github.io/url_content_type_detector/_static/icon.png"
    ),
}


# Copy root files (robots.txt)
def copy_root_files(app, exc):
    """Copy root-level files (robots.txt) into build output."""
    if exc is None:
        src_dir = app.confdir
        build_dir = app.outdir

        robots_src = os.path.join(src_dir, "robots.txt")
        robots_dst = os.path.join(build_dir, "robots.txt")

        if os.path.exists(robots_src):
            shutil.copy2(robots_src, robots_dst)


def setup(app):
    """Register Sphinx hooks."""
    app.connect("build-finished", copy_root_files)
