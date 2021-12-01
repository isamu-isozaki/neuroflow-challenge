"""
Author: Isamu Isozaki (isamu.website@gmail.com)
Description: description
Created:  2021-12-01T17:13:36.074Z
Modified: !date!
Modified By: modifier
"""
from neuroflow.models import Mood
from neuroflow.extensions import db
def create_mood(mood_num):
    """
    Create a mood object
    """
    mood = Mood(mood=mood_num)
    db.session.add(mood)
    db.session.commit()