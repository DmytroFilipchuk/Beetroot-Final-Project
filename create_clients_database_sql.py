import sqlite3

def make_query(connection,query):
    cur = connection.cursor()
    cur.execute(query)
    connection.commit()

connection = sqlite3.connect("FFeelMusicClients.db")
make_query(connection,

"""
    CREATE TABLE IF NOT EXISTS Clients (   
    
    Id INTEGER PRIMARY KEY,
    first_name TEXT,
    username TEXT,
    phone_number Text )
    """)

