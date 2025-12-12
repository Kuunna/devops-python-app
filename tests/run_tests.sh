#!/bin/bash
echo "=== RUNNING UNIT TESTS ==="

echo "1. Checking Python environment..."
python3 --version || python --version

echo "2. Installing dependencies..."
pip3 install -r requirements.txt 2>/dev/null || pip install -r requirements.txt 2>/dev/null

echo "3. Running Python unittest..."
python3 -m pytest tests/ -v --tb=short 2>&1 | tee test_results.txt

echo "4. Running custom test runner..."
python3 test_runner.py 2>&1 | tee -a test_results.txt

echo "5. Creating test report..."
echo "=== TEST SUMMARY ===" > test_report.txt
echo "Date: $(date)" >> test_report.txt
echo "Python: $(python3 --version 2>/dev/null || python --version 2>/dev/null)" >> test_report.txt
echo "" >> test_report.txt

# Kiểm tra kết quả
if grep -q "FAILED" test_results.txt || grep -q "ERROR" test_results.txt; then
    echo "Status: FAILED" >> test_report.txt
    echo "Some tests failed" >> test_report.txt
    exit 1
else
    echo "Status: PASSED" >> test_report.txt
    echo "All tests passed!" >> test_report.txt
    exit 0
fi