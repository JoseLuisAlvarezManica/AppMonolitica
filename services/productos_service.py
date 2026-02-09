from repositories.productos_repository import ProductosRepository

class ProductosService:
    def __init__(self):
        self.repository = ProductosRepository()
    
    def get_all_productos(self):
        return self.repository.find_all()
    
    def search_productos_by_name(self, nombre):
        """
        Busca productos por nombre
        """
        if not nombre:
            return self.get_all_productos()
        return self.repository.find_by_name(nombre)
    
    def create_producto(self, nombre, precio, stock, activo, categoria):
        # Validar nombre (TEXT NOT NULL)
        if not nombre or not isinstance(nombre, str):
            raise ValueError("Nombre es requerido y debe ser texto")
        
        # Validar y convertir precio (REAL CHECK precio >= 0)
        try:
            precio = float(precio)
            if precio < 0:
                raise ValueError("Precio debe ser un número mayor o igual a 0")
        except (ValueError, TypeError):
            raise ValueError("Precio debe ser un número válido")
        
        # Validar y convertir stock (INTEGER CHECK stock >= 0)
        try:
            stock = int(stock)
            if stock < 0:
                raise ValueError("Stock debe ser un entero mayor o igual a 0")
        except (ValueError, TypeError):
            raise ValueError("Stock debe ser un número entero válido")
        
        # Validar y convertir activo (INTEGER DEFAULT 0)
        if isinstance(activo, str):
            activo = 1  # checkbox marcado
        elif activo is None:
            activo = 0  # checkbox no marcado
        else:
            activo = int(activo) if activo else 0
        
        # Validar categoria (TEXT)
        if categoria and not isinstance(categoria, str):
            raise ValueError("Categoria debe ser texto")
        
        return self.repository.insert(nombre, precio, stock, activo, categoria)
    
    def get_producto_by_id(self, id):
        return self.repository.find_by_id(id)
    
    def update_producto(self, id, nombre, precio, stock, activo, categoria):
        
        producto = self.get_producto_by_id(id)

        if not producto:
            raise ValueError("No existe un producto relacionado a esa id.")
        
        # Validar nombre (TEXT NOT NULL)
        if not nombre or not isinstance(nombre, str):
            raise ValueError("Nombre es requerido y debe ser texto")
        
        # Validar y convertir precio (REAL CHECK precio >= 0)
        try:
            precio = float(precio)
            if precio < 0:
                raise ValueError("Precio debe ser un número mayor o igual a 0")
        except (ValueError, TypeError):
            raise ValueError("Precio debe ser un número válido")
        
        # Validar y convertir stock (INTEGER CHECK stock >= 0)
        try:
            stock = int(stock)
            if stock < 0:
                raise ValueError("Stock debe ser un entero mayor o igual a 0")
        except (ValueError, TypeError):
            raise ValueError("Stock debe ser un número entero válido")
        
        # Validar y convertir activo (INTEGER DEFAULT 0)
        if isinstance(activo, str):
            activo = 1  # checkbox marcado
        elif activo is None:
            activo = 0  # checkbox no marcado
        else:
            activo = int(activo) if activo else 0
        
        # Validar categoria (TEXT)
        if categoria and not isinstance(categoria, str):
            raise ValueError("Categoria debe ser texto")
        
        return self.repository.modify(nombre, precio, stock, activo, categoria, id)
    
    def delete_producto(self, id):
        producto = self.get_producto_by_id(id)
                
        if not producto:
            raise ValueError("No existe un producto relacionado a esa id.")

        return self.repository.delete(id)