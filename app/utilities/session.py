"""
セッション管理についてのユーティリティ
FastAPIにはFlaskのようなセッションが無さそうなので，自作した
一応JWTを使ったセッション管理の方法はあるが，サーバサイドで管理していないので厳密にはセッションではないので，自作した
JWT使う例
https://github.com/tiangolo/fastapi/issues/754#issuecomment-585386650
"""
from typing import Dict, Hashable
from uuid import uuid4
from cachelib.file import FileSystemCache

from app.configs import Config


class Session(object):
    """
    セッション管理をするクラス
    cachelibの機能を使ってファイルによってセッションを管理する
    セッション自体は１つの辞書っぽいもので，一番上のキーが各セッションのIDになるえ
    Flask Sessionの実装を参考に作成した
    https://github.com/fengsp/flask-session/blob/a88f07e7260ae582b0744de42e77c4625e6884ea/flask_session/sessions.py

    TODO: セッション情報を削除する機能を追加
    """

    def __init__(self, config: Config):
        self.cache = FileSystemCache(config.session_cache_dir)
        self.session_lifetime = config.session_lifetime

    def get(self, session_id: str) -> Dict[str, Hashable]:
        """
        与えられたセッションIDのセッション情報を取得する
        :param session_id: セッションID
        :return:
        """
        if not session_id:
            return {}
        return self._load_session_from_file(session_id)

    def set(self, key: str, value: Hashable, session_id: str = None) -> str:
        """
        セッションを追加する
        :param session_id: セッションId
        :param key: 追加するセッション情報のキー
        :param value: 追加するセッション情報の値
        """
        if not session_id:
            # セッションを新規作成
            session_id = self._generate_session_id()
        session_obj = self._load_session_from_file(session_id) or {}
        session_obj.update({key: value})
        self._save_session(session_id, session_obj)
        return session_id

    def destroy(self, session_id):
        """
        セッションを削除する
        :param session_id: 削除するセッションのID
        :return: None
        """
        self.cache.delete(session_id)

    def _load_session_from_file(self, session_id) -> Dict[str, Hashable]:
        """
        与えられたセッションIDの情報を取得する
        :param session_id: セッションID
        :return dict: セッション情報
        """
        return self.cache.get(session_id)

    def _save_session(self, session_id: str, obj: Hashable) -> None:
        self.cache.set(session_id, obj, timeout=self.session_lifetime)

    def _generate_session_id(self) -> str:
        return uuid4().hex
