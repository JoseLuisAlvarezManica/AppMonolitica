from db import get_db

class ProductosRepository:
    
    def find_all(self):
        with get_db() as conn:
            return conn.execute(
                'SELECT * FROM productos ORDER BY id DESC'
            ).fetchall()
    
    def find_by_name(self, nombre):
        with get_db() as conn:
            return conn.execute(
                'SELECT * FROM productos WHERE nombre LIKE ? ORDER BY id DESC',
                (f'%{nombre}%',)
            ).fetchall()
    
    def find_by_id(self, id):
        with get_db() as conn:
            return conn.execute(
                "SELECT * FROM productos WHERE id = ?", (id,)
            ).fetchone()
    
    def insert(self, nombre, precio, stock, activo, categoria):
        with get_db() as conn:
            conn.execute(
                """
                INSERT INTO productos(nombre, precio, stock, activo, categoria) 
                        VALUES (?, ?, ?, ?, ?)
                """, (nombre, precio, stock, activo, categoria)
            )
            conn.commit()
    
    def modify(self, nombre, precio, stock, activo, categoria, id):
        with get_db() as conn:
            conn.execute("""
                UPDATE productos
                SET nombre = ?, precio = ?, stock = ?, activo = ?, categoria = ?
                WHERE id = ?
                """, (nombre, precio, stock, activo, categoria, id))
            conn.commit()
    
    def delete(self, id):
        with get_db() as conn:
            conn.execute("DELETE FROM productos WHERE id = ?", (id,))
            conn.commit()