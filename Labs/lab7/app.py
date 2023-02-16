from flask import Flask,render_template,jsonify,request,make_response,redirect,session
from flask_session import Session
from controller import ContactController  
from contact import Contact
from user import User

app = Flask(__name__,template_folder='./templates')
app.secret_key='HD9E8U234@#%#$%@q$%#$R2309'

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)
ctrl = ContactController()

def logged_user():
    return session.get("user")

app.jinja_env.globals.update(logged_user=logged_user)

@app.route("/login",methods=["GET","POST"])
def login():  
    if request.method=='POST': 
        user = User(request.form)
        res = ctrl.loginUser(user=user)        
        if res:
            session['user'] = res
            return redirect("dashboard")
        else:
            return render_template("login.html", error="Invalid Credentials",data=request.form)
    return render_template("login.html")

@app.route("/logout",methods=["GET"])
def logout():   
    del session['user']
    return render_template("login.html")


@app.route("/deleteContact",methods=["GET"])
def deleteContact():   
    user = session.get('user')
    id = request.args.get("id")
    print("user = ", user)
    ctrl.deleteContact(id=id,user_id=user.get("id"))
    print("id = ", id)
    return redirect("dashboard")



@app.route("/signup",methods=["GET","POST"])
def signup():  
    if request.method=='POST': 
        user = User(request.form)
        res = ctrl.insertNewUser(user=user)
        if type(res)!=str:
            return redirect("login")
        else:
            return render_template("signup.html", error=res,data=request.form)
    return render_template("signup.html")


@app.route("/dashboard")
@app.route("/view_all_contacts")
@app.route("/")
def dashboard(): 
    user = session.get('user')
    if not user:
        return redirect("login")
    contacts = ctrl.getAllContacts() 
    name = request.args.get("name") 
    if name:
        contacts = [x for x in contacts if str(name).strip() in str(x['name']).strip() ]
        
    msg = session.get("msg")
    session['msg'] =  None
    return render_template("contacts.html",contacts=contacts,query=name,msg=msg,user=user)



# Same Route /create_contact for edit / Create -> Polymorphic behaviour triggered by contact.id
@app.route("/editContact",methods=["GET","POST"])
@app.route("/create_contact",methods=["GET","POST"])
def create_contact():
    if not session.get('user'):
        return redirect("login")
    
    contact = {}
    contact_id = request.args.get("id")
    if contact_id:
        contact = [x for x in ctrl.getAllContacts() if str(x.get("id")) == str(contact_id)  ]
        contact = contact[0] if contact else {}
    
     
    
    if request.method=="POST":
        name = request.form.get("name")
        city = request.form.get("city")
        profession = request.form.get("profession")
        mobile_no = request.form.get("mobile_no")
        contact_id = request.form.get("id")
        
        
        temp_mobile_no = mobile_no
        allowed = True
        if "+" in temp_mobile_no and not temp_mobile_no.startswith("+"):
            allowed = False
        if not temp_mobile_no.replace("+","").strip().isnumeric():
            allowed = False
        if len(str(temp_mobile_no))>13 or len(str(temp_mobile_no))<9:
            allowed  = False

        data = {
            "id":contact_id,
            "name":name,
            "city":city,
            "profession":profession,
            "mobileno":mobile_no,
            "user_id":session.get('user').get("id"),
        }
        contact = Contact(data) 
        if not allowed: 
            return render_template("create_contact.html",msg='Please enter a valid Mobile No.',contact=contact)
            
        
        
        if str(contact_id).isnumeric():
            if not ctrl.updateContact(contact):
                return render_template("create_contact.html",msg='Cannot update Record due to database problem.')
        else:
            if not ctrl.insertConatct(contact):
                return render_template("create_contact.html",msg='Cannot insert Record due to database problem.',contact=contact)
            
        
        # session['msg'] = "Contact inserted successfully !"
        return  redirect('/')
    
    if contact_id and not contact:
        return redirect("create_contact")
    return render_template("create_contact.html",contact=contact)




if __name__=="__main__":
    app.run(debug=True,port=8000)