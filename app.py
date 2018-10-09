from flask import Flask, redirect, render_template, request, session, url_for
import database
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

db = database.Database()

def get_random_images(page, n):
    subfolder = 'start'
    if page == 1:
        subfolder = 'login'
    files = os.listdir(f'static/images/backgrounds/{subfolder}')
    return random.sample(files, n)

@app.route('/', methods = ['GET'])
def start():
    if 'user' not in session:
        image_list = get_random_images(0, 5)
        # return render_template('start.html', images = image_list)
        return render_template('homepage.html', image = image_list)
    else:
        pass

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'user' in session:
            return redirect(url_for('start'))
        image = get_random_images(1, 1)[0]
        return render_template('login.html', image = image)

    if request.method == 'POST':
        username = (request.form['username']).lower().strip()
        password = (request.form['password'])
        return redirect(url_for('start'))

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        if 'user' in session:
            return redirect(url_for('start'))
        image = get_random_images(1, 1)[0]
        return render_template('register.html', image = image)

    if request.method == 'POST':
        username = (request.form['username']).lower().strip()
        password = (request.form['password'])
        return redirect(url_for('start'))

@app.route('/homepage', methods = ['GET'])
def homepage():
    pass

if __name__ == '__main__':
    app.run(port=8080, debug=True)
