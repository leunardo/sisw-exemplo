from common.db import Db


class RepositoryUsuario:

    def __init__(self):
        self._db = Db()

    def get_all_users(self):
        query = 'Select * from usuario'
        return self._db.query(query)

    def get_user(self, id_usuario):
        query = 'Select * from usuario where id_usuario = %s'
        return self._db.query(query, id_usuario)

    def add_user(self, user):
        query = 'Insert into usuario (nome) values (%s)'
        return self._db.insert(query, user.nome)

    def alter_user(self, user, id):
        query = 'Update usuario set nome = %s where id_usuario = %s'
        return self._db.insert(query, user.nome, id)
