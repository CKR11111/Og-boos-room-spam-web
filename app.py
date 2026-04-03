import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_spam', methods=['POST'])
def send_spam():
    data = request.get_json()
    user_id = data.get('user_id')
    
    if not user_id:
        return jsonify({"status": "error", "message": "UID is required!"}), 400

    # API Endpoint
    api_url = "https://gst-stations-causes-infections.trycloudflare.com/spam"
    params = {'user_id': user_id, 'duration': 5}

    try:
        response = requests.get(api_url, params=params, timeout=15)
        return jsonify({"status": "success", "message": "Command Sent!"})
    except:
        return jsonify({"status": "error", "message": "API Connection Failed"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
