from datetime import datetime
from configs.dbconfig import db

class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.Date, default=datetime.today().date)
    
    def __repr__(self):
        return 'Task %r' % self.id
