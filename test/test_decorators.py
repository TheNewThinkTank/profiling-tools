
import pytest
import time
from profiling_tools.decorators import simple_timer, timer, debug, memoize


def test_simple_timer(capsys):
    """Test simple_timer decorator for correct execution and output."""
    @simple_timer
    def sample_func():
        time.sleep(0.01)
        return "done"

    result = sample_func()
    captured = capsys.readouterr()
    assert "Execution time of sample_func" in captured.out
    assert result == "done"


@pytest.mark.parametrize("unit, expected_unit", [
    ("ns", "ns"),
    ("us", "us"),
    ("ms", "ms"),
    ("s", "s")
])
def test_timer(capsys, unit, expected_unit):
    """Test timer decorator with different time units and precision."""
    @timer(unit=unit, precision=2)
    def sample_func():
        time.sleep(0.01)
        return "done"

    result = sample_func()
    captured = capsys.readouterr()
    assert "sample_func took" in captured.out
    assert f" {expected_unit}" in captured.out
    assert result == "done"


def test_debug(capsys):
    """Test debug decorator for correct output and function call."""
    @debug
    def sample_func(a, b):
        return a + b

    result = sample_func(3, 4)
    captured = capsys.readouterr()
    assert "Calling sample_func with args: (3, 4)" in captured.out
    assert "sample_func returned: 7" in captured.out
    assert result == 7


def test_memoize():
    """Test memoize decorator to ensure caching works correctly."""
    call_count = 0

    @memoize
    def sample_func(x):
        nonlocal call_count
        call_count += 1
        return x * x

    # Call with the same argument multiple times
    assert sample_func(2) == 4
    assert sample_func(2) == 4
    assert sample_func(3) == 9
    assert sample_func(2) == 4
    assert call_count == 2  # `sample_func` should only execute twice
