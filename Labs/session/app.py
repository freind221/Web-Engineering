from contact import Contact
from user import User
from flask import Flask ,render_template,request, flash, session
from flask_session import Session
from controller import ContactController
from db import DB
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
from user import User

from flask_login import login_user, login_required, logout_user, current_user
import mysql.connector
app = Flask(__name__)
app.config.from_object("config")
app.secret_key = app.config["SECRET_KEY"]

app.permanent_session_lifetime = timedelta(minutes=10)
Session(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
@app.route('/contactform')
def registerForm():
    return render_template("contact.html")



@app.route('/logout')
def logout():
    session.clear()
    return render_template("login.html")




@app.route('/login', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        session.permanent = True
        
        
        
        
        che = str(generate_password_hash(
                password, method='sha256'))
        
        print(che)
        db = DB()
        user = User('', '')
        user = db.login(email=email, password=che)
        db.getUserId(email=email, password=che)
        
        # print(user)
        if(user):
            session["email"] = email
            session["password"] = password
            session["id"] = id
            return render_template("search.html")
        else:
            
            flash('Incorrect Password Try again.', category='error')
          
    return render_template("login.html")

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        # user = User.query.filter_by(email=email).first()
        # if user:
        #     flash('User already exists', category='error')
        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            db = DB()
            new_user = User(email=email, password=generate_password_hash(
                password1, method='sha256'))
            passw = str(generate_password_hash(
                password1, method='sha256'))
            check = db.register_user(email=email, password=passw)
            if(check):
                id = db.getUserId(email=email, password=passw)
                session["email"] = email
                session["id"] = id
                session["password"] = passw
            
                # login_user(user)
                flash('Account Created Successfully', category='success')
                return render_template("search.html")
            else:
                flash('Account not created', category='error')
                return render_template("sign_up.html")
    
   
    return render_template("sign_up.html")

@app.route('/register', methods=["POST"])
def register():
    name = request.form["name"]
    mobileno=request.form["mobileno"]
    city = request.form["city"]
    profession = request.form["profession"]
    print(name, mobileno, city, profession)
    
    db = DB()
    # check = db.register_contact(name, mobileno, city, profession)
    contact = Contact('', '', '', '')
    controller = ContactController()
    check = controller.register(db, name, mobileno, profession, session.get("id"))
    print(db.get_contact('kamran'))
    # using DB handler call insertStudent
    if check:
       
        return render_template("search.html", data = contact.name)

    else:
        return render_template("contact.html", msg = "could not register")

@app.route('/search', methods=["POST"])
def search():
    pass
if __name__ == '__main__':
    app.run()
