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

# Add src/ to path so autodoc can import your package
sys.path.insert(0, os.path.abspath("../src"))

project = "URL Content Type Detector"
author = "Kumar Sahil"
description = "A lightweight, efficient utility to determine the content type of any URL with minimal overhead"

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

# HTML meta tags for SEO
html_baseurl = "https://krsahil8825.github.io/url_content_type_detector/"
html_title = "URL Content Type Detector - Detect Content Types from URLs"
html_favicon = "_static/icon.png"

# Meta tags for search engines
html_meta = {
    "viewport": "width=device-width, initial-scale=1.0",
    "description": "URL Content Type Detector - A lightweight, efficient Python utility to determine content types of URLs using HTTP HEAD requests",
    "keywords": "url, content-type, detector, http, python, library, url-parser, content-detection, mime-type",
    "author": "Kumar Sahil",
    "og:type": "website",
    "og:title": "URL Content Type Detector",
    "og:description": "Determine the content type of any URL with minimal overhead. Fast, efficient, and production-ready Python library",
    "og:url": "https://krsahil8825.github.io/url_content_type_detector/",
    "og:image": "https://krsahil8825.github.io/url_content_type_detector/_static/icon.png",
    "twitter:card": "summary",
    "twitter:title": "URL Content Type Detector",
    "twitter:description": "Lightweight Python utility for detecting URL content types with HTTP HEAD requests",
    "twitter:image": "https://krsahil8825.github.io/url_content_type_detector/_static/icon.png",
}


# Copy root files to build output
def copy_root_files(app, exc):
    """Copy root files (robots.txt, sitemap.xml) to build output."""
    if exc is None:

        src_dir = app.confdir
        build_dir = app.outdir

        # Copy robots.txt
        robots_src = os.path.join(src_dir, "robots.txt")
        robots_dst = os.path.join(build_dir, "robots.txt")
        if os.path.exists(robots_src):
            shutil.copy2(robots_src, robots_dst)

        # Copy sitemap.xml
        sitemap_src = os.path.join(src_dir, "sitemap.xml")
        sitemap_dst = os.path.join(build_dir, "sitemap.xml")
        if os.path.exists(sitemap_src):
            shutil.copy2(sitemap_src, sitemap_dst)


def setup(app):
    """Setup Sphinx app hooks."""
    app.connect("build-finished", copy_root_files)
