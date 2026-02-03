=============
API Reference
=============

Complete API documentation for the URL Content Type Detector library. This reference includes all functions, classes, and utilities available in the package.

Main Functions & Classes
=========================

Core API - Content Type Detection
==================================

.. autofunction:: url_content_type_detector.get_content_type

Exception Classes
=================

.. autoclass:: url_content_type_detector.URLUtilsError
   :members:

Utility Functions
=================

The utils module provides convenient helper functions for detecting specific content types:

.. automodule:: url_content_type_detector.utils
   :members:
   :member-order: bysource

Examples
========

**Detect a URL's content type:**

.. code-block:: python

   from url_content_type_detector import get_content_type

   content_type = get_content_type("https://example.com")

**Check for specific content types:**

.. code-block:: python

   from url_content_type_detector import utils

   is_pdf = utils.is_pdf("https://example.com/document.pdf")
   is_image = utils.is_image("https://example.com/photo.jpg")
   is_video = utils.is_video("https://example.com/video.mp4")
