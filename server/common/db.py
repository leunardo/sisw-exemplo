from sys import stderr
import MySQLdb
from MySQLdb.cursors import DictCursor


class Db:
    """Classe responsavel por fazer a comunicacao com o banco de dados."""

    @staticmethod
    def _connect():
        try:
            return MySQLdb.connect(host='localhost', 
                                   user='leo', 
                                   passwd='1234', 
                                   db='p_test', 
                                   cursorclass=DictCursor)

        except Exception as err:
            print('Problema ao conectar-se com o banco de dados: ', err, file=stderr)

    def query(self, query, *args):
        """Executa determinada query.

        Abre conexão com o banco, abre um cursor, executa  a query, fecha o cursor e então retorna os dados.

        query -> str: Query a ser executada.
        *args -> tuple: parametros que serão inseridos na query.
        """
        db = self._connect()
        c = db.cursor()
        try:
            c.execute(query, args)
            dados = c.fetchall()

            return dados
        except Exception as err:
            print("Erro ocorreu durante a query: ", err, file=stderr)
        finally:
            c.close()
