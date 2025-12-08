from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

# Path to frontend folder
FRONTEND_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'frontend')

@app.route('/')
def index():
    return send_from_directory(FRONTEND_FOLDER, 'index.html')

# Serve static files (CSS, JS, etc.)
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(FRONTEND_FOLDER, path)

@app.route('/api/nails', methods=['GET'])
def get_nails():
    # Sample data - in a real app, this might come from a database
    nails_data = [
        {"id": 1, "design": "Floral", "colors": ["red", "white", "green"], "name": "supernail", "description": "very nice nails"},
        {"id": 2, "design": "Geometric", "colors": ["blue", "black", "silver"], "name": "geonail", "description": "stylish geometric nails" },
    ]
    return jsonify(nails_data)