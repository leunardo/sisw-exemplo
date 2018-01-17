from repositories.usuario import RepositoryUsuario
from common.util import make_response
from flask_restful import Resource, reqparse


class UsuarioResource(Resource):
    def __init__(self):
        self._parser = reqparse.RequestParser()
        self._parser.add_argument('nome', type=str)
        self._parser.add_argument('id_usuario', type=int)
        self._repository = RepositoryUsuario()

    def get(self, id_usuario=None):

        if id_usuario:
            return make_response(self._repository.get_user(id_usuario))
        else:
            return make_response(self._repository.get_all_users())

    def post(self):
        try:
            res = make_response(self._repository.add_user(self._parser.parse_args()), status=201)
            return res
        except Exception as e:
            return make_response(str(e), status=500)

    def put(self, id_usuario=None):
        if not id_usuario:
            return make_response("Missing id", status=403)

        try:
            res = make_response(self._repository.alter_user(self._parser.parse_args(), id_usuario), status=204)
            return res
        except Exception as e:
            return make_response(str(e), status=500)

    def delete(self, id_usuario=None):
        if not id_usuario:
            return make_response("You need to specify an id.", status=405)

        try:
            res = make_response(self._repository.delete_user(id_usuario), status=204)
            return res
        except Exception as e:
            return make_response(str(e), status=500)
