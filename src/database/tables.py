from src.database.connection import connection
from src.database.cursor import cursor

def createTables():
    conn = connection
    try:
        # Init the persons table
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS persons(
                        id INT PRIMARY KEY NOT NULL,
                        name TEXT NOT NULL,
                        birth_date TEXT,
                        type TEXT NOT NULL,
                        sex TEXT,
                        address TEXT,
                        telephone TEXT,
                        email TEXT                  
                    )        
        """)


        # Create a specific table for students
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS students(
                            id INT PRIMARY KEY NOT NULL,
                            FOREIGN KEY (id) REFERENCES persons(id)
                        );
        """)

        # Creates a specific table for teachers
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS teachers(
                        id INT NOT NULL PRIMARY KEY,
                        FOREIGN KEY(id) REFERENCES persons(id)   
                    );
        """)


        # Table for subjects.
        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS subjects(
                        id INT PRIMARY KEY,
                        name TEXT NOT NULL,
                        workload INT,
                        teacher_id INT NOT NULL,
                        FOREIGN KEY(teacher_id) REFERENCES teachers(id)
                    )
        """)

        # Creates a specific table for classes
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS classes(
                        id INT PRIMARY KEY,
                        name TEXT NOT NULL,
                        year INT NOT NULL
                    )
                    """)

        """
            Here is only the intermediary tables because all the relations is N:M (Many-too-Many) 
            We can find the same structure in the table person, because each Person can have a
            different role (like teacher or student) and each role have an table, who the key of
            the relation is the id.
        """

        # Table for Teachers of each Class
        # This ensures that teachers relate with classes using the foreign key
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS classTeachers(
                    class_id varchar(255) NOT NULL,
                    teacher_id varchar(255) NOT NULL,
                    PRIMARY KEY(class_id, teacher_id),
                    FOREIGN KEY (class_id) REFERENCES classes(id),
                    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
                    )
            """)

        # Table for students of each Class
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS classStudents(
                    class_id varchar(255) NOT NULL,
                    student_id varchar(255) NULL,
                    PRIMARY KEY (class_id, student_id),
                    FOREIGN KEY (class_id) REFERENCES classes(id),
                    FOREIGN KEY (student_id) REFERENCES students(id)      
                )
            """)

        print("Tables created")
        conn.commit()
        conn.close()
    except Exception as e :
        print("Error trying to create the database: ", e)

if __name__ == "__main__":
    createTables()