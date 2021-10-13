from flask import Flask, render_template, request, redirect
import os


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)

    @app.route('/')
    def home():
        return render_template('index.html')

    return app
