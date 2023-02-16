
from flask import Flask ,render_template,request
from flask import Blueprint

from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    
    db.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix='/')
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')
    from .models import User, Note
    with app.app_context():
        db.create_all()
        
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    # create_database(app)
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
# @app.route('/test')
# def test():
#     return render_template("Test.html")
# @app.route('/registerform')
# def registerForm():
#     return render_template("RegisterStudent.html")

# # @app.route('/register', methods=["POST"])
# # def register():
# #     rollno = request.form["rollno"]
# #     name=request.form["name"]
# #     semmester = request.form["semmester"]
# #     cgpa = request.form["cgpa"]
# #     print(rollno,name,semmester,cgpa)
# #     # create Student
# #     # DB Handler object create
# #     # using DB handler call insertStudent
# #     if name=="Ali":
# #         return render_template("dashboard.html")
# #     else:
# #         return render_template("RegisterStudent.html")
# # if __name__ == '__main__':
# #     app.run()
