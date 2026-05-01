from flask import Flask, render_template,jsonify,request
import requests

app= Flask(__name__)

@app.route('/',methods=['GET'])
def apiAwakening():
    return render_template('index.html')
@app.route('/chat',methods=['POST'])
def chat():
    user_message=request.json['message']
    ollama_response = requests.post('http://localhost:11434/api/generate', json={
        "model": "my-llama",
        "prompt": user_message,
        "stream": False
    })
    ai_reply = ollama_response.json()['response']
    
    
    return jsonify({"reply": ai_reply})


if __name__ == '__main__':
    app.run(port=5000, debug=True)