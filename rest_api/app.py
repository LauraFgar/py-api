from flask import Flask
from config import configuration
from flask_cors import CORS
from decouple import config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#cors
CORS(app, resources={"*":{"origins":config('APP_ORIGIN')}})

#configurations 
app.config.from_object(configuration['development'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#migrations
from models.entities.Movie import Movie

#Routes
from routes import Movie
app.register_blueprint(Movie.movie)

def page_not_found(error):
    return "<h1>Not found page</h1>", 404

app.register_error_handler(404, page_not_found)
app.run()
