import os
import sqlite3
from sql_queries import dl_drop_table_queries, dl_create_table_queries


def dl_connect():
    '''
    Open a connection to the sensor_data database and return con and cur objects.
    '''
    con = sqlite3.connect("sensor_data.db")
    cur = con.cursor()
    
    return con, cur


def dl_close(con, cur):
    '''
    Close input con and cur objects.
    '''
    try:
        cur.close()
        con.close()
    except ProgrammingError:
        print("Database connection is already closed")


def dl_create_tables():
    con, cur = dl_connect()
    
    for query in dl_create_table_queries:
        cur.execute(query)
        
    dl_close(con, cur)