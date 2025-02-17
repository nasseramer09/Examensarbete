from flask import Flask
from db.tables.createTables import Table_Creation

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    Table_Creation.create_All_Tables()
    app.run(debug=True)