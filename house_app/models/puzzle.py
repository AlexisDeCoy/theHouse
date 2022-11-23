from house_app.config.mysqlconnection import connectToMySQL
from flask import flash
from house_app import bcrypt
from house_app import app

class Puzzle:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        
    @classmethod
    def completed_puzzle(cls, data):
        query = "SELECT * FROM solved_puzzles WHERE player_id = %(player_id)s AND puzzle_id = %(puzzle_id)s"

        results = connectToMySQL('house_db').query_db(query, data)

        if results:
            return True
        else:
            return False

    @classmethod
    def mark_solved(cls, data):
        query = "INSERT INTO solved_puzzles (player_id, puzzle_id) VALUES (%(player_id)s, %(puzzle_id)s)"

        return connectToMySQL('house_db').query_db(query, data)