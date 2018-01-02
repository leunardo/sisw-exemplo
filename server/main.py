"""Arquivo principal do servidor."""

from flask import Flask
from flask_restful import Api

# importa nossos recursos
from resources.hello_world import HelloWorld
from resources.hour import Hour

app = Flask(__name__)
api = Api(app)

# adicionamos os recursos para as rotas /hello e /hello/<string>
api.add_resource(HelloWorld, '/hello', '/hello/<string:nome>')
api.add_resource(Hour, '/hour')

if __name__ == '__main__':
    # desativar debug em produção
    app.run(debug=True)
