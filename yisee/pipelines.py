# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from yisee.mysqldb.pyMysqlDb import MySql
from yisee.mysqldb.SQLAlchemyDB import News,Content
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
import sys
class YiseePipelineDb(object):
    def open_spider(self,spider):
        #self.mySql = MySql()
        engine = create_engine("mysql+pymysql://root:root@localhost:3306/yiseedb?charset=utf8", max_overflow=5,encoding='utf-8')
        # 创建DBSession类型:
        self.engine = engine

    def process_item(self, item, spider):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        print(item['title'])
        print(item['author'])
        print(item['zhangjie'])
        print(item['content'])
        try:
            news = session.query(News).filter(News.title==item['title']).first()
            if news is not None:
                # 插入章节内容
                content = Content(newid=news.id, zhangjie=item['zhangjie'], content=item['content'])
                session.add(content)
                session.commit()
                session.flush()
            else:
                # 没有查询到结果
                # 先插入news表,再插入章节表
                news = News(title=item['title'], author=item['author'], type='0')
                session.add(news)
                try:
                    session.commit()
                    session.flush()
                except:
                    print(sys.exc_info()[0])

                try:
                    newsResult = session.query(News).filter(News.title == item['title']).first()
                    self.insert_content(session, item, newsResult)
                except NoResultFound:
                    print('找不到这本小说的表内容')
        except NoResultFound:
            pass
        session.close()
        print('插章节表完毕')



    #插入章节内容
    def insert_content(self,session, item, result):
        # 插入章节
        content = session.query(Content).filter(Content.zhangjie == item['zhangjie']).first()
        if content is None:
            newid = result.id
            content = Content(newid=newid, zhangjie=item['zhangjie'], content=item['content'])
            session.add(content)
            session.commit()
            session.flush()
        print('插入章节内容完毕')