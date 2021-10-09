from flask import Flask, render_template, request, redirect, jsonify
from json import dump
from Gameboard import Gameboard
import db


app = Flask(__name__)

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

game = None

'''
Implement '/' endpoint
Method Type: GET
return: template player1_connect.html and status = "Pick a Color."
Initial Webpage where gameboard is initialized
'''


@app.route('/', methods=['GET'])
def player1_connect():
    global game
    game = Gameboard()
    db.init_db()
    return render_template("player1_connect.html", status = 'Pick a Color.')


'''
Helper function that sends to all boards don't modify
'''


@app.route('/autoUpdate', methods=['GET'])
def updateAllBoards():
    try:
        return jsonify(move=game.board, winner=game.game_result,
                       color=game.player1)
    except Exception:
        return jsonify(move="")


'''
Implement '/p1Color' endpoint
Method Type: GET
return: template player1_connect.html and status = <Color picked>
Assign player1 their color
'''


@app.route('/p1Color', methods=['GET'])
def player1_config():
    save = db.getMove()
    if(save):
        game.current_turn       = save[0]
        game.winner             = save[2]
        game.player1            = save[3]
        game.player2            = save[4]
        game.remaining_moves    = save[5]
        for row, srow in zip(game.gameboard, save[1].splitlines()):
            row = srow.split(' ')
    else:
        if(request.args.get('color') == 'red'):
            game.player1 = "red"
            game.player2 = "yellow"
        elif(request.args.get('color') == 'yellow'):
            game.player1 = "yellow"
            game.player2 = "red"


    return render_template("player1_connect.html", status = game.player1)



'''
Implement '/p2Join' endpoint
Method Type: GET
return: template p2Join.html and status = <Color picked> or Error
if P1 didn't pick color first

Assign player2 their color  
'''


@app.route('/p2Join', methods=['GET'])
def p2Join():
    save = db.getMove()
    if (save):
        game.current_turn       = save[0]
        game.winner             = save[2]
        game.player1            = save[3]
        game.player2            = save[4]
        game.remaining_moves    = save[5]
        for row, srow in zip(game.gameboard, save[1].splitlines()):
            row = srow.split(' ')
    else:
        if(game.player1 == "red"):
            game.player2 = "yellow"
        elif(game.player1 == "yellow"):
            game.player2 = "red"
        else:
            return "Error"

    return render_template("p2Join.html", status = game.player2)

'''
Implement '/move1' endpoint
Method Type: POST
return: jsonify (move=<CurrentBoard>,
invalid=True or False, winner = <currWinner>)
If move is valid --> invalid = False else invalid = True
If invalid == True, also return reason= <Why Move is Invalid>

Process Player 1's move
'''


@app.route('/move1', methods=['POST'])
def p1_move():
    col = int(request.json['column'][3]) - 1
    ret = game.validate_move('p1', col)

    if (ret == "Valid"):
        game.add_chip(game.player1, col)
        move = (game.current_turn, '\n'.join(' '.join(map(str,row)) for row in game.board),
                game.game_result, game.player1, game.player2, game.remaining_moves)
        db.add_move(move)
        return jsonify(move=game.board, invalid=False, winner=game.game_result)
    else:
        return jsonify(move=game.board, invalid=True, reason=ret, winner=game.game_result)

'''
Same as '/move1' but instead proccess Player 2
'''


@app.route('/move2', methods=['POST'])
def p2_move():
    col = int(request.json['column'][3]) - 1
    ret = game.validate_move('p2', col)

    if (ret == "Valid"):
        game.add_chip(game.player2, col)
        move = (game.current_turn, '\n'.join(' '.join(map(str,row)) for row in game.board),
                game.game_result, game.player1, game.player2, game.remaining_moves)
        db.add_move(move)
        return jsonify(move=game.board, invalid=False, winner=game.game_result)
    else:
        return jsonify(move=game.board, invalid=True, reason=ret, winner=game.game_result)
        



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
