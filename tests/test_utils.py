"""
test_utils.py
~~~~~~~~~~~~~

Tests for utility helpers in url_content_type_detector.utils.
"""

from __future__ import annotations
import pytest
from url_content_type_detector import utils


def _mock_get_content_type_factory(content_type: str):
    """Create a mock get_content_type function returning a fixed value."""

    def _mock_get_content_type(*_args, **_kwargs):
        return content_type

    return _mock_get_content_type


@pytest.mark.parametrize(
    "function_name,content_type",
    [
        ("is_7z", "application/x-7z-compressed"),
        ("is_audio", "audio/mpeg"),
        ("is_avif", "image/avif"),
        ("is_css", "text/css"),
        ("is_csv", "text/csv"),
        ("is_gif", "image/gif"),
        ("is_graphql", "application/graphql"),
        ("is_gzip", "application/gzip"),
        ("is_html", "text/html"),
        ("is_image", "image/png"),
        ("is_javascript", "application/javascript"),
        ("is_jpeg", "image/jpeg"),
        ("is_json", "application/json"),
        ("is_markdown", "text/markdown"),
        ("is_mp3", "audio/mpeg"),
        ("is_mp4", "video/mp4"),
        ("is_octet_stream", "application/octet-stream"),
        ("is_opendocument", "application/vnd.oasis.opendocument.text"),
        ("is_pdf", "application/pdf"),
        ("is_png", "image/png"),
        ("is_rar", "application/vnd.rar"),
        ("is_svg", "image/svg+xml"),
        ("is_text", "text/plain"),
        ("is_video", "video/webm"),
        ("is_webp", "image/webp"),
        ("is_x_bz2", "application/x-bzip2"),
        ("is_xml", "application/xml"),
        ("is_x_tar", "application/x-tar"),
        ("is_xz", "application/x-xz"),
        ("is_zip", "application/zip"),
        ("is_zstd", "application/zstd"),
    ],
)
def test_utils_return_true_for_matching_content_type(
    monkeypatch, function_name: str, content_type: str
):
    """Verify each utility returns True for matching content types."""
    monkeypatch.setattr(
        utils, "get_content_type", _mock_get_content_type_factory(content_type)
    )

    helper = getattr(utils, function_name)

    assert helper("https://example.com/resource") is True


@pytest.mark.parametrize(
    "function_name",
    [
        "is_7z",
        "is_audio",
        "is_avif",
        "is_css",
        "is_csv",
        "is_excel",
        "is_gif",
        "is_graphql",
        "is_gzip",
        "is_html",
        "is_image",
        "is_javascript",
        "is_jpeg",
        "is_json",
        "is_markdown",
        "is_mp3",
        "is_mp4",
        "is_octet_stream",
        "is_opendocument",
        "is_pdf",
        "is_png",
        "is_powerpoint",
        "is_rar",
        "is_svg",
        "is_text",
        "is_video",
        "is_webp",
        "is_word",
        "is_x_bz2",
        "is_xml",
        "is_x_tar",
        "is_xz",
        "is_zip",
        "is_zstd",
    ],
)
def test_utils_return_false_for_non_matching_content_type(
    monkeypatch, function_name: str
):
    """Verify utilities return False when the content type doesn't match."""
    monkeypatch.setattr(
        utils, "get_content_type", _mock_get_content_type_factory("application/foobar")
    )

    helper = getattr(utils, function_name)

    assert helper("https://example.com/resource") is False


@pytest.mark.parametrize(
    "function_name,content_type",
    [
        ("is_excel", "application/vnd.ms-excel"),
        (
            "is_excel",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        ),
        ("is_powerpoint", "application/vnd.ms-powerpoint"),
        (
            "is_powerpoint",
            "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        ),
        ("is_word", "application/msword"),
        (
            "is_word",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ),
    ],
)
def test_utils_multiple_token_match(monkeypatch, function_name: str, content_type: str):
    """Verify helpers that match multiple tokens return True."""
    monkeypatch.setattr(
        utils, "get_content_type", _mock_get_content_type_factory(content_type)
    )

    helper = getattr(utils, function_name)

    assert helper("https://example.com/resource") is True


def test_utils_pass_through_arguments(monkeypatch):
    """Ensure utils forward timeout and is_secure to get_content_type."""
    called_args = []

    def _mock_get_content_type(*, url, timeout, is_secure):
        called_args.append((url, timeout, is_secure))
        return "text/html"

    monkeypatch.setattr(utils, "get_content_type", _mock_get_content_type)

    result = utils.is_html("https://example.com", timeout=5, is_secure=False)

    assert result is True
    assert called_args == [("https://example.com", 5, False)]
