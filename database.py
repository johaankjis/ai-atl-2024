import sqlite3

def get_db_connection():
    conn = sqlite3.connect('resume_matcher.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS job_descriptions (id INTEGER PRIMARY KEY, description TEXT)')
    conn.close()

def get_job_descriptions():
    conn = get_db_connection()
    job_descriptions = conn.execute('SELECT * FROM job_descriptions').fetchall()
    conn.close()
    return job_descriptions

def add_job_description(description):
    conn = get_db_connection()
    conn.execute('INSERT INTO job_descriptions (description) VALUES (?)', (description,))
    conn.commit()
    conn.close()

# Initialize the database
init_db()

