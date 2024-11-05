import sqlite3

# Conexión a la base de datos SQLite
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Facilita el acceso a las columnas por nombre
    return conn

# Crear la tabla si no existe
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS candidatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dni TEXT NOT NULL,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
