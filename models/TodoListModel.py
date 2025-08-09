from datetime import date
from configs.dbconfig import db


class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    # Use a callable so the date is evaluated when a task is created, not at import time.
    date_created = db.Column(db.Date, default=date.today)

    def __repr__(self):
        return 'Task %r' % self.id
