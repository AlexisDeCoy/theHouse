from flask import render_template, request, redirect, session
from house_app import app
from house_app.models.player import Player, bcrypt
from house_app.models.item import Item
from house_app.models.puzzle import Puzzle

#LOGIN AND REGISTRATION
@app.route("/")
def index():
    return render_template("login.html")

@app.route("/create_player", methods=['POST'])
def create():

    if not Player.validate_inputs(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    data = {
        **request.form,
        "password" : pw_hash
    }

    session['uid'] = Player.make_player(data)

    return redirect('/intro1')

@app.route('/login', methods=['POST'])
def login():
    if not Player.validate_login(request.form):
        return redirect('/')
    
    found_player = Player.get_by_username(request.form)

    session['uid'] = found_player.id

    return redirect(f'/{found_player.location}')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
#END


#INTRODUCTION
@app.route("/intro1")
def intro():
    if not 'uid' in session:
        return redirect('/')

    return render_template("/intro/intro.html")

@app.route("/intro2")
def intro2():
    if not 'uid' in session:
        return redirect('/')
    return render_template("/intro/intro2.html")

@app.route("/intro3")
def intro3():
    if not 'uid' in session:
        return redirect('/')
    return render_template("/intro/intro3.html")

@app.route("/intro4")
def intro4():
    if not 'uid' in session:
        return redirect('/')
    return render_template("/intro/intro4.html")

@app.route("/intro5")
def intro5():
    if not 'uid' in session:
        return redirect('/')
    return render_template("/intro/intro5.html")

@app.route("/intro6")
def intro6():
    if not 'uid' in session:
        return redirect('/')
    return render_template("/intro/intro6.html")
#END


#LOCATIONS
@app.route("/entry")
def entry():
    if not 'uid' in session:
        return redirect('/')

    data = {
        'id' : session['uid'],
        'location' : 'entry'
    }

    Player.change_location(data)
    return render_template("/rooms/entry.html")

@app.route("/dining")
def dining():
    if not 'uid' in session:
        return redirect('/')

    data = {
        'id' : session['uid'],
        'location' : 'dining'
    }

    Player.change_location(data)
    return render_template("/rooms/dining.html")

@app.route("/kitchen")
def kitchen():
    if not 'uid' in session:
        return redirect('/')

    data = {
        'id' : session['uid'],
        'location' : 'kitchen'
    }
    
    check = {
        'user_id': session['uid'],
        'item_id': 14
    }

    bottle = Item.have_item(check)
    Player.change_location(data)
    return render_template("/rooms/kitchen.html", bottle=bottle)

@app.route("/ds-hallway")
def ds_hallway():
    if not 'uid' in session:
        return redirect('/')

    data = {
        'id' : session['uid'],
        'location' : 'ds-hallway'
    }

    puzzle = {
        'player_id': session['uid'],
        'puzzle_id': 1
    }

    door = Puzzle.completed_puzzle(puzzle)
    Player.change_location(data)
    return render_template("/rooms/ds_hallway.html", door=door)

@app.route("/ds-bath")
def ds_bath():
    if not 'uid' in session:
        return redirect('/')

    data = {
        'id' : session['uid'],
        'location' : 'ds-bath'
    }

    check = {
        'user_id': session['uid'],
        'item_id': 16
    }

    mirror = Item.have_item(check)
    Player.change_location(data)
    return render_template("/rooms/ds_bath.html", mirror=mirror)

@app.route("/us-hallway")
def us_hallway():
    if not 'uid' in session:
        return redirect('/')

    data = {
        'id' : session['uid'],
        'location' : 'us-hallway'
    }

    Player.change_location(data)
    return render_template("/rooms/us_hallway.html")

@app.route("/us-bath")
def us_bath():
    if not 'uid' in session:
        return redirect('/')

    data = {
        'id' : session['uid'],
        'location' : 'us-bath'
    }

    Player.change_location(data)
    return render_template("/rooms/us_bath.html")

@app.route("/bedroom")
def bedroom():
    if not 'uid' in session:
        return redirect('/')

    data = {
        'id' : session['uid'],
        'location' : 'bedroom'
    }

    puzzle = {
        'player_id': session['uid'],
        'puzzle_id': 2
    }

    clock = Puzzle.completed_puzzle(puzzle)
    Player.change_location(data)
    return render_template("/rooms/bedroom.html", clock=clock)

@app.route("/study")
def study():
    if not 'uid' in session:
        return redirect('/')

    data = {
        'id' : session['uid'],
        'location' : 'study'
    }

    Player.change_location(data)
    return render_template("/rooms/study.html")

@app.route("/backyard")
def backyard():
    if not 'uid' in session:
        return redirect('/')

    data = {
        'id' : session['uid'],
        'location' : 'backyard'
    }

    Player.change_location(data)
    return render_template("/rooms/backyard.html")

@app.route("/basement")
def basement():
    if not 'uid' in session:
        return redirect('/')

    data = {
        'id' : session['uid'],
        'location' : 'basement'
    }

    check = {
        'user_id': session['uid'],
        'item_id': 4
    }

    Player.change_location(data)
    lighter = Item.have_item(check)
    return render_template("/rooms/basement.html", lighter=lighter)

@app.route("/greenhouse")
def greenhouse():
    if not 'uid' in session:
        return redirect('/')

    data = {
        'id' : session['uid'],
        'location' : 'greenhouse'
    }

    Player.change_location(data)
    return render_template("/rooms/greenhouse.html")

@app.route("/hidden-room")
def hidden_room():
    if not 'uid' in session:
        return redirect('/')

    data = {
        'id' : session['uid'],
        'location' : 'hidden-room'
    }

    check = {
        'user_id': session['uid'],
        'item_id': 12
    }

    book = Item.have_item(check)

    Player.change_location(data)
    return render_template("/rooms/hidden_room.html", book=book)
