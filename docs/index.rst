=====================================
URL Content Type Detector
=====================================

**A lightweight, efficient utility to determine the content type of any URL with minimal overhead**

URL Content Type Detector is a powerful Python library that detects and retrieves the MIME type of any URL using efficient HTTP HEAD requests. It's designed for production use with comprehensive error handling, URL validation, and robust security features.

**Key Highlights:**

* 🚀 Fast & Efficient - Uses HTTP HEAD requests to minimize bandwidth
* ✅ Robust Error Handling - Custom exceptions and detailed error messages
* 🔒 URL Validation - Built-in URL validation using industry standards
* ⏱️ Configurable Timeout - Adjustable timeout with sensible defaults
* 🛡️ Security-First - Optional strict HTTP status code validation
* 📦 Lightweight - Zero unnecessary dependencies beyond requests and validators
* 🧪 Well-Tested - Comprehensive test suite with pytest
* 🐍 Python 3.10+ - Modern Python support

Quick Start Example
===================

Get the content type of any URL with just a few lines:

.. code-block:: python

   from url_content_type_detector import get_content_type

   # Detect content type from URL
   content_type = get_content_type("https://example.com/image.png")
   print(content_type)  # Output: image/png

   # Detect content type from any URL with error handling
   try:
       content_type = get_content_type("https://github.com/krsahil8825/url_content_type_detector")
       print(f"Content Type: {content_type}")
   except Exception as e:
       print(f"Error: {e}")

Contents & Documentation
==========================

.. toctree::
   :maxdepth: 2
   :caption: Documentation

   installation
   usage
   api
   contributing
