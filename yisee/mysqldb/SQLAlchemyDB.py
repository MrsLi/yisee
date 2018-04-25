# coding=utf-8
from sqlalchemy import Column, String, create_engine,INT,Integer
from sqlalchemy.ext.declarative import declarative_base

#初始化数据库ORM连接（SQLAlchemy）

# 创建对象的基类:
Base = declarative_base()
# 定义News对象:
class News(Base):
    # 表的名字:
    __tablename__='ys_news'
    # 表的结构:
    id = Column(primary_key=True)
    title = Column(String(255),unique=True)  # 小说名
    author = Column(String(255),unique=True)  # 作者名
    type = Column(String(255),unique=True)  # 小说分类


# 定义Content对象:
class Content(Base):
    # 表的名字:
    __tablename__ = 'ys_content'

    # 表的结构:
    id = Column(primary_key=True)
    newid = Column(unique=True)
    zhangjie = Column(String(255),unique=True)
    content = Column(String(255),unique=True)