from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

# Path to frontend folder
FRONTEND_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'frontend')

@app.route('/')
def index():
    return send_from_directory(FRONTEND_FOLDER, 'index.html')

@app.route('/gallery')
def gallery():
    return send_from_directory(FRONTEND_FOLDER, 'gallery.html')

@app.route('/about')
def about():
    return send_from_directory(FRONTEND_FOLDER, 'about.html')

@app.route('/api/nails', methods=['GET'])
def get_nails():
    # Sample data - in a real app, this might come from a database
    nails_data = [
        {"id": 1, "design": "Floral", "colors": ["red", "white", "green"], "name": "Aqua Elegance", "description": "Beautiful aqua-themed nail design", "image": "aqua_nail.jpg"},
        {"id": 2, "design": "Sparkle", "colors": ["blue", "silver"], "name": "Blue Sparkle", "description": "Stunning blue sparkle nails", "image": "blue_sparkle_nail.jpg"},
        {"id": 3, "design": "Abstract", "colors": ["pink", "purple", "white"], "name": "Melody Art", "description": "Artistic melody-inspired design", "image": "melody_nail.jpg"},
        {"id": 4, "design": "Abstract", "colors": ["pink", "blue", "white"], "name": "Melody Dreams", "description": "Dreamy artistic nail design", "image": "melody_nail2.jpg"},
        {"id": 5, "design": "Multicolor", "colors": ["red", "blue", "yellow", "green"], "name": "Rainbow Pop", "description": "Vibrant multicolor design", "image": "multicolour_nail.jpg"},
        {"id": 6, "design": "Multicolor", "colors": ["pink", "orange", "yellow"], "name": "Sunset Vibes", "description": "Colorful sunset-inspired nails", "image": "multicolour_nail2.jpg"},
        {"id": 7, "design": "French Tip", "colors": ["pink", "white"], "name": "Pink Tips", "description": "Classic pink tip design", "image": "pink_tip_nail.jpg"},
        {"id": 8, "design": "Glitter", "colors": ["silver", "white"], "name": "Silver Sparkle", "description": "Elegant glitter design", "image": "sparkle_nail.jpg"},
        {"id": 9, "design": "Pattern", "colors": ["black", "white", "pink"], "name": "Spotted Style", "description": "Fun spotted pattern", "image": "spotted_nail.jpg"},
        {"id": 10, "design": "Classic", "colors": ["white"], "name": "Pure White", "description": "Elegant white nails", "image": "white_nail.jpg"},
    ]
    return jsonify(nails_data)

# Serve static files (CSS, JS, etc.) - must be last
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(FRONTEND_FOLDER, path)