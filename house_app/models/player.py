from house_app.config.mysqlconnection import connectToMySQL
from flask import flash
from house_app import bcrypt
from house_app import app

class Player:
    def __init__( self , data ):
        self.id = data['id']
        self.username = data['username']
        self.password = data['password']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


#CLASS METHODS
    #GET METHODS
    @classmethod
    def get_by_username(cls, data):
        query = "SELECT * FROM players WHERE username = %(username)s;"

        results = connectToMySQL('house_db').query_db(query, data)
        
        if not results or len(results)<1:
            return False

        else:
            return cls(results[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM players WHERE id = %(id)s;"

        results = connectToMySQL('house_db').query_db(query, data)
        
        if not results or len(results)<1:
            return False

        else:
            return cls(results[0])
    #END


    #CREATE,EDIT,DELETE METHODS
    @classmethod
    def make_player(cls, data):
        query = "INSERT INTO players (username, password, location, created_at, updated_at ) VALUES (%(username)s , %(password)s, 'entry', NOW() , NOW());"

        return connectToMySQL('house_db').query_db( query, data )

    @classmethod
    def change_location(cls, data):
        query = "UPDATE players SET location = %(location)s, updated_at = NOW() WHERE id= %(id)s"

        return connectToMySQL('house_db').query_db( query, data )
    #END

#STATIC METHODS
    @staticmethod
    def validate_inputs(user):
        is_valid = True
        if len(user['username']) < 2:
            flash("must be at least 2 characters.")
            is_valid = False
        if len(user['password']) < 5:
            flash("Password must be at least 5 characters.")
            is_valid = False
        if user['password'] != user['pass_con']:
            flash("Passwords do not match")
            is_valid = False

        return is_valid

    @staticmethod
    def validate_login(player):
        is_valid = True
        
        found_player = Player.get_by_username(player)
        print(found_player.password)

        if found_player:
            if not bcrypt.check_password_hash(found_player.password, player['password']):
                flash("Incorrect Login")
                is_valid = False
        
        else:
            flash('Incorrect Login')
            is_valid = False

        return is_valid