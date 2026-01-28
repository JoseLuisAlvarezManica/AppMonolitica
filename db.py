import sqlite3

SQUEMA_SQL = '''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL CHECK (precio >= 0),
        stock INTEGER CHECK (stock >= 0),
        activo INTEGER DEFAULT 0
    ); '''

def get_db():
    conn = sqlite3.connect('productos.db')
    return conn

def create_database():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(SQUEMA_SQL)
    conn.commit()
    conn.close()

