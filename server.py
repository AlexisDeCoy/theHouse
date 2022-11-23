from house_app.controllers import player_controller
from house_app.controllers import item_controller
from house_app.controllers import puzzle_controller
from house_app import app

if __name__ == "__main__":
    app.run(debug=True)

# MVC = Models, Views, Controllers