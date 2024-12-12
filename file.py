from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        step = request.form.get('step')
        if step == 'funding_status':
            funding_status = request.form['funding_status']
            if funding_status == 'yes':
                return render_template('index.html', step='funded')
            else:
                return render_template('index.html', step='not_funded')
        elif step == 'used_funding':
            used_funding = request.form['used_funding']
            if used_funding == 'yes':
                return render_template('index.html', step='no_funding')
            else:
                return render_template('index.html', step='grades')
        elif step == 'submit_grades':
            grades = request.form.getlist('grades')
            return "Grades submitted: " + ", ".join(grades)
    return render_template('index.html', step='funding_status')

if __name__ == '__main__':
    app.run(debug=True)