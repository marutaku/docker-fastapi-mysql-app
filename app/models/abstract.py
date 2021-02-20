"""
DB関連の共通処理
!!!!ここは先生の指示があった場合のみ修正してください!!!!
"""
from typing import List, Dict
import pymysql.cursors

from app.configs import Config


class AbstractModel(object):
    """
    DB関連の共通処理をするクラス
    SQLの実行などは，このクラスのメソッドを通して行う．
    そのため，全てのモデルはこのクラスを継承する
    """

    def __init__(self, config: Config):
        """
        初期化
        :param config: アプリケーションの設定．ここにデータベースの情報も入っていることを想定
        """

        self.connection = pymysql.connect(
            host=config.mysql_host,
            user=config.mysql_username,
            password=config.mysql_password,
            database=config.mysql_database,
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

    def __del__(self):
        self.connection.close()
