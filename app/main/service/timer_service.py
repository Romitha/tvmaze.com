from app.main import db
from app.main.model.timer import Timer
from flask import jsonify
from uuid import uuid4


def save_timer(data):

    api_name = data['api_name']
    description = data['description']
    created_at = data['created_at']
    
    if api_name:

        timer = Timer(api_name, description, created_at)
        timer.save()
        return 'Timer save action is success'

    else:

        return 'Timer save action not success'
