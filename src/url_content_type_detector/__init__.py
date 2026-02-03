"""URL Content Type Detector.

A lightweight utility to determine the content type of a URL using HTTP
``HEAD`` requests.

Basic usage:

>>> from url_content_type_detector import get_content_type
>>> url = "https://example.com/image.png"
>>> content_type = get_content_type(url)
>>> print(content_type)
image/png
"""

from importlib.metadata import version
from .detector import get_content_type
from .exceptions import URLUtilsError
from . import utils

__all__ = [
    "get_content_type",
    "utils",
    "URLUtilsError",
]


__version__ = version("url-content-type-detector")
