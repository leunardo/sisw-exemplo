from sys import stderr
import MySQLdb
from MySQLdb.cursors import DictCursor


class Db:
    """Classe responsavel por fazer a comunicacao com o banco de dados."""

    @staticmethod
    def _connect():
        try:
            db = MySQLdb.connect(host='localhost',
                                 user='leo',
                                 passwd='1234',
                                 db='p_test',
                                 cursorclass=DictCursor)

            return db

        except Exception as err:
            print('Problema ao conectar-se com o banco de dados: ', err, file=stderr)

    @staticmethod
    def dispose(db, cursor):
        cursor.close()
        db.close()

    def query(self, query, *args):
        """Executa determinada query.

        Abre conexão com o banco, abre um cursor, executa  a query, fecha o cursor e então retorna os dados.

        :param query: Query a ser executada.
        :param args:  parametros que serão inseridos na query.
        :return: Uma lista dos dados obtidos.
        """

        db = self._connect()
        c = db.cursor()
        c.execute(query, args)
        dados = c.fetchall()
        self.dispose(db, c)

        return dados

    def insert(self, query, *args):
        """Insere uma entidade.

        :param query: Query a ser executada.
        :param args: parametros que serão inseridos na query.
        :return: Id da linha inserida.
        """
        db = self._connect()
        c = db.cursor()
        try:
            c.execute(query, args)
            db.commit()
            return {"id": c.lastrowid}
        except MySQLdb.Error:
            db.rollback()
        finally:
            self.dispose(db, c)

    def delete(self, query, *args):
        """Deleta uma entidade.

        :param query: Query a ser executada.
        :param args: parametros que serão inseridos na query.
        """
        db = self._connect()
        c = db.cursor()
        try:
            c.execute(query,args)
            db.commit()
        except MySQLdb.Error:
            db.rollback()
        finally:
            self.dispose(db, c)
