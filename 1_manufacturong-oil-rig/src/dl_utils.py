import os
import sqlite3
from src.sql_queries import dl_drop_table_queries, dl_create_table_queries


def dl_connect(target_directory):
    '''
    Open a connection to the sensor_data database and return con and cur objects.
    '''
    try:
        os.chdir(target_directory)
    except FileNotFoundError:
        os.mkdir(target_directory)
        os.chdir(target_directory)
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


def dl_create_tables(target_directory):
    '''
    Create database if not exists in the target directory
    '''
    current_directory = os.getcwd()
    
    con, cur = dl_connect(target_directory)
    
    for query in dl_create_table_queries:
        cur.execute(query)
        
    dl_close(con, cur)
    
    os.chdir(current_directory)