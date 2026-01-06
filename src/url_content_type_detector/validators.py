import validators


def is_valid_url(url: str) -> bool:
    """Check if the provided string is a valid URL."""
    return validators.url(url)
