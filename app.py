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

if __name__ == '__main__':
    app.run(debug=True)
# Login (GET/POST) redirigir a login si no funciona

# Logout

#Crud completo de productos
# /productos (GET)

# /productos/nuevo (POST)

# /productos/<id>/editar (POST)

# /productos/<id>/eliminar (DELETE)


if __name__ == '__main__':
    app.run(debug=True)
