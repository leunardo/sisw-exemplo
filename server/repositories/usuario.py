from common.db import Db


class RepositoryUsuario:

    def __init__(self):
        self._db = Db()

    def get_all_users(self):
        query = 'Select * from usuario'
        return self._db.query(query)

    def get_user(self, name):
        query = 'Select * from usuario where nome = %s'
        return self._db.query(query, name)
