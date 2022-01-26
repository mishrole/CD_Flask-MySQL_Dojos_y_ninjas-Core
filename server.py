from dojo_app import app
# Importante importar para cargar las rutas
from dojo_app.controllers import dojosController
from dojo_app.controllers import ninjasController

if __name__ == '__main__':
    app.run( debug = True )