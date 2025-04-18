from flask import Flask 
from routes import routes
import os 


app = Flask(__name__)
app.register_blueprint(routes)
app.secret_key=os.getenv("FLASK_SECRET_KEY", "default_secret")
app.config['SEND:FILE_MAX_AGE_DEFAULT'] = 0
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

if __name__ == '__main__':
    app.run(debug=True)
    