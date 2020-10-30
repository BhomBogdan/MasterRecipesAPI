from flask import Flask
from flask_cors import CORS


app = Flask(__name__)

CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/bhom/Proiecte/React+Flask/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False