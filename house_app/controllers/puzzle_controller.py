from flask import render_template, request, redirect, session
from house_app import app
from house_app.models.player import Player, bcrypt
from house_app.models.item import Item
from house_app.models.puzzle import Puzzle

@app.route('/clock-pz')
def clk_pz():
    return render_template('/puzzles/clock_pz.html')


@app.route('/clock-input', methods=['GET', 'POST'])
def clk_input():
    hours = request.form['hours']
    minutes = request.form['minutes']

    if int(hours) == 10 and int(minutes) == 20:
        solved = True

        data = {
            'player_id': session['uid'],
            'puzzle_id': 2
        }
        Puzzle.mark_solved(data)
    else:
        solved = False
    return render_template('/puzzles/clock_return.html', solved=solved)

@app.route('/bm-door')
def bm_door():
    check = {
        'user_id': session['uid'],
        'item_id': 3
    }

    keyring = Item.have_item(check)
    return render_template('/puzzles/basement_door.html', keyring=keyring)

@app.route('/door-open', methods=['GET', 'POST'])
def open_door():
    key_number = request.form['key_number']

    if int(key_number) == 82:
        solved = True

        data = {
            'player_id': session['uid'],
            'puzzle_id': 1
        }
        Puzzle.mark_solved(data)
    else:
        solved = False
    return render_template('/puzzles/door_return.html', solved=solved)

@app.route('/potion')
def make_potion():
    check = {
        'user_id': session['uid'],
        'item_id': 22
    }
    milk = {
        'user_id': session['uid'],
        'item_id': 18
    }
    night = {
        'user_id': session['uid'],
        'item_id': 19
    }
    worm = {
        'user_id': session['uid'],
        'item_id': 21
    }

    recipe = Item.have_item(check)
    milkweed = Item.have_item(milk)
    nightshade = Item.have_item(night)
    wormwood = Item.have_item(worm)

    if milkweed and nightshade and wormwood:
        ingredients = True
    else:
        ingredients = False
    return render_template("/puzzles/potion.html", recipe=recipe, ingredients=ingredients)

@app.route('/make-potion')
def potion_inventory():
    data = {
        'player_id': session['uid']
    }

    Item.switch_potion(data)
    return redirect('/kitchen')


@app.route('/fix-mirror')
def fix_mirror():
    return render_template('/puzzles/mirror_pz.html')

@app.route('/mirror-input', methods=['GET', 'POST'])
def mirror_input():
    word = request.form['word']

    if word == "XLIII":
        solved = True

        data = {
            'player_id': session['uid'],
            'puzzle_id': 3
        }

        mirror = {
            'player_id': session['uid']
        }

        Item.switch_mirror(data)
        Puzzle.mark_solved(data)
    else:
        solved = False
    return render_template('/puzzles/mirror_return.html', solved=solved)

@app.route('/ritual')
def perfrom_ritual():
    pot = {
        'user_id': session['uid'],
        'item_id': 15
    }
    cand = {
        'user_id': session['uid'],
        'item_id': 2
    }

    puzzle = {
        'player_id': session['uid'],
        'puzzle_id': 3
    }

    potion = Item.have_item(pot)
    print(potion)
    candles = Item.have_item(cand)
    print(candles)
    mirror = Puzzle.completed_puzzle(puzzle)
    print(mirror)

    if potion and candles and mirror:
        materials = True
    else:
        materials = False
    return render_template("/puzzles/ritual.html", materials=materials)

@app.route('/ending')
def thank_you():
    return render_template('/ending.html')
