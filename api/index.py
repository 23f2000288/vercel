from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load student data from JSON file
with open(os.path.join(os.path.dirname(__file__), 'q-vercel-python.json')) as f:
    students = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [students.get(name, 0) for name in names]
    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run()
