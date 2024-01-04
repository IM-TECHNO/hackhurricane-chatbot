from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
GOOGLE_API_KEY='YOUR_API_KEY'
genai.configure(api_key=GOOGLE_API_KEY)

model = "models/text-bison-001"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['GET','POST'])
def chat():
    question = request.json['question']
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    prompt = f'''Answer this question shortly and be precise. DO NOT ANSWER IF IT INVOLVES NSFW CONTENT. Here is your question : {question}.
    '''
    reply = chat.send_message(question)

    return jsonify({'response': reply.text})

if __name__ == '__main__':
    app.run()
