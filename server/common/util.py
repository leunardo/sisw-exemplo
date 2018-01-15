"""Módulo utilitário"""

from datetime import datetime
from json import dumps
import flask


def hora_atual():
    """"Retorna a hora atual"""
    hora = str(datetime.now())
    return hora


class Response(flask.Response):

    def __init__(self, data, status, headers):
        headers['Content-type'] = 'application/json'
        super().__init__(response=dumps(data), status=status, headers=headers)


def make_response(data, status=200, headers=None):
    if headers is None: headers = {}
    return flask.make_response(Response(data, status, headers))
