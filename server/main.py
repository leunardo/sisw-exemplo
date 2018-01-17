"""Arquivo principal do servidor."""

from flask import Flask
from flask_restful import Api
from flask_cors import CORS

# importa nossos recursos
from resources.hello_world import HelloWorld
from resources.hour import Hour
from resources.usuario import UsuarioResource

app = Flask(__name__)
CORS(app)
api = Api(app)
# adicionamos os recursos para as rotas /hello e /hello/<string>
api.add_resource(HelloWorld, '/hello', '/hello/<string:nome>')
api.add_resource(Hour, '/hour')
api.add_resource(UsuarioResource, '/user', '/user/<int:id_usuario>')

if __name__ == '__main__':
    # desativar debug em produção
    app.run(debug=True, threaded=True)
