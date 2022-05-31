import sqlite3

conn = sqlite3.connect("data.sqlite")


def createGame(data):
    query = """insert into game(name,character_type,default_name,over18) values (?,?,?,?)"""
    print(data)
    cursor = conn.cursor()
    cursor.execute(query,data)
    conn.commit()