URL Content Type Detector
===========================

A lightweight utility to determine the content type of a URL using efficient
HTTP ``HEAD`` requests.

Quick Start
-----------

.. code-block:: python

   from url_content_type_detector import get_content_type

   content_type = get_content_type("https://example.com/image.png")
   print(content_type)

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Documentation

   installation
   usage
   api
   contributing
