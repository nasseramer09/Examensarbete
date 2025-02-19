from flask import Flask
from db.tables.createTables import Table_Creation
from Backend.services import AuthenticationServices

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    Table_Creation.create_All_Tables()
    #AuthenticationServices.createAcount("Nasser", "Amer", "namer", "securepassword", "admin")
    #print(AuthenticationServices.login("namer", "securepassword"))

    app.run(debug=True)