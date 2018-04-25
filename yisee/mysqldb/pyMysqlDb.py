# coding=utf-8
import pymysql
from yisee import settings
class MySql(object):

    def __init__(self):
        try:
            self.conn = pymysql.connect(
                    host=settings.MYSQL_HOST,
                    port =settings.MYSQL_PORT,
                    user=settings.MYSQL_USER,
                    passwd=settings.MYSQL_PASSWD,
                    db=settings.MYSQL_DBNAME,
                    charset='utf8'
            )
        except Exception as e:
            print("MySqlDBError Message:"+e)
        else:
            print('连接数据库成功')
            self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def update(self,sql):  #增删改
        res = self.cur.execute(sql)
        if res:
            self.conn.commit()
        else:
            self.conn.rollback()
        return res

    def show(self,sql): #查
        self.cur.execute(sql)
        res = self.cur.fetchall()
        return res
