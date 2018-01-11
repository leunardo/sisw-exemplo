from repositories.usuario import RepositoryUsuario
from flask_restful import Resource
from common.util import send_response


class UsuarioResource(Resource):

    def __init__(self):
        self._repository = RepositoryUsuario()

    def get(self, nome=None):
        if nome:
            return send_response(self._repository.getUser(nome))
        else:
            return send_response(self._repository.getAllUsers())
