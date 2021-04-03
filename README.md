# Docker, FastAPI, MySQLを用いたブログのサンプルアプリ

## 前提条件

講義内での指示に従ってDockerのインストールを完了させておくこと

- [Windowsの場合](docs/install-docker-windows.md)
- [Macの場合](docs/install-docker-windows.md)

## 実行方法

- Webアプリ
  - `docker-compose up`の実行中に`http://localhost:8000`にアクセス
- PHPMyadmin
  - `docker-compose up`の実行中に`http://localhost:8080`にアクセス

### 備考

- コンテナの初回実行時には，初期データ作成用として`docker/mysql/sqls/initdb.d/`に配置されているsqlファイルが実行される
  - docker-composeのログに`[Entrypoint]: MySQL init process done. Ready for start up.`が出力されるまでは待機(割と待つ)

## 開発の進め方

主に`app/`ディレクトリのファイルを編集して開発を進めていく

- `views.py`にルーティングや処理を記述
- `models/`ディレクトリにテーブルの定義を記述
  - テーブルを追加する際には`articles.py`を参考にするとよい 
- `templates/`ディレクトリにHTMLファイルを配置
- `statics/`ディレクトリにCSSやJavaScriptのファイルを配置

## 発展

- 外部パッケージを導入したいときは`docker/fastapi/requirements.txt`に追記して，再ビルド
