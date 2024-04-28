from .. import db, bcrypt


class Train(db.Model):
    """
        User Model for storing user related details
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, unique = True)
    source = db.Column(db.String(255), nullable=False)
    destination = db.Column(db.String(255), nullable=False)
    max_seats = db.Column(db.Integer, nullable=False)
    occupied_seats = db.Column(db.Integer, nullable=False, default=0)
    
