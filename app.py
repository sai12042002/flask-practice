# importing the flask module

from flask import Flask, render_template, request

# creating the flask app

app = Flask(__name__)

@app.route('/')
def render_home():

    return render_template('home.html')


@app.route('/signUp', methods=['GET'])
def render_signUp():

    return render_template('signUp.html')


@app.route('/register', methods=['GET', 'POST'])
def register():

    firstName = request.form['firstName']
    lastName = request.form['lastName']

    print(firstName, lastName)

    return render_template('login.html')


@app.route('/login', methods=['GET'])
def render_login():

    return render_template('login.html')

if __name__=='__main__':

    app.run()