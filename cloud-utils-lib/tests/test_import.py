from cloud_utils_lib import greet


def test_greet_returns_string():
    result = greet("Priii")
    assert isinstance(result, str)
    assert "Hello" in result
