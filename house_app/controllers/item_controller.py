from flask import render_template, request, redirect, session
from house_app import app
from house_app.models.player import Player, bcrypt
from house_app.models.item import Item

#PICKUPS
@app.route('/bm-mound')
def mound():
    check = {
        'user_id': session['uid'],
        'item_id': 7
    }

    boots = Item.have_item(check)
    return render_template('/pickups/bm-mound.html', boots=boots)

@app.route('/br-clock')
def clock():
    return render_template('/pickups/br-clock.html')

@app.route('/br-open')
def br_open():
    return render_template('/pickups/br-open.html')

@app.route('/by-dig')
def dig():
    check = {
        'user_id': session['uid'],
        'item_id': 1
    }

    trowel = Item.have_item(check)
    return render_template('/pickups/by-dig.html', trowel=trowel)

@app.route('/by-stone')
def stone():
    return render_template('/pickups/by-stone.html')

@app.route('/dr-candles')
def candles():
    return render_template('/pickups/dr-candles.html')

@app.route('/dsb-cabinet')
def dsb_cabinet():
    return render_template('/pickups/dsb-cabinet.html')

@app.route('/dsh-cabinet')
def dsh_cabinet():
    return render_template('/pickups/dsh-cabinet.html')

@app.route('/gh-plants')
def plants():
    return render_template('/pickups/gh-plants.html')

@app.route("/gh-table")
def gh_table():
    return render_template('/pickups/gh-table.html')

@app.route('/k-drawers')
def drawers():
    return render_template('/pickups/k-drawers.html')

@app.route('/k-utensils')
def utensils():
    return render_template('/pickups/k-utensils.html')

@app.route('/st-books')
def books():
    check = {
        'user_id': session['uid'],
        'item_id': 11
    }

    log = Item.have_item(check)
    return render_template('/pickups/st-books.html', log=log)

@app.route('/st-papers')
def papers():
    return render_template('/pickups/st-papers.html')

@app.route('/usb-faucet')
def faucet():
    return render_template('/pickups/usb-faucet.html')


#END

#INVENTORY
@app.route("/inventory")
def show_inventory():
    data = {
        'player_id': session['uid'],
        'id': session['uid']
    }

    
    items = Item.get_items(data)
    player = Player.get_by_id(data)

    return render_template('inventory.html', items=items, player=player)

@app.route("/add-item/<int:item_id>")
def add_to_inventory(item_id):
    data = {
        'player_id': session['uid'],
        'item_id' : item_id
    }

    found_player = Player.get_by_id(data = {'id': session['uid']})

    Item.add_item(data)

    return redirect(f"/{found_player.location}")

@app.route('/show-item/<int:item_id>')
def item_info(item_id):
    data = {
        'item_id': item_id
    }

    item = Item.get_item_by_id(data)
    return render_template("item_info.html", item = item)

#