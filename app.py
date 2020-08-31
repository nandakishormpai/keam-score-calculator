from flask import Flask,flash,render_template,request
from boto.s3.connection import S3Connection
import os
app=Flask(__name__)

app.config['SECRET_KEY']=S3Connection(os.environ['SECRET_KEY'])

@app.route('/', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        student_maths = int(request.form['maths'])
        student_chemistry = int(request.form['chemistry'])
        student_physics=int(request.form['physics'])
        student_keam=float(request.form['keam'])
        if(request.form['board']=="state"):
            score=(student_maths+student_physics+student_chemistry)*0.8823529 + student_keam*0.3125
        else:
            score=(student_maths+student_physics+student_chemistry) + student_keam*0.3125
        flash(score, 'danger')
        return render_template('main.html')
    else:
        return render_template('main.html')


if __name__=='__main__' :
    app.run()
