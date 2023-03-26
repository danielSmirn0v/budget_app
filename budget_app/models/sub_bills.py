
from budget_app.config.mysqlconnection import connectToMySQL

from budget_app.models import users, main_bills

from flask import flash

class Sub_bills:
    db = 'budget_app'

    def __init__(self,data):
        self.id = data['id']
        self.sub_bill_name = data['sub_bill_name']
        self.amount = data['amount']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creater = None


    @classmethod 
    def save(cls,data):
        query = 'INSERT INTO sub_bills (sub_bill_name, amount , main_bill_id) VALUES(%(bill_type)s,%(amount)s,, %(main_bill_id)s)'
        result = connectToMySQL(cls.db).query_db(query, data)
        print(result)
        return result