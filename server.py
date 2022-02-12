from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'count me in'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form',methods=['POST'])
def form_submit():
    print(request.form)
    # ASSIGNING FORM VALUES TO SESSION
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    
    return redirect('/result')


# THIS IS WHERE TO VIEW RESULTS
# CREATE NEW VARIABLES TO STORE THE SESSION KEYS
@app.route('/result')
def result():
    return render_template(
        'print.html',
        name = session['name'],
        location = session['location'],
        language = session['language'],
        comment = session['comment']
        
    )







if __name__=="__main__":
    app.run(debug=True)
