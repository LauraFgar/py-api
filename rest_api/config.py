from decouple import config

class Config:
    SECRET_KEY=config('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI=f"postgresql://{config('PGSQL_USER')}:{config('PGSQL_PASSWORD')}@{config('PGSQL_HOST')}:5432/{config('PGSQL_DATABASE')}"
    SQLALCHEMY_TRACK_MODIFICATIONS=False

configuration = {
    'development': DevelopmentConfig()
}