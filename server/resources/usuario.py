from repositories.usuario import RepositoryUsuario
from common.util import Response
from flask_restful import Resource
from flask import make_response
import json
# from common.util import send_response


class UsuarioResource(Resource):
    def __init__(self):
        self._repository = RepositoryUsuario()

    def get(self, nome=None):
        if nome:
            return make_response(self._repository.get_user(nome))
        else:
            return make_response(Response(self._repository.get_all_users()))
