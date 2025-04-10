from flask import Flask, request, jsonify, send_from_directory
from chatbot_logic import get_bot_response
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)  # Enables cross-origin requests from frontend

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static_file(path):
    return send_from_directory(app.static_folder, path)

# ✅ FIXED this route to call the actual bot logic
@app.route('/get', methods=['GET'])
def get_response():
    user_input = request.args.get('msg')
    print("User input:", user_input)

    response = get_bot_response(user_input)  # Use your logic function
    return jsonify({"reply": response})


if __name__ == '__main__':
    app.run(debug=True)
