# App web monolítica en Flask

## Integrantes del Equipo
José Luis Álvarez Mánica  
Marco Uriel Castaneda Avila  
Fernando Agustin Hernández Rivas  

## Fecha de realización: 
28 de enero del 2026

## Descripción
Este proyecto es una aplicación monolitica la cual integra una base de datos de productos, una pagina web sencilla (login simulado e una interfaz para realizar un CRUD hacia los productos) asi como una api en Flask para comunicar estos dos elementos y coordinar la pagina. Este diseño no es adecuado para uso en una pagina web comercial o personal, es parte de una actividad donde se establecieron decisiones de diseño consideradas como malas practicas con fines educativos.

## Estructura del Proyecto
```
AppMonolitica/
├── app.py              # Aplicación Flask principal
├── db.py              # Configuración de base de datos
├── requirements.txt    # Dependencias
├── templates/         # Plantillas HTML
│   ├── login.html
│   ├── products.html
│   └── product_form.html
└── static/css/        # Archivos CSS
    ├── login.css
    └── products.css
```

## Instalación

### 1. Clonar el proyecto
```bash
git clone <URL_DEL_REPOSITORIO>
cd AppMonolitica
```

### 2. Crear entorno virtual
```bash
# Crear entorno virtual
python -m venv venv

# Activar (Windows)
venv\Scripts\activate

# Activar (Linux/Mac)
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar
```bash
python app.py
```

**Acceder a:** http://localhost:5000  
**Credenciales:** usuario: `admin`, contraseña: `admin`

## Preguntas
¿Qué quedó más acoplado en el monolito?  
- La API es lo que quedó más acoplado, ya que esta tiene que orquestar la página web y su renderizado, la autorización, la lógica del negocio y la comunicación con la base de datos. 

¿Qué separarías primero si lo migraras a API/microservicio?  
- Separaríamos primero la autorización y el CRUD de productos como su propio componente API REST, permitiendo poder trabajar de manera independiente el frontend del backend. Así como permitiendo el desarrollo de otros productos que consuman de esta API.

¿Qué problemas surgen si dos equipos trabajan en paralelo en el mismo monolito?  

- Es más difícil de coordinar, ya que, como los componentes no son independientes el uno del otro, lo que realice un equipo puede acabar afectando el desarrollo del otro, trayendo conflictos de código, posibles conflictos en la estructura de datos entre equipos, la necesidad de implementar maneras ineficientes de trabajo (por ejemplo, esperar a que el primer equipo acabe para realizar cambios), entre otros. Problemas que son reducidos o eliminados cuando los componentes son independientes y existe una clara estructura a ocupar (ejemplo: endpoints bien definidos con estructuras de datos que no van a cambiar).