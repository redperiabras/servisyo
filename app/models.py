from sqlalchemy.ext.hybrid import hybrid_property
from flask.ext.login import UserMixin

from app import db, bcrypt


class User(db.Model, UserMixin):

    ''' A user who has an account on the website. '''

    __tablename__ = 'users'

    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String, primary_key=True)
    gender = db.Column(db.String)
    profession = db.Column(db.String)
    confirmation = db.Column(db.Boolean)
    geolat = db.Column(db.String)
    geolng = db.Column(db.String)
    _password = db.Column(db.String)

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def check_password(self, plaintext):
        return bcrypt.check_password_hash(self.password, plaintext)

    def get_id(self):
        return self.email

    def to_json(self):
        json_post = {
            'email'           : self.emal,
            'first_name'    : self.first_name,
            'last_name'     : self.last_name,
            'email'        : self.email,
            'password': self.password,
            'profession'     : self.profession,
            'gender'     : self.gender,
            'geolat'      : self.geolat,
            'geolng'        : self.geolng,
            'phone': self.phone,
            'gender': self.gender
        }
        return json_post

