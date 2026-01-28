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

        if usuario == "hola" and password == "mundo":
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
    if "usuario" not in session:
        return redirect(url_for("login"))
    return render_template("products.html")

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route('/')
def home():
    # Renderiza el archivo index.html ubicado en templates/
    return render_template('index.html')

#Crud completo de productos
# /productos (GET)
@app.route('/productos', methods=['GET'])
def productos_get():
    if request.method == 'GET':
        conn = get_db()
        datos = conn.execute('SELECT * FROM productos;').fetchall()
        conn.close()
        return datos
    else:
        return render_template('index.html')

# /productos/nuevo (POST)
@app.route('/productos/nuevo', methods=['POST'])
def productos_post():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        activo = request.form['activo']
        comando = f""" INSERT INTO productos(nombre, precio, stock, activo) 
                        VALUES (?, ?, ?, ?) """
        conn = get_db()
        conn.execute(comando, (nombre, precio, stock, activo))
        conn.commit()
        conn.close()
    else:
        return render_template('index.html')

# /productos/<id>/editar (PUT)
@app.route('/productos/<int:id>/editar', methods=['GET', 'POST'])
def productos_editar(id):
    conn = get_db()
    producto = conn.execute("SELECT * FROM productos WHERE id = ?", (id,)).fetchone()

    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        activo = request.form['activo']

        conn.execute("""
            UPDATE productos
            SET nombre = ?, precio = ?, stock = ?, activo = ?
            WHERE id = ?
        """, (nombre, precio, stock, activo, id))

        conn.commit()
        conn.close()

        return "Producto actualizado"
    conn.close()
    return render_template('form.html', producto=producto, modo="editar")

# /productos/<id>/eliminar (DELETE)
@app.route('/productos/<int:id>/eliminar', methods=['POST'])
def productos_delete(id):
    conn = get_db()
    conn.execute("DELETE FROM productos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return "Producto eliminado "

if __name__ == '__main__':
    app.run(debug=True)

