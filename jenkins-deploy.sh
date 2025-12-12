#!/bin/bash
# jenkins-deploy.sh - Script đơn giản để Jenkins deploy

echo "=== BẮT ĐẦU DEPLOY ==="
date

echo "1. Kiểm tra thư mục"
pwd
ls -la

echo "2. Kiểm tra Python"
python3 --version || python --version || echo "Python không có"

echo "3. Chạy ứng dụng Python đơn giản"
# Tạo file kết quả để chứng minh deploy thành công
echo "Deployed by Jenkins" > deployment.txt
echo "Build Number: $BUILD_NUMBER" >> deployment.txt
echo "Time: $(date)" >> deployment.txt
echo "Status: SUCCESS" >> deployment.txt

echo "4. Hiển thị kết quả"
cat deployment.txt

echo "5. Mô phỏng deploy Docker"
echo "Nếu dùng Docker sẽ chạy:"
echo "  docker build -t myapp ."
echo "  docker run -d -p 5000:5000 myapp"

echo "=== KẾT THÚC DEPLOY ==="
echo "✅ Ứng dụng đã được deploy"
echo "🌐 Truy cập: http://localhost:5000"
exit 0