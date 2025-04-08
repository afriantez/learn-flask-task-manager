from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='../frontend')
CORS(app)

tasks = []

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')