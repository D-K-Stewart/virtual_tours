from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

from flask_app.models.user import User
# DATABASE = ''

class Tour:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.location = db_data['location']
        self.description = db_data['description']
        self.date = db_data['date']
        self.link = db_data['link']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user_id = db_data['user_id']
        
    @property  
    def creator(self):
        return User.get_one({'id': self.user_id})
# ----------------------------------------------------------------C

    @classmethod # doesn't taget the instance but instead targets the class itself
    def create(cls,data):
        query = "INSERT INTO tours (name, location, description, date, link, created_at, updated_at, user_id) VALUES (%(name)s, %(location)s, %(description)s, %(date)s, %(link)s, NOW(), NOW(), %(user_id)s);"
        return connectToMySQL('virtual_tours').query_db(query, data)
    
        # list of dictionaries

    # ---------------------------------------------------------------R

    @classmethod # doesn't taget the instance but instead targets the class itself
    def get_all(cls):
        query = "SELECT * FROM tours"
        results = connectToMySQL('virtual_tours').query_db(query)  #list of dictionaries
        
        print(results)
        if len(results):
            all_tours = []
            for tours in results:
                all_tours.append(cls(tours))
            return all_tours



    @classmethod # doesn't taget the instance but instead targets the class itself
    def update(cls, data):
        query = "UPDATE tours SET name=%(name)s, location=%(location)s, description=%(description)s, date=%(date)s, link=%(link)s WHERE id=%(id)s;"
        return connectToMySQL('virtual_tours').query_db(query, data)


    @classmethod # doesn't taget the instance but instead targets the class itself
    def get_one(cls, data):
        query = "SELECT * FROM tours WHERE tours.id = %(id)s;"
        results = connectToMySQL('virtual_tours').query_db(query, data)  #list of dictionaries
        if not results:
            return results

        data = {
            **results[0]
        }
        return cls(data)
    

    @classmethod 
    def delete_tour(cls, data):
        query = "DELETE FROM tours WHERE id=%(id)s;"
        return connectToMySQL('virtual_tours').query_db(query, data)



    @staticmethod
    def validate_tour(tour):
        is_valid = True # we assume this is true
        if len(tour['name']) < 3:
            flash("Name must be at least 3 characters.", 'error_tour_name')
            is_valid = False
        if len(tour['location']) < 2:
            flash("Location must be at least 3 characters.", 'error_tour_location')
            is_valid = False
        # if len(show['release_date']) < 0:
        #     flash("Month Day Year must be given.", 'error_release_date')
        #     is_valid = False
        if len(tour['description']) < 3:
            flash("Description must be at least 3 characters.", 'error_description')
            is_valid = False
        if len(tour['link']) < 3:
            flash("Link must be at least 3 characters.", 'error_link')
            is_valid = False

        return is_valid