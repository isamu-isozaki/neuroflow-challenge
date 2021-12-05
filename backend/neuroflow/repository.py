"""
Author: Isamu Isozaki (isamu.website@gmail.com)
Description: description
Created:  2021-12-01T17:13:36.074Z
Modified: !date!
Modified By: modifier
"""
from neuroflow.models import Mood, User, Token
from neuroflow.extensions import db
from datetime import datetime, timedelta
def create_mood(mood_num, user):
    """
    Create a mood object
    """
    mood = Mood(mood=mood_num, user=user)
    db.session.add(mood)
    db.session.commit()

def create_user(email, first_name, last_name, password):
    user = load_user_from_email(email)
    if user:
        return False
    user = User(email=email, first_name=first_name, last_name=last_name, password=password)
    db.session.add(user)
    db.session.commit()
    return True

def load_user_from_email(email):
    return db.session.query(User).filter_by(email=email).first()

def load_token(access_token=None, refresh_token=None):
    if access_token:
        return Token.query.filter_by(access_token=access_token).first()

def save_token(token):
    toks = Token.query.filter_by(user_id=token['user_id'])
    # make sure that every client has only one token connected to a user
    for t in toks:
        db.session.delete(t)

    expires_in = 3600
    expires = datetime.utcnow() + timedelta(seconds=expires_in)

    tok = Token(
        access_token=token['access_token'],
        refresh_token=token['refresh_token'],
        expires=expires,
        user_id=token['user_id'],
    )
    db.session.add(tok)
    db.session.commit()
    return tok

def get_authorized(request):
    if not request.headers.get('Authorization', None):
        return
    access_token = request.headers['Authorization']
    token = load_token(access_token=access_token)
    if not token:
        return False
    if token.expires < datetime.utcnow():
        return False
    return token.user