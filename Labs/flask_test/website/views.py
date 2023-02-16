from flask import Blueprint, render_template, request


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/registerform')
def registerForm():
    return render_template("RegisterStudent.html")

@views.route('/register', methods=["POST"])
def register():
    rollno = request.form["rollno"]
    name=request.form["name"]
    semmester = request.form["semmester"]
    cgpa = request.form["cgpa"]
    print(rollno,name,semmester,cgpa)
    # create Student
    # DB Handler object create
    # using DB handler call insertStudent
    if name=="Ali":
        return render_template("dashboard.html")
    else:
        return render_template("register.html")