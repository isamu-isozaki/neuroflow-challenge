"""
Author: Isamu Isozaki (isamu.website@gmail.com)
Description: description
Created:  2021-12-01T16:33:02.647Z
Modified: !date!
Modified By: modifier
"""
from neuroflow.extensions import db
import datetime
class Mood(db.Model):
    __tablename__ = 'mood'
    id = db.Column(db.Integer, primary_key=True)
    mood = db.Column(db.Float)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)