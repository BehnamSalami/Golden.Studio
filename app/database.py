import sqlite3
import os
from kivy.app import App


def get_db_path():
    try:
        # روی اندروید از پوشه خصوصی برنامه استفاده می‌کند
        return os.path.join(App.get_running_app().user_data_dir, "projects.db")
    except Exception:
        return "projects.db"


DB_PATH = get_db_path()


def connection():
    return sqlite3.connect(DB_PATH)



def create_database():

    conn = connection()
    cur = conn.cursor()


    cur.execute("""
    CREATE TABLE IF NOT EXISTS projects
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        python_code TEXT,
        financial_data TEXT,
        result TEXT
    )
    """)


    conn.commit()
    conn.close()



def create_project(name, python_code):

    conn = connection()
    cur = conn.cursor()


    cur.execute(
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

    conn = connection()
    cur = conn.cursor()


    cur.execute(
        """
        SELECT id,name
        FROM projects
        ORDER BY id DESC
        """
    )


    data = cur.fetchall()

    conn.close()

    return data



def get_project(project_id):

    conn = connection()
    cur = conn.cursor()


    cur.execute(
        """
        SELECT *
        FROM projects
        WHERE id=?
        """,
        (project_id,)
    )


    data = cur.fetchone()

    conn.close()

    return data



def save_financial(project_id,data,result):

    conn = connection()
    cur = conn.cursor()


    cur.execute(
        """
        UPDATE projects
        SET financial_data=?,
        result=?
        WHERE id=?
        """,
        (
        data,
        result,
        project_id
        )
    )


    conn.commit()
    conn.close()