from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/question', methods=['GET', 'POST'])
def question():
    if request.method == 'POST':
        funding_status = request.form.get('funding_status')
        class_grades = request.form.getlist('class_grades')
        # Process the answers and determine the next steps
        return redirect(url_for('results', funding_status=funding_status, class_grades=class_grades))
    return render_template('question.html')

@app.route('/results')
def results():
    funding_status = request.args.get('funding_status')
    class_grades = request.args.getlist('class_grades')
    # Logic to display results based on funding status and class grades
    return render_template('results.html', funding_status=funding_status, class_grades=class_grades)