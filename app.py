# app.py - Phiên bản có logic để test
from flask import Flask, jsonify
import os

app = Flask(__name__)

def add_numbers(a, b):
    """Hàm đơn giản để test"""
    return a + b

def is_positive(number):
    """Kiểm tra số dương"""
    return number > 0

@app.route('/')
def home():
    return jsonify({
        "message": "DevOps Python App with Tests",
        "status": "running",
        "version": "1.0.0"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/add/<int:a>/<int:b>')
def add_route(a, b):
    result = add_numbers(a, b)
    return jsonify({"result": result})

@app.route('/check-positive/<int:number>')
def check_positive(number):
    is_pos = is_positive(number)
    return jsonify({"number": number, "is_positive": is_pos})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)