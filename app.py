from flask import Flask, render_template
from db import get_db, create_database


app = Flask(__name__)

create_database()

@app.route('/')
def home():
    # Renderiza el archivo index.html ubicado en templates/
    return render_template('index.html')

# Login (GET/POST) redirigir a login si no funciona

# Logout

#Crud completo de productos
# /productos (GET)

# /productos/nuevo (POST)

# /productos/<id>/editar (POST)

# /productos/<id>/eliminar (DELETE)


if __name__ == '__main__':
    app.run(debug=True)