import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

try:
    json_path = os.path.join(os.path.dirname(__file__), 'q-vercel-python.json')
    with open(json_path) as f:
        students = json.load(f)
except Exception as e:
    print(f"Error loading JSON: {e}")
    students = {}

@app.route('/', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [students.get(name, 0) for name in names]
    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run()
