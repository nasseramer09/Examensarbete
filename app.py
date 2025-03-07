from flask import Flask, render_template, request
from db.tables.createTables import Table_Creation
from Backend.services import AuthenticationServices

app = Flask(__name__)


#@app.route("/")
#def landingPage():
 #   return render_template('login.html')

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        userName=request.form['username']
        password=request.form['password']

        loginCheck= AuthenticationServices.login(userName, password)

        if loginCheck["message"] == "Success":
            print('ok')
            return render_template('home.html')
        else:
            print('inte ok')

            return f"fel användarnamn eller lösenord"
        
    return render_template('landingPage.html')

if __name__ == '__main__':
    Table_Creation.create_All_Tables()
    app.run(debug=True)