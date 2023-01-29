
from app import db
from utils.DateFormat import DateFormat

class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    duration = db.Column(db.Integer)
    released = db.Column(db.String)

    def __init__(self, id, title, duration, released):
        self.id = id
        self.title = title
        self.duration = duration
        self.released = released

    def to_JSON(self):
        return {
            'id': self.id,
            'title': self.title,
            'duration': self.duration,
            'released': self.released#DateFormat.convert_date(self.released)
        }