from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY='AIzaSyD04Ap2sE9Dx4LPGiP1y5ldqZNIfgaT-DY'
genai.configure(api_key=GOOGLE_API_KEY)

model = "models/text-bison-001"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['GET','POST'])
def chat():
    # Get the question from the request
    question = request.json['question']

    # Define the model and prompt
    model = genai.GenerativeModel('gemini-pro')
    prompt = f'''Answer this question very shortly : {question}.
    '''

    # Generate the response using the palm library
    # completion = palm.generate_text(
    #     model=model,
    #     prompt=prompt,
    #     temperature=0,
    # )
    reply = model.generate_content(prompt)

    # Return the response as JSON
    return jsonify({'response': reply.text})

if __name__ == '__main__':
    app.run()
