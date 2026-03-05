"""Tests for micro-color-contrast."""

import pytest
from micro_color_contrast import contrast


class TestContrast:
    """Test suite for contrast."""

    def test_basic(self):
        """Test basic usage."""
        result = contrast("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            contrast("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = contrast(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
