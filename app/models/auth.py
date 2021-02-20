"""
ログイン関連の処理をここに書く
"""
from .abstract import AbstractModel

from hashlib import sha256


class AuthModel(AbstractModel):
    """
    ログイン，セッションなどの情報はここに書く
    """

    def __init__(self, config):
        super().__init__(config)

    def login(self, username, password):
        """
        :param username: ログインするユーザのユーザ名
        :param password: ログインするユーザのパスワード
        :return bool:ログインが成功したか
        """
        hashed_password = self.hash_password(password)
        sql = "SELECT * FROM users where username=%s AND password=%s"
        user = self.fetch_one(sql, username, hashed_password)
        # 該当するユーザがいなければFalseを返す
        if not user:
            return False, None
        # TODO: セッションに情報を追加
        return True, user["id"]

    def create_user(self, username, password):
        """
        新規ユーザ作成
        :param username: ユーザ名
        :param password: パスワード
        :return:
        """
        hashed_password = self.hash_password(password)
        sql = "INSERT INTO users(username, password) VALUE (%s, %s);"
        self.execute(sql, username, hashed_password)

    def logout(self):
        pass

    def hash_password(self, password: str):
        """
        パスワードを安全に保存するためにハッシュ化する．
        :param password: パスワード
        :return: ハッシュ化されたパスワード
        """
        return sha256(password.encode()).hexdigest()
