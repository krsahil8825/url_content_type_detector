import requests
from .validators import is_valid_url
from .exceptions import URLUtilsError


def get_content_type(url: str, timeout: int | None = 10, is_secure: bool = True) -> str:
    """Fetch the content type of the resource at the given URL.

    Args:
        url (str): The URL of the resource.
        timeout (int): Timeout for the request in seconds. Defaults to `10`. Use `None` for no timeout. Recommended range is 1-60 seconds. Avoid using `None` in production.
        is_secure (bool): If `True`, raises an error for HTTP status codes indicating failure. Defaults to `True`.

    Returns:
        str: The content type of the resource.

    Raises:
        ValueError: If the URL is invalid or the timeout is negative.
        requests.RequestException: If the request fails for any reason.
    """

    try:
        timeout = None if timeout is None else int(timeout)
    except ValueError:
        raise ValueError("Timeout must be an integer or None.")

    if isinstance(timeout, int) and timeout < 0 and timeout is not None:
        raise ValueError("Timeout must be a non-negative integer or None.")

    url = url.strip().replace(" ", "%20")

    if not is_valid_url(url):
        raise ValueError("Invalid URL provided.")

    try:
        response = requests.head(url, allow_redirects=True, timeout=timeout)

        if is_secure:
            response.raise_for_status()

        content_type = response.headers.get("Content-Type", "Not Found")
        return content_type
    except requests.Timeout:
        raise URLUtilsError("The request timed out.")
    except requests.HTTPError as e:
        raise URLUtilsError(f"Accessing Unsecure URL\n\nHTTP error occurred: {e}")
    except requests.RequestException as e:
        raise URLUtilsError(f"Failed to fetch content type: {e}")
