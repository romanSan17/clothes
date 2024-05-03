from sqlite3 import *
from sqlite3 import Error
from os import *

def create_connect(path:str):
    connection=None
    try:
        connection=connect(path)
        print("Ühendus on olemas!")
    except Error as e:
        print(f"Tekkis viga: {e}")
    return connection
def execute_query(connection,query):
    try:
        cursor=connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabel on loodud või andmed on sisestatud")
    except Error as e:
        print(f"Tekkis viga: {e}")
def execute_read_query(connection,query):
    cursor=connection.cursor()
    result=None
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        return result
    except Error as e:
        print(f"Tekkis viga: {e}")

def tooted_query(connection,data):
    query = "INSERT INTO tooted(toote_id,toote_nimi,hind,kategooria_id,brändi_id) VALUES(?,?,?,?,?)"
    cursor = connection.cursor()
    cursor.execute(query, data)
    connection.commit()

def kategooriad_query(connection,data):
    query = "INSERT INTO kategooriad(kategooria_id,kategooria_nimi) VALUES(?,?)"
    cursor = connection.cursor()
    cursor.execute(query, data)
    connection.commit()

def brandid_query(connection,data):
    query = "INSERT INTO brandid(brandi_id,brandi_nimi) VALUES(?,?)"
    cursor = connection.cursor()
    cursor.execute(query, data)
    connection.commit()

create_tooted_table = """
CREATE TABLE IF NOT EXISTS tooted(
toote_id INTEGER PRIMARY KEY AUTOINCREMENT,
toote_nimi TEXT NOT NULL,
hind INTEGER NOT NULL,
kategooria_id INTEGER,
brandi_id INTEGER,
FOREIGN KEY (kategooria_id) REFERENCES kategooriad(kategooria_id),
FOREIGN KEY (brandi_id) REFERENCES brandid(brandi_id)
)
"""

create_kategooriad_table = """
CREATE TABLE IF NOT EXISTS kategooriad(
kategooria_id INTEGER PRIMARY KEY AUTOINCREMENT,
kategooria_nimi TEXT NOT NULL
)
"""

create_brandid_table = """
CREATE TABLE IF NOT EXISTS brandid(
brandi_id INTEGER PRIMARY KEY AUTOINCREMENT,
brandi_nimi TEXT NOT NULL
)
"""

insert_tooted = """
INSERT INTO
tooted(toote_nimi, hind, kategooria_id, brandi_id)
VALUES
("t-särk", 20, 1, 1),
("tossud", 100, 2, 2)
"""

insert_kategooriad = """
INSERT INTO
kategooriad(kategooria_nimi)
VALUES
("t-särgid"),
("kingad")
"""

insert_brandid = """
INSERT INTO
brandid(brandi_nimi)
VALUES
("adidas"),
("nike")
"""


filename = path.abspath(__file__)
dbdir = filename.rstrip('clothes.py')
dbpath = path.join(dbdir,"data.db")
conn = create_connect(dbpath)

execute_query(conn, create_brandid_table) 
execute_query(conn, create_kategooriad_table) 
execute_query(conn, create_tooted_table) 
execute_query(conn, insert_brandid) 
execute_query(conn, insert_kategooriad) 
execute_query(conn, insert_tooted) 