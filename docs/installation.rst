============
Installation
============

Install **URL Content Type Detector** using pip or uv. The package is available on PyPI and ready for production use.

Prerequisites
=============

* Python 3.10 or higher
* pip or uv package manager

Install via pip (Recommended)
==============================

The simplest way to install URL Content Type Detector:

.. code-block:: bash

   pip install url-content-type-detector

Install via uv (Fast & Modern)
==============================

For development or faster installations, use uv:

.. code-block:: bash

   uv pip install url-content-type-detector

Development Installation
=========================

If you want to contribute to the project or use the latest development version:

.. code-block:: bash

   git clone https://github.com/krsahil8825/url_content_type_detector.git
   cd url_content_type_detector
   uv pip install -e ".[dev]"

This installs the package in editable mode with all development dependencies included.

Verification
============

After installation, verify that everything is working correctly:

.. code-block:: bash

   python -c "from url_content_type_detector import get_content_type; print(get_content_type('https://example.com'))"
