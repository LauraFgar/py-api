from flask import Blueprint, jsonify

# Models
from models.MovieModel import MovieModel

movie = Blueprint('movie', __name__, url_prefix='/movies')

@movie.route('/')
def get_movies():

    try:
        movies = MovieModel().get_movies()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
