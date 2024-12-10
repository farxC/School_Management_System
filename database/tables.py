from db_connection import cursor
from db_connection import connection

# Init the persons table
cursor.execute("""
               CREATE TABLE IF NOT EXISTS persons(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   birth_date TEXT,
                   type TEXT NOT NULL,
                   sex TEXT,
                   address TEXT,
                   telephone INTEGER,
                   email TEXT                  
               )        
""")


# Table for discipline.
cursor.execute("""
                CREATE TABLE IF NOT EXISTS discipline(
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   teacher TEXT NOT NULL,
                   workload INTEGER
               )
""")


# Create a specific table for students
cursor.execute("""
               CREATE TABLE IF NOT EXISTS students(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   person_id INTEGER NOT NULL,
                   FOREIGN KEY(person_id) REFERENCES person (id),
                   grade TEXT
                )
""")

# Creates a specific table for teachers
cursor.execute("""
               CREATE TABLE IF NOT EXISTS tearchers(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   person_id INTEGER NOT NULL,
                   FOREIGN KEY (person_id) REFENCES person (id)
                   subject TEXT,
               )
""")

# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS grade(
#                 code INTEGER PRIMARY KEY,
#                 name TEXT NOT NULL,
#                 students 
#                )
#                """)

connection.commit()
connection.close()
