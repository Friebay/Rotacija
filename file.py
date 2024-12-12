from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/rotacija', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        step = request.form.get('step')
        if step == 'funding_status':
            funding_status = request.form['funding_status']
            if funding_status == 'yes':
                return render_template('rotacija.html', step='funded', funding_status=funding_status)
            else:
                return render_template('rotacija.html', step='not_funded', funding_status=funding_status)
        elif step == 'used_funding':
            used_funding = request.form['used_funding']
            funding_status = request.form.get('funding_status')
            if used_funding == 'yes':
                return render_template('rotacija.html', step='no_funding', funding_status=funding_status)
            else:
                return render_template('rotacija.html', step='grades', funding_status=funding_status)
        elif step == 'submit_grades':
            grades = request.form.getlist('grades')
            grades = [float(grade) for grade in grades if grade]
            total_grades = len(grades)
            if total_grades > 0:
                percent_below_5 = len([grade for grade in grades if grade < 5]) / total_grades * 100
                percent_5_to_7 = len([grade for grade in grades if 5 <= grade < 7]) / total_grades * 100
                percent_7_to_9 = len([grade for grade in grades if 7 <= grade < 9]) / total_grades * 100
                percent_above_9 = len([grade for grade in grades if grade >= 9]) / total_grades * 100
            else:
                percent_below_5 = percent_5_to_7 = percent_7_to_9 = percent_above_9 = 0

            funding_status = request.form.get('funding_status')
            if funding_status == 'yes':
                if percent_below_5 == 0 and percent_5_to_7 == 0:
                    funding_status_message = "You are not at risk of losing your funding."
                elif percent_below_5 > 0 or percent_5_to_7 > 0:
                    funding_status_message = "There is a possibility that you will lose your funding."
                else:
                    funding_status_message = "You will lose your funding."
            else:
                if percent_7_to_9 > 0 or percent_above_9 > 0:
                    funding_status_message = "You have a possibility to get funded."
                else:
                    funding_status_message = "You won't get funded."

            return render_template('rotacija.html', step='final', grades=grades, percent_below_5=percent_below_5, percent_5_to_7=percent_5_to_7, percent_7_to_9=percent_7_to_9, percent_above_9=percent_above_9, funding_status_message=funding_status_message, funding_status=funding_status)
    return render_template('rotacija.html', step='funding_status')

if __name__ == '__main__':
    app.run(debug=True)