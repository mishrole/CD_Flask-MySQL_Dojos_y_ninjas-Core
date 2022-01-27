from dojo_app import app
# Importante importar para cargar las rutas
from dojo_app.controllers import dojosController, ninjasController

if __name__ == '__main__':
    app.run( debug = True, port = 8091 )