"""
セッション管理についてのユーティリティ
FastAPIにはFlaskのようなセッションが無さそうなので，自作した


!!!!!!!!!! WARING !!!!!!!!!!
本当はRedisとかを使って管理するべきセッションをオブジェクトとして保管しているので，結構危険なきがする
"""
from collections.abc import MutableMapping


class SimpleSessions(MutableMapping):
    """
    セッション管理をするクラス
    """

    def __init__(self):
        self.sessions = {}

    def __getitem__(self, item):
        return self.sessions[item]

    def __setitem__(self, key, value):
        self.sessions[key] = value

    def __len__(self):
        return len(self.sessions)

    def __delitem__(self, key):
        del self.sessions[key]

    def __iter__(self):
        return self.sessions.items()
