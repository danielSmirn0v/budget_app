
from budget_app.config.mysqlconnection import connectToMySQL

from budget_app.models import users, user_bill_has_comment,sub_bills

from flask import flash

class Main_bill:
    db = 'budget_app'

    def __init__(self,data):
        self.id = data['id']
        self.bill_type = data['bill_type']
        self.budget_main_bills_id = data['budget_main_bills_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creater = None
        self.sub_bills = []


    @classmethod 
    def save(cls,data):
        query = '''INSERT INTO main_bills (bill_type, budget_main_bills_id) 
                    VALUES(%(bill_type)s, %(budget_main_bills_id)s)'''
        result = connectToMySQL(cls.db).query_db(query, data)
        print(result)
        return result

    @classmethod
    def get_all_from_id(cls,data):
        query = """SELECT *
                    FROM budget
                    LEFT JOIN users
                    ON budget.user_id = users.id
                    LEFT JOIN main_bills
                    ON main_bills.budget_main_bills_id = budget.id
                    LEFT JOIN sub_bills
                    ON sub_bills.main_bill_id = main_bills.id
                    WHERE users.id = %(id)s;"""
        result = connectToMySQL(cls.db).query_db(query,data)
        return result


    @classmethod
    def update_budget(cls,data):
        query="UPDATE main_bills SET bill_type = %(bill_type)s WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @staticmethod
    def validate_bill_name(bill):
        is_valid = True
        if len(bill['bill_type']) < 2:
            flash("Name must be at least 2 characters long.")
            is_valid = False
        return is_valid 