import pytest
from src.pricing import calculate_laundry_cost

# common cases:

# TC-01
def test_regular_integer_weight():
    assert calculate_laundry_cost(3, "regular") == 18000

# TC-02
def test_regular_decimal_weight():
    assert calculate_laundry_cost(2.5, "regular") == 15000

# TC-03
def test_express_integer_weight():
    assert calculate_laundry_cost(2, "express") == 20000

# TC-04
def test_express_decimal_weight():
    assert calculate_laundry_cost(1.5, "express") == 15000

# TC-05
def test_case_insensitive_and_whitespace():
    assert calculate_laundry_cost(2, " Express ") ==  20000   

# Edge Cases:

# TC-06
def test_minimum_weight_threshold():
    assert calculate_laundry_cost(0.5, "regular") == 6000

# TC-07
def test_exact_minimum_weight():
    assert calculate_laundry_cost(1.0, "regular") == 6000

# TC-08
def test_zero_or_negative_weight():
    with pytest.raises(ValueError):
        calculate_laundry_cost(0, "regular")
    with pytest.raises(ValueError):
        calculate_laundry_cost(-1.5, "regular")

# TC-09
def test_invalid_service_type():
    with pytest.raises(ValueError):
        calculate_laundry_cost(3, "super_fast")
# TC-10
def test_invalid_data_type():
    with pytest.raises(TypeError):
        calculate_laundry_cost("tiga kg", "regular")
    with pytest.raises(TypeError):
        calculate_laundry_cost(True, "regular")
        