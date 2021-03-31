# Docker, FastAPI, MySQLを用いたブログのサンプルアプリ

## 前提条件

講義内での指示に従ってDockerのインストールを完了させておくこと

## 実行方法

`docker-compose up`を実行して`http://localhost:8000`にアクセス

### 備考

- コンテナの初回実行時には，初期データ作成用として`docker/mysql/sqls/initdb.d/`に配置されているsqlファイルが実行される
  - docker-composeのログに`[Entrypoint]: MySQL init process done. Ready for start up.`が出力されるまでは待機

## 開発の進め方

主に`app/`ディレクトリのファイルを編集して開発を進めていく

- `views.py`にルーティングや処理を記述
- `templates/`ディレクトリにHTMLファイルを配置
- `statics/`ディレクトリにCSSやJavaScriptのファイルを配置
- `models/`ディレクトリにテーブルの定義を記述していく
  - テーブルを追加する際には`articles.py`を参考にするとよい 
