from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config
from .entities.Movie import Movie

class MovieModel():

    def __init__(self):
        self.engine = create_engine(f"postgresql://{config('PGSQL_USER')}:{config('PGSQL_PASSWORD')}@{config('PGSQL_HOST')}:5432/{config('PGSQL_DATABASE')}")
        self.Session = sessionmaker(bind=self.engine)

    # @classmethod
    def get_movies(self):
        session = self.Session()
        movies = session.query(Movie).order_by(Movie.title).all()
        movies = [Movie(row.id, row.title, row.duration, row.released).to_JSON()
                          for row in movies]
        session.close()
        return movies