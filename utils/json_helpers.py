import pytest

def safe_json_parse(response):
    """Safely parse response to JSON or fail the test."""
    try:
        return response.json()
    except Exception as e:
        pytest.fail(f"Response is not valid JSON: {e}")
