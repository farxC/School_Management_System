import sqlite3


# Create/Connect to DB
def connect():
    conn = sqlite3.connect('school_sys.sql')
    return conn



