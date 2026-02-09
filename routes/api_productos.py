from flask import render_template, request, redirect, url_for, Blueprint, jsonify
from services.productos_service import ProductosService

api_productos = Blueprint('api_productos', __name__, template_folder='../templates', url_prefix='/api')
productos_service = ProductosService()


# /productos (GET y POST)
@api_productos.route('/productos/', methods=['GET', 'POST'])
def productos():
    if request.method == 'GET':

        search_query = request.args.get('search', '').strip()
    
        if search_query:
            productos = productos_service.search_productos_by_name(search_query)
        else:
            productos = productos_service.get_all_productos()
        
        if not productos:
            #Error not found
            return jsonify({'productos': productos, 'status':'Vacio'}), 404
        
        return jsonify({'productos': productos, 'status':'Correcto'}), 200
    
    if request.method == 'POST':
        data = request.get_json()
        
        try:
            nombre = data['nombre']
            precio = data['precio']
            stock = data['stock']
            activo = data['activo']
            categoria = data['categoria']

        except:

            return jsonify({'status':'Revisa el body del json'}), 400

        try:
            productos_service.create_producto(nombre, precio, stock, activo, categoria)
            return jsonify({'status':'Creado con exito'}), 201
        except Exception as e:
            return jsonify({'status': str(e)}), 400

# /productos (GET y POST)
@api_productos.route('/productos/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def productos_id(id):
    if request.method == 'GET':
        producto = productos_service.get_producto_by_id(id)
        if producto:
            return jsonify({'producto': producto, 'status':'Encontrado.'}), 200
        else:
            return jsonify({'status':'No encontrado.'}), 404

    if request.method == 'PUT':
        data = request.get_json()
        try:
            nombre = data['nombre']
            precio = data['precio']
            stock = data['stock']
            activo = data['activo']
            categoria = data['categoria']

        except:
            return jsonify({'status':'Revisa el body del json'}), 400

        try:
            productos_service.update_producto(id, nombre, precio, stock, activo, categoria)
            return jsonify({'status':'Actualizado con exito'}), 200
        except Exception as e:
            return jsonify({'status': str(e)}), 400
    
    if request.method == 'DELETE':
        try:
            productos_service.delete_producto(id)
            return jsonify({'status':'Producto eliminado'}), 200
        except Exception as e:
            return jsonify({'status': str(e)}), 404
