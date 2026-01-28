from flask import Flask, render_template, request, redirect, url_for, session
from db import get_db, create_database

app = Flask(__name__)
app.secret_key = "clave_secreta_ficticia"

create_database()

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        password = request.form.get("password")

        if usuario == "admin" and password == "admin":
            session["usuario"] = usuario
            return redirect(url_for("products"))
        else:
            return render_template("login.html", error="Credenciales incorrectas")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/products")
def products():
    return redirect(url_for("productos_get"))

@app.route("/")
def index():
    return redirect(url_for("login"))

#Crud completo de productos
# /productos (GET)
@app.route('/productos', methods=['GET'])
def productos_get():
    if "usuario" not in session:
        return redirect(url_for("login"))
    
    conn = get_db()
    datos = conn.execute('SELECT * FROM productos;').fetchall()
    conn.close()
    return render_template('products.html', productos=datos)

# /productos/nuevo (GET y POST)
@app.route('/productos/nuevo', methods=['GET', 'POST'])
def productos_nuevo():
    if "usuario" not in session:
        return redirect(url_for("login"))
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        activo = 1 if request.form.get('activo') else 0
        
        comando = """ INSERT INTO productos(nombre, precio, stock, activo) 
                        VALUES (?, ?, ?, ?) """
        conn = get_db()
        conn.execute(comando, (nombre, precio, stock, activo))
        conn.commit()
        conn.close()
        
        return redirect(url_for('productos_get'))
    
    # GET - mostrar formulario para nuevo producto
    return render_template('product_form.html', modo='nuevo')

# /productos/<id>/editar (PUT)
@app.route('/productos/<int:id>/editar', methods=['GET', 'POST'])
def productos_editar(id):
    if "usuario" not in session:
        return redirect(url_for("login"))
    
    conn = get_db()
    producto = conn.execute("SELECT * FROM productos WHERE id = ?", (id,)).fetchone()

    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        activo = 1 if request.form.get('activo') else 0

        conn.execute("""
            UPDATE productos
            SET nombre = ?, precio = ?, stock = ?, activo = ?
            WHERE id = ?
        """, (nombre, precio, stock, activo, id))

        conn.commit()
        conn.close()

        return redirect(url_for('productos_get'))
    
    # GET - mostrar formulario para editar producto
    return render_template('product_form.html', modo='editar', producto=producto)

# /productos/<id>/eliminar (DELETE)
@app.route('/productos/<int:id>/eliminar', methods=['POST'])
def productos_delete(id):
    if "usuario" not in session:
        return redirect(url_for("login"))
    
    conn = get_db()
    conn.execute("DELETE FROM productos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    
    return redirect(url_for('productos_get'))

if __name__ == '__main__':
    app.run(debug=True)

