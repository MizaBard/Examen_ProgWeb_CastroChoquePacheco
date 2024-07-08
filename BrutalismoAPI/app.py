from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)  # Habilitar CORS

# Cargar datos de arquitectos
with open('data/architects.json') as f:
    architects = json.load(f)

@app.route('/api/architects', methods=['GET'])
def get_architects():
    return jsonify(architects)

@app.route('/images/<path:filename>', methods=['GET'])
def get_image(filename):
    return send_from_directory('images', filename)

if __name__ == '__main__':
    app.run(debug=True)
