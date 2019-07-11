from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/no')
def no():
    return render_template('no.html')

@app.route('/yes')
def yes():
    return render_template('yes.html')

@app.route('/life')
def life():
    return render_template('life.html')

@app.route('/therapy')
def therapy():
    return render_template('therapy.html')

@app.route('/location')
def location():
    return render_template('location.html')

@app.route('/dress')
def dress():
    return render_template('dress.html')














app.run(debug =True)