# Flask API RESTful CRUD
 
 Este es un proyecto que consiste en una aplicación CRUD usando Flask, SQLAlchemy y MySQL.
 
 ## Requisitos
 
 - Python 3
 - MySQL
 
 ## Configuración del entorno
 
 ### 1. Crear un entorno virtual
 
 #### En Linux / macOS:
 ```sh
 python3 -m venv <nombre_del_entorno>
 ```
 
 #### En Windows:
 ```sh
 python -m venv <nombre_del_entorno>
 ```
 
 ### 2. Activar el entorno virtual
 
 #### En Linux / macOS:
 ```sh
 source <nombre_del_entorno>/bin/activate
 ```
 
 #### En Windows:
 ```sh
 <nombre_del_entorno>\Scripts\activate
 ```
 
 ### 3. Instalar dependencias
 
 ```sh
 pip install Flask Flask-SQLAlchemy PyMySQL python-dotenv
 ```
 
 ## Configuración de la base de datos
 
 Antes de ejecutar la aplicación, debes configurar las siguientes variables de entorno:
 
 ```sh
 MYSQL_USER=<tu_usuario>
 MYSQL_PASSWORD=<tu_contraseña>
 MYSQL_DATABASE=<nombre_de_la_base_de_datos>
 MYSQL_HOST=<host_de_mysql>
 ```
 
 ## Instalación y ejecución
 
 1. Clona el repositorio:
 ```sh
 git clone <url_del_repositorio>
 ```
 
 2. Accede al directorio del proyecto:
 ```sh
 cd <nombre_del_proyecto>
 ```
 
 3. Instala las dependencias desde el archivo `requirements.txt`:
 ```sh
 pip install -r requirements.txt
 ```
 
 4. Ejecuta la aplicación:
 ```sh
 python app.py
 ```
paradigmas de programación: distintos estilos que se utilizan en programación para resolver un problema
poo: abstracción del mundo real
secuencial:de arriba hacia abajo de izquiersa a derecha
reactiva:react

framework: define la estructura y el flujo general de la aplicación., mientras que una librería proporciona funciones  o clases específicas.
dotenv utilizar las variables  para conectar la base de datos con .env
ORM: se comunica la base    para evitar la inyeccion de sql
pamysql para que entienda mi aplicacion 
levanto el servidor app.py
arquitectura modelo cliente y servidor sirve para ordenar el codigo
 del modelo al controlador y el controlador(routes) ala base de datos
 las rutas son el intermediario entre el modelo y la base de datos
 jinja es un motor de plantillas permite que pyhton en ccs y html
 appi un protocolo de comunicacion entre distintas aplicaciones a traves de los métodos get put pat delete 