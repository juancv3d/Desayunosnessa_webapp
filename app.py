from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os


email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = email
    app.config['MAIL_PASSWORD'] = password
    mail = Mail(app)

    @app.route('/', methods=['GET', 'POST'])
    def home():
        if request.method == 'POST':
            name = request.form['name']
            email_user = request.form['email']
            phone = request.form['phone']
            message = request.form['message']
            message_to_send = f"Name: {name}\nEmail: {email_user}\nPhone: {phone}\nMessage: {message}"
            msg = Message(subject="Contacto desayunosnessa",
                          sender=email, recipients=[email], body=message_to_send)
            mail.send(msg)

        return render_template('index.html')

    return app
