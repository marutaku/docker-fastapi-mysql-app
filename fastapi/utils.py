import pymysql.cursors


class DB:
    def __init__(self, password='password', db='app'):
            self.connection = pymysql.connect(
                    host='mysql',
                    user='root',
                    password='password',
                    db="app",
                    charset='utf8',
                    cursorclass=pymysql.cursors.DictCursor
                    )
        
    def __del__(self):
        self.connection.close()
        
    def select(self, sql , query=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, query)
        return cursor.fetchall()
