from flask import render_template, request, redirect, url_for, session, Blueprint
from services.auth_service import authenticate_user, logout_user

auth_bp = Blueprint('auth', __name__, template_folder='../templates')

@auth_bp.route('/')
def index():
    return redirect(url_for('auth.login'))

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        password = request.form.get("password")

        if authenticate_user(usuario, password):
            session["usuario"] = usuario
            return redirect(url_for("productos.productos_get"))
        else:
            return render_template("login.html", error="Credenciales incorrectas")

    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    logout_user(session)
    return redirect(url_for("auth.login"))