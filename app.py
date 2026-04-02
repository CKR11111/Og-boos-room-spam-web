import os
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_spam', methods=['POST'])
def send_spam():
    try:
        data = request.get_json()
        uid = data.get('user_id')
        dur = data.get('duration', 5)
        
        api_url = f"https://ckrunknown-ckrpro.hf.space/spam?user_id={uid}&duration={dur}"
        
        # 120 seconds wait garchha (2 minutes)
        response = requests.get(api_url, timeout=120)
        
        return jsonify({
            "status": "success", 
            "res": response.text
        })
    except requests.exceptions.Timeout:
        return jsonify({"status": "error", "res": "API Response Timeout (Took too long)!"})
    except Exception as e:
        return jsonify({"status": "error", "res": f"Error: {str(e)}"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
