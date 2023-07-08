from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'piyushdas3110@gmail.com'  # Update with your email
app.config['MAIL_PASSWORD'] = 'Pabloescobar123*'  # Update with your email password

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    msg = Message('New Contact Form Submission', sender='your-email@gmail.com', recipients=['piyushdas3110@gmail.com'])  # Update with your email
    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

    mail.send(msg)

    return 'Message sent successfully!'


if __name__ == '__main__':
    app.run()
