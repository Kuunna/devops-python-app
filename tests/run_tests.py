#!/usr/bin/env python3
# run_tests.py - Script chạy tất cả tests
import subprocess
import sys
import os

def run_pytest():
    """Chạy pytest"""
    print("🚀 Running pytest...")
    result = subprocess.run(
        ["pytest", "tests/", "-v", "--tb=short"],
        capture_output=True,
        text=True
    )
    
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    return result.returncode == 0

def run_custom_tests():
    """Chạy custom tests"""
    print("\n🔧 Running custom tests...")
    
    # Import và chạy math tests
    from tests.test_math import test_add_numbers, test_is_positive, test_sample
    from tests.test_api import run_all_api_tests
    
    try:
        test_add_numbers()
        test_is_positive()
        test_sample()
        print("✅ Math tests passed")
    except AssertionError as e:
        print(f"❌ Math test failed: {e}")
        return False
    
    if run_all_api_tests():
        print("✅ API tests passed")
        return True
    else:
        print("❌ API tests failed")
        return False

def main():
    """Chính"""
    print("=" * 50)
    print("🧪 RUNNING AUTOMATED TESTS")
    print("=" * 50)
    
    all_passed = True
    
    # Chạy pytest
    if not run_pytest():
        all_passed = False
    
    # Chạy custom tests
    if not run_custom_tests():
        all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("✅ ALL TESTS PASSED!")
        sys.exit(0)
    else:
        print("❌ SOME TESTS FAILED")
        sys.exit(1)

if __name__ == "__main__":
    main()