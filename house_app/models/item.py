from house_app.config.mysqlconnection import connectToMySQL
from flask import flash
from house_app import bcrypt
from house_app import app

class Item:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.img = data['img']
        self.description = data['description']

#CLASS METHODS
    #GET METHODS
    @classmethod
    def get_items(cls, data):
        query = "SELECT items.id, name, img, description FROM inventory JOIN items ON items.id = item_id JOIN players ON players.id = player_id WHERE players.id = %(player_id)s;"

        results = connectToMySQL('house_db').query_db(query, data)

        items = []

        for item in results:
            items.append(cls(item))
        
        return items

    @classmethod
    def get_item_by_id(cls, data):
        query = "SELECT * FROM items WHERE id = %(item_id)s "

        results = connectToMySQL('house_db').query_db(query, data)


        items = []

        for item in results:
            items.append(cls(item))
        
        return items[0]

    @classmethod
    def have_item(cls, data):
        query = "SELECT * FROM inventory WHERE player_id = %(user_id)s AND item_id = %(item_id)s"

        results = connectToMySQL('house_db').query_db(query, data)

        if results:
            return True
        else:
            return False

    @classmethod
    def add_item(cls, data):
        query = "INSERT INTO inventory (player_id, item_id) VALUES (%(player_id)s, %(item_id)s)"

        return connectToMySQL('house_db').query_db(query, data)

    @classmethod
    def switch_potion(cls, data):
        query = "UPDATE inventory SET item_id = 15 WHERE player_id = %(player_id)s and item_id = 14"

        return connectToMySQL('house_db').query_db(query, data)

    @classmethod
    def switch_mirror(cls, data):
        query = "UPDATE inventory SET item_id = 23 WHERE player_id = %(player_id)s and item_id = 16"

        return connectToMySQL('house_db').query_db(query, data)