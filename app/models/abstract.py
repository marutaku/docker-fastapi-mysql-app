"""
DB関連の共通処理
!!!!ここは先生の指示があった場合のみ修正してください!!!!
"""
from typing import List, Dict, Tuple
import pymysql.cursors


class AbstractModel(object):
    """
    DB関連の共通処理をするクラス
    SQLの実行などは，このクラスのメソッドを通して行う．
    そのため，全てのモデルはこのクラスを継承する
    """

    def __init__(self, host, port, username, password, db_name):
        """
        初期化
        :param host: MySQLのホスト
        :param port: MySQLのポート
        :param username: MySQLのユーザ名
        :param password: MySQLのパスワード
        """
        self.connection = pymysql.connect(
            host=host,
            port=port,
            user=username,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor,
            # トランザクションをちゃんとやるならFalseにしてコードを修正
            autocommit=True
        )

    def fetch_all(self, sql_statement: str, *args: any) -> List[Dict[str, any]]:
        """
        複数のレコードを取得する
        :param sql_statement: SQL文
        :param args: SQLに代入する値
        :return: 取得したレコード(List)
        """
        with self.connection.cursor() as cursor:
            self._execute(sql_statement, cursor, *args)
            return cursor.fetchall()

    def fetch_one(self, sql_statement, *args) -> Dict[str, any]:
        """
        レコードを１つだけ取得する
        :param sql_statement: SQL文
        :param args: SQLに代入する値
        :return: 取得したレコード(Dict)
        """
        with self.connection.cursor() as cursor:
            self._execute(sql_statement, cursor, *args)
            return cursor.fetchone()

    def execute(self, sql_statement, *args) -> None:
        """

        :param sql_statement:
        :param args:
        :return:
        """
        with self.connection.cursor() as cursor:
            self._execute(sql_statement, cursor, *args)

    def _execute(self, sql_statement: str, cursor: pymysql.connections.Cursor, *args: any) -> None:
        """
        SQLを実行する．fetchとかはやらない.
        :param sql_statement: SQL文
        :param cursor: PyMySQLのカーソル
        :param args: SQLに代入する値
        :return:
        """
        cursor.execute(sql_statement, args)
