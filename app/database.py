import sqlite3


DB_NAME = "projects.db"


def create_database():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects
    (
        id INTEGER PRIMARY KEY,
        name TEXT,
        python_code TEXT
    )
    """)

    conn.commit()

    conn.close()



def save_project(name, code):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO projects
        (name, python_code)
        VALUES (?,?)
        """,
        (name, code)
    )

    conn.commit()

    conn.close()