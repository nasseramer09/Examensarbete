from flask import Flask, render_template, request, session, redirect, url_for
from db.tables.createTables import Table_Creation
from Backend.services import AuthenticationServices

app = Flask(__name__)
app.secret_key="SessionKey"


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userName=request.form['username']
        password=request.form['password']

        loginCheck= AuthenticationServices.login(userName, password)

        if loginCheck["message"] == "Success":
            session['username']=userName
            session['role']=loginCheck['role']
            return redirect(url_for('checkRole'))
        else:
            
            return render_template('login.html', error=" fel användarnamn eller lösenord!" )
        
    return render_template('login.html')

#check the role of the user and redirect to pages aloweed access based on role
@app.route('/checkRole')
def checkRole():
   if 'username' not in session:
       return redirect(url_for('login'))
   
   return render_template('home.html', userName=session['username'], role=session['role'])

if __name__ == '__main__':
    Table_Creation.create_All_Tables()
    app.run(debug=True)