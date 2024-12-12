from connection import connect
# Create one cursor.
def cursor():
    conn = connect()
    cursor = conn.cursor()
    return cursor
