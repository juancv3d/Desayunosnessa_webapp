from flask import Flask, render_template, request, redirect
import os


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)

    @app.route('/', methods=['GET', 'POST'])
    def home():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            message = request.form['message']
            # print(name, email, phone, message)

        return render_template('index.html')

    return app
