# Silvia Pineda Jimenez
# 3/25/2026
# CST 205 M/W 2-4pm
# Lab — Flask, Part 1
# GitHub link: paste your GitHub repo link here

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# Task 2 — Hello World without templates
@app.route('/')
def hello():
    return '''
    <h1>Hello world from Flask!</h1>

    <p>Silvia P. : idk - I use it a lot when texting.</p>
    <p>Maria G. : brb - She uses it when she is busy.</p>
    <p>Jessica R. : lol - She uses it when something is funny.</p>
    <p>Alex M. : tbh - He uses it when being honest.</p>
    '''

# Task 3 and 4 — Template route with Bootstrap
@app.route('/silvia')
def silvia():
    return render_template('template.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)