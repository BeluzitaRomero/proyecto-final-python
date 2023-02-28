# 3ra pre-entrega python

## Pasos para clonar y levantar el proyecto

Creamos una carpeta donde haremos la clonacion del proyecto
- Enviaremos el comando: `git clone + url del proyecto`
- Nos moveremos dentro de la carpeta de proyecto con el comando: `cd nombre`
- Instalaremos el entorno virtual mediante: `pip install virtualenv`
- Luego crearemos nuestro entorno virtual: `virtualenv venv`
- Lo activaremos con el comando: `venv\Scripts\activate`

- Luego instalaremos todas las dependencias mediante: `pip install -r requirements.txt`
- Instalamos django: `pip install django`
- Hacemos las migraciones necesarias: `py manage.py migrate`
- Levantamos el proyecto con: `py manage.py runserver`

## Para insertar registros en la base de datos

Cada modelo tiene una template con su formulario para crear un nuevo registro.
Esto se puede acceder desde la barra de navegacion, seleccionando "usuario", "post" o "comentario" donde se encontrara un boton para cargar nuevos registros.
En esta mismo template encontramos el buscador de registros, una vez que ya hay alguno insertado en la db.

### ATENCIÓN 🚨
⚠ Para insertar un registro de "post" tener en cuenta que la imagen debe ser guardada como url.👈

El link "general" de la barra de navegacion, trae todos los post realizados.

Tambien accediendo a "/all-users" y "/all-comments" se pueden ver el listado de registros guardados en dichas tablas.



