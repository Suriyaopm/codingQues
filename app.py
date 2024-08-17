from flask import Flask, render_template, request, jsonify
from questions import questions
import random

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Get the number of questions from the form
    num_easy = int(request.form['easy'])
    num_medium = int(request.form['medium'])
    num_difficult = int(request.form['difficult'])

    # Select random questions based on the user input
    selected_questions = {
        "easy": random.sample(questions["easy"], min(num_easy, len(questions["easy"]))),
        "medium": random.sample(questions["medium"], min(num_medium, len(questions["medium"]))),
        "difficult": random.sample(questions["difficult"], min(num_difficult, len(questions["difficult"]))),
    }

    return jsonify(selected_questions)

if __name__ == '__main__':
    app.run(debug=True)