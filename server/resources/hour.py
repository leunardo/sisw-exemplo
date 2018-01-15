"""Recurso que envia horas"""

from flask_restful import Resource
from common.util import hora_atual, make_response


class Hour(Resource):

    def get(self):
        hora = hora_atual()
        return make_response(hora)
