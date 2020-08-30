from flask import render_template
from main import app
@app.route('/', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        score="Please Enter Your Scores"
        student_maths = int(request.form['maths'])
        student_chemistry = int(request.form['chemistry'])
        student_physics=int(request.form['physics'])
        student_keam=float(request.form['keam'])
        if(request.form['board']=="state"):
            score=(student_maths+student_physics+student_physics)*0.8823529 + student_keam*0.3125
        else:
            score=(student_maths+student_physics+student_physics) + student_keam*0.3125
        flash(score, 'danger')
        return render_template('main.html')
    else:
        return render_template('main.html')