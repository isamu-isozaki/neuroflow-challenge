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
from sqlalchemy import and_

def create_mood(mood_num, user):
    """
    Create a mood object
    """
    mood = Mood(mood=mood_num, user=user, streak=previous_streak(user)+1)
    db.session.add(mood)
    db.session.flush()
    mood_dict = mood.__dict__.copy()
    db.session.commit()
    return mood_dict

def create_user(email, first_name, last_name, password):
    user = load_user_from_email(email)
    if user:
        return False
    user = User(email=email, first_name=first_name, last_name=last_name, password=password)
    db.session.add(user)
    db.session.commit()
    return user

def load_user_from_email(email):
    return db.session.query(User).filter_by(email=email).first()

def load_token(access_token=None, refresh_token=None):
    if access_token:
        return Token.query.filter_by(access_token=access_token).first()

def load_moods_from_user(user):
    moods = db.session.query(Mood).filter_by(user=user).all()
    mood_dicts = []
    for mood in moods:
        mood = mood.__dict__.copy()
        del mood['_sa_instance_state']
        mood_dicts.append(mood)
    return mood_dicts

def previous_streak(user):
    one_day_before = datetime.utcnow() - timedelta(days=1)
    two_days_before = datetime.utcnow() - timedelta(days=2)
    mood_one_day_ago = db.session.query(Mood).filter(Mood.user==user).filter(and_(Mood.created_date >= two_days_before, Mood.created_date <=one_day_before)).first()
    if mood_one_day_ago:
        return mood_one_day_ago.streak
    return 0

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
        return False
    access_token = request.headers['Authorization']
    token = load_token(access_token=access_token)
    if not token:
        return False
    if token.expires < datetime.utcnow():
        return False
    return token.user