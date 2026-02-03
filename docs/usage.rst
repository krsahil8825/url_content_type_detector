Usage
=====

Basic usage
-----------

.. code-block:: python

   from url_content_type_detector import get_content_type

   content_type = get_content_type("https://example.com")
   print(content_type)

Custom timeout and secure mode
------------------------------

.. code-block:: python

   from url_content_type_detector import get_content_type, URLUtilsError

   try:
       content_type = get_content_type("https://example.com", timeout=15)
       print(content_type)
   except URLUtilsError as exc:
       print(f"Request failed: {exc}")

Convenience helpers
-------------------

.. code-block:: python

   from url_content_type_detector import utils

   if utils.is_pdf("https://example.com/sample.pdf"):
       print("PDF detected")

Notes
-----

- The library uses HTTP ``HEAD`` requests for efficiency.
- ``is_secure=True`` raises for 4xx/5xx responses.
- Use ``timeout=None`` only when you control network conditions.
