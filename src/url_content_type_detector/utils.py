"""Convenience helpers for content-type checks.

Each helper calls :func:`url_content_type_detector.get_content_type` and
performs a simple substring check on the returned ``Content-Type`` value.
"""

from .detector import get_content_type


def is_7z(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates a 7z archive.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates a 7z archive; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "7z" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_audio(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates audio.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates audio; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "audio" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_avif(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates an AVIF image.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates AVIF; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "avif" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_css(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates CSS.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates CSS; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "css" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_csv(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates CSV.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates CSV; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "csv" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_excel(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates an Excel file.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates Excel; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "excel" in get_content_type(
        url=url, timeout=timeout, is_secure=is_secure
    ) or "spreadsheetml" in get_content_type(
        url=url, timeout=timeout, is_secure=is_secure
    ):
        return True
    return False


def is_gif(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates a GIF image.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates GIF; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "gif" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_graphql(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates GraphQL.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates GraphQL; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "graphql" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_gzip(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates gzip.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates gzip; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "gzip" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_html(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates HTML.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates HTML; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "html" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_image(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates an image.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates an image; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "image" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_javascript(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates JavaScript.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates JavaScript; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "javascript" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_jpeg(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates a JPEG image.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates JPEG; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "jpeg" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_json(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates JSON.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates JSON; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "json" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_markdown(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates Markdown.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates Markdown; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """

    if "markdown" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False

def is_mp3(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates an MP3 audio file.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates MP3; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "mpeg" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_mp4(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates an MP4 video file.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates MP4; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "mp4" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_octet_stream(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates ``application/octet-stream``.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates octet-stream; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "octet-stream" in get_content_type(
        url=url, timeout=timeout, is_secure=is_secure
    ):
        return True
    return False


def is_opendocument(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates an OpenDocument file.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates OpenDocument; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "opendocument" in get_content_type(
        url=url, timeout=timeout, is_secure=is_secure
    ):
        return True
    return False


def is_pdf(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates a PDF.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates PDF; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "pdf" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_png(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates a PNG image.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates PNG; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "png" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_powerpoint(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates a PowerPoint file.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates PowerPoint; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "powerpoint" in get_content_type(
        url=url, timeout=timeout, is_secure=is_secure
    ) or "presentationml" in get_content_type(
        url=url, timeout=timeout, is_secure=is_secure
    ):
        return True
    return False


def is_rar(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates a RAR archive.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates RAR; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "rar" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_svg(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates an SVG image.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates SVG; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "svg" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_text(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates plain text.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates plain text; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "text/plain" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_video(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates video.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates video; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "video" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_webp(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates a WebP image.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates WebP; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "webp" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_word(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates a Word document.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates Word; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "word" in get_content_type(
        url=url, timeout=timeout, is_secure=is_secure
    ) or "msword" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_x_bz2(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates a bzip2 archive.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates bzip2; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "x-bzip2" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_xml(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates XML.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates XML; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "xml" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_x_tar(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates a tar archive.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates tar; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "x-tar" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_xz(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates an xz archive.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates xz; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "xz" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_zip(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates a ZIP archive.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates ZIP; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "zip" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False


def is_zstd(url: str, timeout: int | None = 10, is_secure: bool = True) -> bool:
    """Check whether the URL content type indicates a zstd archive.

    Args:
        url: The URL to inspect.
        timeout: Request timeout in seconds. Use ``None`` for no timeout.
        is_secure: When ``True``, raise for HTTP error responses.

    Returns:
        ``True`` if the content type indicates zstd; otherwise ``False``.

    Raises:
        ValueError: If the URL is invalid or timeout is negative.
        URLUtilsError: If the request fails or times out.
    """
    if "zstd" in get_content_type(url=url, timeout=timeout, is_secure=is_secure):
        return True
    return False
