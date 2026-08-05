import sqlite3
import os


DB_NAME = "projects.db"


def get_connection():

    return sqlite3.connect(DB_NAME)



def create_database():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS projects
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            python_code TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )


    conn.commit()

    conn.close()



def save_project(name, python_code):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO projects
        (
            name,
            python_code
        )
        VALUES (?,?)
        """,
        (
            name,
            python_code
        )
    )


    conn.commit()

    conn.close()



def get_projects():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT id, name, python_code
        FROM projects
        ORDER BY id DESC
        """
    )


    data = cursor.fetchall()


    conn.close()


    return data