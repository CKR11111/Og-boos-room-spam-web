import os
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_spam', methods=['POST'])
def send_spam():
    data = request.get_json()
    uid = data.get('user_id')
    dur = data.get('duration', 5)
    
    api_url = f"https://ckrunknown-ckrpro.hf.space/spam?user_id={uid}&duration={dur}"
    
    try:
        # 30 second timeout rakheko chhu taaki API le time liyo bhane pani crash nahos
        response = requests.get(api_url, timeout=30)
        return jsonify({"status": "success", "res": response.text})
    except Exception as e:
        return jsonify({"status": "error", "res": str(e)})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
