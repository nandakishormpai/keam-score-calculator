from myapp import app
from flask import render_template,request
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/event', methods=['GET', 'POST'])
def event():
    if request.method == 'POST':
        event_name = request.form['title']
        event_img = request.form['envetbg']
        event_disc = request.form['content']
        event_insta = request.form['insta']

    return render_template('event.html',event_name=event_name,event_img=event_img,event_disc=event_disc,event_insta=event_insta)