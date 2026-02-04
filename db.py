import sqlite3

SQUEMA_SQL = '''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL CHECK (precio >= 0),
        stock INTEGER CHECK (stock >= 0),
        activo INTEGER DEFAULT 0
    ); '''

ALTER_TABLE = """
    ALTER TABLE productos ADD categoria TEXT DEFAULT miscelanio;
"""

def get_db():
    conn = sqlite3.connect('productos.db')
    return conn

def create_database():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(SQUEMA_SQL)
    #Migración 1 agregar categoria a la tabla de productos
    try:
        cursor.execute(ALTER_TABLE)
    except:
        print('Categoria already exists.')
    conn.commit()
    conn.close()

