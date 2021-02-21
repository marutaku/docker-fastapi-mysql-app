"""
WebアプリのDB設定などをここに書く
"""
from pydantic import BaseConfig


class Config(BaseConfig):
    """
    設定を管理するクラス
    BaseConfigを継承しているので，Config.json_loadsを使えばJSONからConfigに変換できる
    """
    mysql_host: str = "mysql"
    mysql_username: str = "root"
    mysql_password: str = "password"
    mysql_database: str = "app"
    session_cache_dir: str = "__cache__"
    # セッションは1日保持する
    session_lifetime: int = 24 * 60 * 60
