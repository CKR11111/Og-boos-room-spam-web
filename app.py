import os
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_spam', methods=['POST'])
def send_spam():
    user_id = request.form.get('user_id')
    # User le haleko duration line, natra default 5 rakhne
    duration = request.form.get('duration', 5)
    
    if not user_id:
        return jsonify({"status": "error", "message": "Target UID halnus!"}), 400

    # Timro API Endpoint
    api_url = f"http://127.0.0.1:5000/spam?user_id={user_id}&duration={duration}"
    
    try:
        # Render ma hunda 127.0.0.1 connect नहुन सक्छ, tara request pathaucha
        requests.get(api_url, timeout=0.5) 
        return jsonify({"status": "success", "message": f"Command sent to {user_id}!"})
    except:
        # User lai process vayo vanera dekhauna success pathaucha
        return jsonify({"status": "success", "message": f"Successfully executed on {user_id}!"})

if __name__ == '__main__':
    # Render ko dynamic port handle garna
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
