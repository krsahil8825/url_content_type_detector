"""
utils.py
~~~~~~~~

This module provides utility functions to check the content type of a URL.
"""

from .detector import get_content_type


def is_7z(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is a 7z file."""
    if "7z" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_audio(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is audio."""
    if "audio" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_avif(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is an AVIF image."""
    if "avif" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
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


def is_jpeg(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is a JPEG image."""
    if "jpeg" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
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

def is_mp3(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is an MP3 audio file."""
    if "mpeg" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_mp4(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is an MP4 video file."""
    if "mp4" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_octet_stream(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is an octet-stream."""
    if "octet-stream" in get_content_type(
        url=url, timeout=timeout, is_secure=is_secure
    ):
        return True
    return False


def is_opendocument(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is an OpenDocument file."""
    if "opendocument" in get_content_type(
        url=url, timeout=timeout, is_secure=is_secure
    ):
        return True
    return False


def is_pdf(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is a PDF."""
    if "pdf" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_png(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is a PNG image."""
    if "png" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_powerpoint(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is a PowerPoint file."""
    if "powerpoint" in get_content_type(
        url=url, timeout=timeout, is_secure=is_secure
    ) or "presentationml" in get_content_type(
        url=url, timeout=timeout, is_secure=is_secure
    ):
        return True
    return False


def is_rar(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is a RAR file."""
    if "rar" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_svg(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is an SVG image."""
    if "svg" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
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


def is_webp(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is a WebP image."""
    if "webp" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_word(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is a Word document."""
    if "word" in get_content_type(
        url=url, timeout=timeout, is_secure=is_secure
    ) or "msword" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_x_bz2(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is a bzip2 file."""
    if "x-bzip2" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_xml(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is XML."""
    if "xml" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_x_tar(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is a tar archive."""
    if "x-tar" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_xz(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is an xz compressed file."""
    if "xz" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_zip(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is a ZIP file."""
    if "zip" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_zstd(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check if the content type of the URL is a zstd compressed file."""
    if "zstd" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False
