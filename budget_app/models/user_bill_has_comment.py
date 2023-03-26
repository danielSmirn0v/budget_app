
from budget_app.config.mysqlconnection import connectToMySQL

from budget_app.models import users, main_bills

from flask import flash

class Bill_comment:
    db = 'budget_app'

    def __init__(self,data):
        self.id = data['id']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creater = None