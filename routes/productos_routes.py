from flask import render_template, request, redirect, url_for, session, Blueprint
from services.auth_service import is_user_authenticated
from services.productos_service import ProductosService

productos_bp = Blueprint('productos', __name__, template_folder='../templates')
productos_service = ProductosService()

def login_required(f):
    """
    Decorador para requerir autenticación
    """
    def decorated_function(*args, **kwargs):
        if not is_user_authenticated(session):
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

@productos_bp.route("/products")
@login_required
def products():
    return redirect(url_for("productos.productos_get"))

# /productos (GET)
@productos_bp.route('/productos', methods=['GET'])
@login_required
def productos_get():
    search_query = request.args.get('search', '').strip()
    
    if search_query:
        productos = productos_service.search_productos_by_name(search_query)
    else:
        productos = productos_service.get_all_productos()
    
    return render_template('products.html', productos=productos)

# /productos/nuevo (GET y POST)
@productos_bp.route('/productos/nuevo', methods=['GET', 'POST'])
@login_required
def productos_nuevo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        activo = 1 if request.form.get('activo') else 0
        categoria = request.form['categoria']
        
        try:
            productos_service.create_producto(nombre, precio, stock, activo, categoria)
            return redirect(url_for('productos.productos_get'))
        except ValueError as e:
            return render_template('product_form.html', modo='nuevo', error=str(e))
    
    # GET - mostrar formulario para nuevo producto
    return render_template('product_form.html', modo='nuevo')

# /productos/<id>/editar (PUT)
@productos_bp.route('/productos/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def productos_editar(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        activo = 1 if request.form.get('activo') else 0
        categoria = request.form['categoria']

        try:
            productos_service.update_producto(id, nombre, precio, stock, activo, categoria)
            return redirect(url_for('productos.productos_get'))
        except ValueError as e:
            producto = productos_service.get_producto_by_id(id)
            return render_template('product_form.html', modo='editar', producto=producto, error=str(e))
    
    # GET - mostrar formulario para editar producto
    producto = productos_service.get_producto_by_id(id)
    return render_template('product_form.html', modo='editar', producto=producto)

# /productos/<id>/eliminar (DELETE)
@productos_bp.route('/productos/<int:id>/eliminar', methods=['POST'])
@login_required
def productos_delete(id):
    productos_service.delete_producto(id)
    return redirect(url_for('productos.productos_get'))