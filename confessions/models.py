from . import db

class Confession(db.Model):

    __tablename__ = 'confessions'
    id = db.Column(db.Integer, primary_key=True)
    confession = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Confession: {}...>'.format(self.confession[0:15])