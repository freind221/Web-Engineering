
# from flask import Flask ,render_template,request

# app = Flask(__name__)


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
# @app.route('/test')
# def test():
#     return render_template("Test.html")
# @app.route('/registerform')
# def registerForm():
#     return render_template("RegisterStudent.html")

# @app.route('/register', methods=["POST"])
# def register():
#     rollno = request.form["rollno"]
#     name=request.form["name"]
#     semmester = request.form["semmester"]
#     cgpa = request.form["cgpa"]
#     print(rollno,name,semmester,cgpa)
#     # create Student
#     # DB Handler object create
#     # using DB handler call insertStudent
#     if name=="Ali":
#         return render_template("dashboard.html")
#     else:
#         return render_template("RegisterStudent.html")
# if __name__ == '__main__':
#     app.run()
