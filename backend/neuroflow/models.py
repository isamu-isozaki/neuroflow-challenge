"""
Author: Isamu Isozaki (isamu.website@gmail.com)
Description: description
Created:  2021-12-01T16:33:02.647Z
Modified: !date!
Modified By: modifier
"""
from neuroflow.extensions import db, bcrypt
from flask_login import UserMixin
import datetime
import os
from sqlalchemy.ext.hybrid import hybrid_property
import binascii

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    _password = db.Column(db.String, nullable=False)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, val):
        seasoned, salt = self.season(val)
        self._password = bcrypt.generate_password_hash(seasoned).decode('utf-8')

        if not self.id:
            db.session.add(self)
            db.session.flush()
            salt.user_id = self.id
            db.session.add(salt)
            db.session.commit()

        return self._password

    def check_password(self, val):
        seasoned, _ = self.season(val)
        return bcrypt.check_password_hash(self._password, seasoned)

    def get_user_id(self):
        return self.id

    @hybrid_property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def season(self, val):
        salt = None

        if self.id:
            salt = db.session.query(Salt).filter_by(user_id=self.id).first()

        if not salt:
            salt = Salt(salt=str(binascii.b2a_hex(os.urandom(100))))

        pepper = os.getenv('PEPPER')
        seasoned = val + salt.salt + pepper

        return seasoned, salt

class Salt(db.Model):
    __tablename__ = 'salt'
    id = db.Column(db.Integer, primary_key=True)
    salt = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))

    user = db.relationship('User')

class Mood(db.Model):
    __tablename__ = 'mood'
    id = db.Column(db.Integer, primary_key=True)
    mood = db.Column(db.Float)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User')

class Token(db.Model):
    __tablename__ = 'token'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    access_token = db.Column(db.String(255), unique=True)
    refresh_token = db.Column(db.String(255), unique=True)
    expires = db.Column(db.DateTime)
    _scopes = db.Column(db.Text)

    user = db.relationship('User')

    def delete(self):
        db.session.delete(self)
        db.session.commit()

        return self

    @hybrid_property
    def scopes(self):
        if self._scopes:
            return self._scopes.split()

        return []