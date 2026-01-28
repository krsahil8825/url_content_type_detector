"""
utils.py
~~~~~~~~

This module provides utility functions to check the content type of a URL.
"""

from .detector import get_content_type


def is_audio(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is audio."""
    if "audio" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_css(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is CSS."""
    if "css" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_csv(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is CSV."""
    if "csv" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_excel(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is an Excel file."""
    if "excel" in get_content_type(
        url=url, timeout=timeout, is_secure=is_secure
    ) or "spreadsheetml" in get_content_type(
        url=url, timeout=timeout, is_secure=is_secure
    ):
        return True
    return False


def is_gif(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is a GIF image."""
    if "gif" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_graphql(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is GraphQL."""
    if "graphql" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_gzip(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is GZIP."""
    if "gzip" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_html(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is HTML."""
    if "html" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_image(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is an image."""
    if "image" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_javascript(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is JavaScript."""
    if "javascript" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_json(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is JSON."""
    if "json" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_markdown(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is Markdown."""
    if "markdown" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_octet_stream(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is an octet-stream."""
    if "octet-stream" in get_content_type(
        url=url, timeout=timeout, is_secure=is_secure
    ):
        return True
    return False


def is_pdf(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is a PDF."""
    if "pdf" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_rar(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is a RAR file."""
    if "rar" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_text(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is plain text."""
    if "text/plain" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_video(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is a video."""
    if "video" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_xml(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is XML."""
    if "xml" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_zip(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is a ZIP file."""
    if "zip" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False
