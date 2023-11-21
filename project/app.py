from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import random
app = Flask(__name__)

# Initialize the SQLite database
conn = sqlite3.connect('quiz.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        score INTEGER
    )
''')
conn.commit()
conn.close()

# Define quiz questions
quiz_questions = quiz_questions = [ 
  {
    "id": "python1",
    "text": "What is Python?",
    "options": ["A type of snake", "A programming language", "A database management system"],
    "correct_option": "2"
  },
  {
    "id": "python2",
    "text": "Which of the following is a correct way to comment in Python?",
    "options": ["// This is a comment", "# This is a comment", "/* This is a comment */"],
    "correct_option": "2"
  },
  {
    "id": "python3",
    "text": "What is the purpose of the 'if __name__ == '__main__':",
    "options": ["To define a function", "To execute code only if the script is run directly", "To import modules"],
    "correct_option": "2"
  },
  {
    "id": "python3",
    "text": "What is the purpose of the 'if __name__ == '__main__':",
    "options": ["To define a function", "To execute code only if the script is run directly", "To import modules"],
    "correct_option": "2"
  },
  {
    "id": "python4",
    "text": "Which of the following is a mutable data type in Python?",
    "options": ["String", "Tuple", "List"],
    "correct_option": "3"
  },
  {
    "id": "python5",
    "text": "What does the 'import' keyword do in Python?",
    "options": ["Define a new function", "Import a module or library", "Create a variable"],
    "correct_option": "2"
  },
  {
    "id": "python6",
    "text": "What is the purpose of 'pip' in Python?",
    "options": ["A package manager for Python", "A web framework", "A version control system"],
    "correct_option": "1"
  },
  {
    "id": "python7",
    "text": "Which statement is used for exiting a loop prematurely in Python?",
    "options": ["break", "continue", "exit"],
    "correct_option": "1"
  },
  {
    "id": "python8",
    "text": "What is the purpose of the 'try', 'except', and 'finally' blocks in Python?",
    "options": ["Define a function", "Handle exceptions", "Create a loop"],
    "correct_option": "2"
  },
  {
    "id": "python9",
    "text": "What is the primary use of a Python dictionary?",
    "options": ["Sorting data", "Storing key-value pairs", "Performing mathematical operations"],
    "correct_option": "2"
  },
  {
    "id": "python10",
    "text": "In Python, what is the purpose of the 'lambda' keyword?",
    "options": ["Define a constant variable", "Create an anonymous function", "Import a library"],
    "correct_option": "2"
  },
  {
    "id": "python11",
    "text": "Which module in Python provides support for working with regular expressions?",
    "options": ["re", "regex", "regexp"],
    "correct_option": "1"
  },
  {
    "id": "python12",
    "text": "What is the purpose of the 'yield' keyword in Python?",
    "options": ["Return a value from a function", "Pause execution and return a value", "Define a class"],
    "correct_option": "2"
  },
  {
    "id": "python13",
    "text": "Which of the following is used for error handling in Python?",
    "options": ["try", "catch", "handle"],
    "correct_option": "1"
  },
  {
    "id": "python14",
    "text": "What does the 'range()' function do in Python?",
    "options": ["Generate a sequence of numbers", "Round a floating-point number", "Find the length of a string"],
    "correct_option": "1"
  },
  {
    "id": "python15",
    "text": "In Python, what is the purpose of 'self' in a class method?",
    "options": ["Reference to the current instance of the class", "Alias for 'super'", "Indicate a private method"],
    "correct_option": "1"
  },
  {
    "id": "python16",
    "text": "Which module in Python is used for working with dates and times?",
    "options": ["time", "datetime", "calendar"],
    "correct_option": "2"
  },
  {
    "id": "python17",
    "text": "What is the purpose of '__init__' in a Python class?",
    "options": ["Initialize a variable", "Create a static method", "Define a constructor"],
    "correct_option": "3"
  },
  {
    "id": "python18",
    "text": "What does the 'with' statement do in Python?",
    "options": ["Define a new variable", "Create a loop", "Ensure proper resource management"],
    "correct_option": "3"
  },
  {
    "id": "python19",
    "text": "Which method is used to remove an item from a list in Python?",
    "options": ["remove()", "pop()", "discard()"],
    "correct_option": "2"
  },
  {
    "id": "python20",
    "text": "What is the purpose of the 'sys' module in Python?",
    "options": ["File input/output operations", "System-specific parameters and functions", "String manipulation"],
    "correct_option": "2"
  },



    
    # Add more question objects as needed
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Process the quiz answers and calculate the score
        name = request.form['name']
        email = request.form['email']
        score = calculate_score(request.form)

        # Save user details and score to the database
        conn = sqlite3.connect('quiz.db', check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email, score) VALUES (?, ?, ?)', (name, email, score))
        conn.commit()
        conn.close()

        return redirect(url_for('result', score=score))

    return render_template('quiz.html', quiz_questions=quiz_questions)

@app.route('/result/<int:score>')
def result(score):
    recommendation = recommend_course(score)
    return render_template('result.html', score=score, recommendation=recommendation)
def calculate_score(form_data):
    # Placeholder implementation, replace with your scoring logic
    score = 0
    for key, value in form_data.items():
        if key.startswith('q'):
            question_index = int(key[1]) - 1
            correct_option = quiz_questions[question_index]['correct_option']
            print(f"Checking question {question_index + 1}: selected={value}, correct={correct_option}")
            
            if value == correct_option:
                score += 1

    return score


def recommend_course(score):
    if score >= 15:
        return "Congratulations! You have a strong understanding of the topics covered in the quiz. Consider advanced courses in python."
    elif 5 <= score < 10:
        return "You have a good grasp of the basics. Consider intermediate-level courses to further enhance your knowledge."
    else:
        return "It looks like you are just getting started. Consider introductory courses to build a solid foundation."



if __name__ == '__main__':
    app.run(debug=True)
