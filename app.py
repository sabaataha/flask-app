from flask import Flask , request, jsonify
from openai import OpenAI
import os  ,openai

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/ask" ,  methods=['POST'])
def ask_question():
    data = request.get_json()
    question_text = data.get('question')
    
    if not question_text:
        return jsonify({'error': 'No question provided'}), 400
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question_text}]
        )
        answer_text = response.choices[0].message.content
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    return jsonify({'answer_text': answer_text}), 200
  

if __name__ == '__main__':
    app.run(debug=True)