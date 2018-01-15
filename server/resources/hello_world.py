"""Esse recurso é um exemplo de requisição para um servidor"""

from flask_restful import Resource
from common.util import make_response


class HelloWorld(Resource):
    # Adicionar aqui os outros verbos
    # ex: put, post, delete etc
    
    def get(self, nome="World"):
        texto = "Hello, %s" % nome
        return make_response(texto)
