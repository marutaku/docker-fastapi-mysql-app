"""
カスタムエラー
学生はいじらなくで良い
"""


class UserNotLoggedIn(Exception):
    """ユーザがログインしていない時に送る"""
    pass
