from flask import Flask
from routes import routes
import os 
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
app.register_blueprint(routes)
app.secret_key=os.getenv("FLASK_SECRET_KEY", "default_secret")

if __name__ == '__main__':
    app.run(debug=True)
    