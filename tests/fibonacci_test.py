import pytest
from fibonacci import fibonacci


@pytest.mark.parametrize("position,expected", [
    (1, 1),
    (2, 1),
    (5, 5),
    (10, 55),
    (15, 610),
])
def test_calculate_fibonacci(position, expected):
    assert fibonacci.generate_fibonacci(position) == expected, "Fibonacci value was not as expected"


@pytest.mark.parametrize("position", [0, -5])
def test_error_should_appear_on_non_positive_value(position):
    with pytest.raises(ValueError, match="Value should be greater than 0"):
        fibonacci.generate_fibonacci(position)


@pytest.mark.parametrize("position", ["some", 1.5, b'0101'])
def test_error_should_appear_on_non_integer_value(position):
    with pytest.raises(TypeError):
        fibonacci.generate_fibonacci(position)
