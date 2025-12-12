# tests/test_math.py - Unit tests đơn giản
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import add_numbers, is_positive

def test_add_numbers():
    """Test hàm cộng số"""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    print("✓ test_add_numbers passed")

def test_is_positive():
    """Test kiểm tra số dương"""
    assert is_positive(5) == True
    assert is_positive(-5) == False
    assert is_positive(0) == False
    print("✓ test_is_positive passed")

def test_sample():
    """Test mẫu"""
    assert 1 + 1 == 2
    print("✓ test_sample passed")

if __name__ == "__main__":
    test_add_numbers()
    test_is_positive()
    test_sample()
    print("✅ All tests passed!")