=====
Usage
=====

The URL Content Type Detector library makes it easy to detect and identify MIME types from any URL. Below are comprehensive examples covering basic usage, error handling, and advanced features.

Basic Usage - Get Content Type
===============================

The simplest way to detect a URL's content type:

.. code-block:: python

   from url_content_type_detector import get_content_type

   # Detect content type from any URL
   content_type = get_content_type("https://example.com")
   print(content_type)  # Output: text/html

Advanced Usage - Custom Timeout
=================================

Control request timeout and error handling:

.. code-block:: python

   from url_content_type_detector import get_content_type, URLUtilsError

   try:
       # Set custom timeout (in seconds)
       content_type = get_content_type("https://example.com", timeout=15)
       print(f"Content Type: {content_type}")
   except URLUtilsError as exc:
       print(f"Request failed: {exc}")

Secure Mode - Strict HTTP Status Validation
=============================================

Enable strict mode to raise exceptions for 4xx/5xx responses:

.. code-block:: python

   from url_content_type_detector import get_content_type, URLUtilsError

   try:
       # is_secure=True raises exceptions for 4xx/5xx status codes
       content_type = get_content_type("https://example.com", is_secure=True)
       print(f"Content Type: {content_type}")
   except URLUtilsError as exc:
       print(f"Error: {exc}")

Convenience Helpers - Detect Specific Content Types
====================================================

Use built-in utility functions to detect specific MIME types:

.. code-block:: python

   from url_content_type_detector import utils

   # Check if URL points to a PDF
   if utils.is_pdf("https://example.com/document.pdf"):
       print("PDF file detected!")

   # Check for other common types
   if utils.is_image("https://example.com/photo.jpg"):
       print("Image file detected!")

   if utils.is_video("https://example.com/video.mp4"):
       print("Video file detected!")

Complete Example with Error Handling
======================================

A production-ready example with comprehensive error handling:

.. code-block:: python

   from url_content_type_detector import get_content_type, URLUtilsError

   def detect_url_type(url, timeout=10):
       """Detect content type of a URL with error handling."""
       try:
           content_type = get_content_type(url, timeout=timeout, is_secure=True)
           return content_type
       except URLUtilsError as e:
           print(f"Failed to detect content type: {e}")
           return None

   # Usage
   url = "https://example.com/image.png"
   content_type = detect_url_type(url)
   if content_type:
       print(f"Detected: {content_type}")

Important Notes
================

- **Efficiency**: The library uses HTTP ``HEAD`` requests instead of full ``GET`` requests, minimizing bandwidth usage
- **Secure Mode**: When ``is_secure=True``, the function raises exceptions for 4xx and 5xx HTTP status codes
- **Timeout**: Use ``timeout=None`` only when you have full control over network conditions; otherwise, always specify a timeout
- **URL Validation**: The library validates URLs before making requests using industry-standard validators
- **Error Handling**: Always catch ``URLUtilsError`` and ``InvalidURLError`` in production code
