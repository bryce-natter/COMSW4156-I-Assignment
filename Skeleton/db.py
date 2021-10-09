import sqlite3
from sqlite3 import Error

'''
Initializes the Table GAME
Do not modify
'''


def init_db():
    # creates Table
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        conn.execute('DROP TABLE IF EXISTS GAME')
        conn.execute('CREATE TABLE GAME(current_turn TEXT, board TEXT,' +
                     'winner TEXT, player1 TEXT, player2 TEXT' +
                     ', remaining_moves INT)')
        print('Database Online, table created')
    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()


'''
move is a tuple (current_turn, board, winner, player1, player2,
remaining_moves)
Insert Tuple into table
'''


def add_move(move):  # will take in a tuple
    
    conn = None
    print(move)
    try:
        conn = sqlite3.connect('sqlite_db')
        cur = conn.cursor()
        cmd = ('INSERT INTO GAME(' +
                     'current_turn, board, winner, player1, player2, remaining_moves)' +
                     '\n\t VALUES(' + str(move) + ')' )
        print(cmd)
        cur.execute('INSERT INTO GAME(' +
                     'current_turn, board, winner, player1, player2, remaining_moves)' +
                     ' VALUES(' + str(move) + ')')
        conn.commit
        print('Move saved')
    except Error as e:
        print(e)



'''
Get the last move played
return (current_turn, board, winner, player1, player2, remaining_moves)
'''


def getMove():
    # will return tuple(current_turn, board, winner, player1, player2,
    # remaining_moves) or None if db fails
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM GAME ORDER BY remaining_moves DESC LIMIT 1')
        print('Move saved')
        return cur.fetchall()
    except Error as e:
        print(e)
        return False


'''
Clears the Table GAME
Do not modify
'''


def clear():
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        conn.execute("DROP TABLE GAME")
        print('Database Cleared')
    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()
