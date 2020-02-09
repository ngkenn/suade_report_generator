
from app import db, app

# The report model: Has attributes id and type
# Extends db.Model from SQLAlchemy - so we can call a query on this class...
# which will query the db (defined in __init__) and return the Report object
class Report(db.Model):
    __tablename__ = 'reports' # override the default tablename
    # basic attributes of the Report
    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.Text)
    
    def __init__(self,type):
       self.type = type

