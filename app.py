from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from DevOps Python App with Tests!",
        "version": "1.0.0",
        "status": "running",
        "endpoints": ["/", "/health", "/version", "/api/test"]
    })

@app.route('/health')
def health():
    return "OK", 200

@app.route('/version')
def version():
    return jsonify({"version": "1.0.0", "tests": "enabled"})

@app.route('/api/test')
def test():
    return jsonify({"test": "success", "unit_tests": "passed"})

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print(f"🚀 Starting app with unit tests on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)