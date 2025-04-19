
from flask import Flask, jsonify
from data.dummy_data import attractions
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow access from Flutter app

@app.route('/')
def index():
    return "City Guide API is running!"

@app.route('/api/attractions', methods=['GET'])
def get_attractions():
    return jsonify(attractions)

@app.route('/api/attractions/<int:attraction_id>', methods=['GET'])
def get_attraction(attraction_id):
    attraction = next((a for a in attractions if a['id'] == attraction_id), None)
    if attraction:
        return jsonify(attraction)
    else:
        return jsonify({"error": "Attraction not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
