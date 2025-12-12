import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
import unittest

class TestApp(unittest.TestCase):
    
    def setUp(self):
        """Chuẩn bị test client"""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_home_endpoint(self):
        """Test endpoint chính"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello', response.data)
    
    def test_health_endpoint(self):
        """Test health check"""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'OK', response.data)
    
    def test_version_endpoint(self):
        """Test version endpoint"""
        response = self.app.get('/version')
        self.assertEqual(response.status_code, 200)
    
    def test_404_endpoint(self):
        """Test endpoint không tồn tại"""
        response = self.app.get('/notfound')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()