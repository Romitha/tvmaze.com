from .. import db


class Timer(db.Model):
    """This class represents the Setup table."""

    __tablename__ = 'timer'

    id = db.Column(db.Integer, primary_key=True)
    api_name = db.Column(db.String(455))
    description = db.Column(db.String(1024))
    created_at = db.Column(db.String(255))
    

    def __init__(self, api_name, description, created_at):

        self.api_name = api_name
        self.description = description
        self.created_at = created_at

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Timer.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Timer '{}'>".format(self.api_name)
