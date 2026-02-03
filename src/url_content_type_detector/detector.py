"""URL content type detection.

This module provides functionality to determine the content type of a URL
by making an HTTP ``HEAD`` request.
"""

import requests
import validators
from .exceptions import URLUtilsError


def get_content_type(url: str, timeout: int | None = 10, is_secure: bool = True) -> str:
    """Fetch the content type of the resource at the given URL.

    Args:
        url: The URL of the resource.
        timeout: Request timeout in seconds. Defaults to ``10``. Use ``None``
            for no timeout. Recommended range is 1-60 seconds; avoid using
            ``None`` in production.
        is_secure: When ``True``, raises an error for HTTP status codes that
            indicate failure.

    Returns:
        The content type reported by the server, or ``"Not Found"`` if the
        ``Content-Type`` header is missing.

    Raises:
        ValueError: If the URL is invalid or the timeout is negative.
        URLUtilsError: If the request times out, fails, or returns an HTTP
            error response when ``is_secure`` is ``True``.
    """

    try:
        timeout = None if timeout is None else int(timeout)
    except ValueError as e:
        raise ValueError("Timeout must be an integer or None.") from e

    if isinstance(timeout, int) and timeout < 0 and timeout is not None:
        raise ValueError("Timeout must be a non-negative integer or None.")

    url = url.strip().replace(" ", "%20")

    if not validators.url(url):
        raise ValueError("Invalid URL provided.")

    try:
        response = requests.head(url, allow_redirects=True, timeout=timeout)

        if is_secure:
            response.raise_for_status()

        content_type = response.headers.get("Content-Type", "Not Found")
        return content_type
    except requests.Timeout as e:
        raise URLUtilsError("The request timed out.") from e
    except requests.HTTPError as e:
        raise URLUtilsError(
            f"Accessing Unsecure URL\n\nHTTP error occurred: {e}"
        ) from e
    except requests.RequestException as e:
        raise URLUtilsError(f"Failed to fetch content type: {e}") from e
