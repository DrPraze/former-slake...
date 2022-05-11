from flask import Flask, jsonify, request, send_from_directory, render_template, session, url_for, redirect
from flask_cors import CORS
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy

# from form_contact import ContactForm, csrf
import os

app = Flask(__name__)
CORS(app)

mail = Mail()
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
# csrf.init_app(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'slakenetofficial@gmail.com'
app.config['MAIL_PASSWORD'] = 'Slakee404!'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    slakes = db.Column(db.Integer)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.slakes = slakes + 1

@app.route('/feed.html', methods=['GET'])
def feed():
    if session.get('logged_in'):
        return render_template('home.html')
    else:
        return render_template('feed.html', message=f"Welcome/Become Slakee!")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            db.session.add(User(username=request.form['username'], password=request.form['password'], slakes = 0))
            db.session.commit()
            # return redirect(url_for('login'))
            return render_template('home.html', message = f"Slakes: {User.slakes}")
        except Exception as e:
            # print(e)
            return (f"<h2>{e}</h2>", render_template('home.html', message="User Already Exists"))
    else:
        return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        u = request.form['username']
        p = request.form['password']
        data = User.query.filter_by(username=u, password=p).first()
        if data is not None:
            session['logged_in'] = True
            return redirect(url_for('home'))
        return render_template('home.html', message="Incorrect Details")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))

@app.route('/', methods=['GET'])
def index():
    return send_from_directory('','index.html')

@app.route('/about.html', methods=['GET'])
def about():
    return send_from_directory('', 'about.html')

@app.route('/buy.html', methods = ['GET'])
def buy_data():
    return send_from_directory('', 'buy.html')

@app.route('/subscribe/<name>/<email>', methods=['POST'])
def subscribe(name, email):
    # write data to database
    pass

@app.route('/contact.html', methods=['POST', 'GET'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():        
        print('-------------------------')
        print(request.form['name'])
        print(request.form['email'])
        # print(request.form['subject'])
        print(request.form['message'])       
        print('-------------------------')
        send_message(request.form)
        return redirect('/')    

    return render_template('contact.html', form=form)

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5000)
    args = parser.parse_args()
    port = args.port
    # wallet = Wallet(port)
    # blockchain = Blockchain(wallet.public_key, port)
    app.run(host='0.0.0.0', port=port, debug = True)
