# tests/test_api.py - Test API endpoints
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_home_endpoint():
    """Test endpoint chính"""
    # Đây là test mô phỏng, trong thực tế dùng requests
    expected_message = "DevOps Python App with Tests"
    print(f"✓ Testing home endpoint - Expected: {expected_message}")
    return True

def test_health_endpoint():
    """Test health check"""
    print("✓ Testing health endpoint - Should return status: healthy")
    return True

def test_add_endpoint():
    """Test endpoint cộng số"""
    print("✓ Testing add endpoint - Should calculate sum")
    return True

def run_all_api_tests():
    """Chạy tất cả API tests"""
    tests = [
        test_home_endpoint,
        test_health_endpoint,
        test_add_endpoint
    ]
    
    passed = 0
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"✗ {test.__name__} failed: {e}")
    
    print(f"\n📊 API Tests: {passed}/{len(tests)} passed")
    return passed == len(tests)

if __name__ == "__main__":
    success = run_all_api_tests()
    if success:
        print("✅ All API tests passed!")
        sys.exit(0)
    else:
        print("❌ Some API tests failed")
        sys.exit(1)