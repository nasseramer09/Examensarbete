from flask import Blueprint, render_template, request, redirect, session, url_for

from Backend.services import AuthenticationServices

routes = Blueprint("routes", __name__, template_folder="templates")




@routes.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userName=request.form['username']
        password=request.form['password']

        loginCheck= AuthenticationServices.login(userName, password)

        if loginCheck["message"] == "Success":
            print('login successfuly, redirecting to checkrol')
            session['username'] = userName
            session['role'] = loginCheck['role']
            return redirect(url_for('routes.checkRole'))
        else:
            print('login failed', loginCheck['message'])
            return render_template('login.html', error=" fel användarnamn eller lösenord!" )
        
    return render_template('login.html')

@routes.route('/register', methods=['GET','POST'])
def register():

    if request.method=='POST':
        firstName=request.form['firstName']
        lastName=request.form['lastName']
        userName=request.form['userName']
        password=request.form['password']
        role=request.form['role']
        AuthenticationServices.createAcount(firstName,lastName,userName,password,role)
        return redirect(url_for('/routes.login'))
    
    return redirect(url_for('user_managment'))


@routes.route('/user_manager')
def user_managment():

    users = AuthenticationServices.user_managment()
    
    return render_template('user_manager.html')




    

#check the role of the user and redirect to pages aloweed access based on role
@routes.route('/checkRole' )
def checkRole():
   print(session)
   if 'username' not in session:
       print("no username in session redirecting to login page")
       return redirect(url_for('routes.login'))

   return render_template('home.html', userName=session['username'], role=session['role'])
   
