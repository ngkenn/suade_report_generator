# config for the flask app
# used in app/__init__.py
class Config(object):
    DEBUG = True
    DEVELOPMENT = True # Set a development flag. useful if both prod and dev configs are added
    db_user = 'interview'
    db_pass = 'uo4uu3AeF3'
    db_host = 'candidate.suade.org/suade'
    SQLALCHEMY_DATABASE_URI = f"postgres://{db_user}:{db_pass}@{db_host}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
