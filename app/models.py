# -*- coding: utf-8 -*-

# Mysql -- databse
# from peewee import MySQLDatabase, Model, CharField, BooleanField, IntegerField
# from conf.config import config
#cfg = config[os.getenv('FLASK_CONFIG') or 'default']
#db = MySQLDatabase(host=cfg.DB_HOST, user=cfg.DB_USER, passwd=cfg.DB_PASSWD, database=cfg.DB_DATABASE)

from werkzeug.security import check_password_hash
from flask_login import UserMixin
from app import login_manager
from peewee import SqliteDatabase, Model, CharField, BooleanField, IntegerField
import os
import json

db = SqliteDatabase('app.db')

class BaseModel(Model):
    class Meta:
        database = db

    def __str__(self):
        r = {}
        for k in self._data.keys():
            try:
                r[k] = str(getattr(self, k))
            except:
                r[k] = json.dumps(getattr(self, k))
        # return str(r)
        return json.dumps(r, ensure_ascii=False)


# 管理员工号
class User(UserMixin, BaseModel):
    username = CharField()  # 用户名
    password = CharField()  # 密码Hash
    fullname = CharField(default='x')  # 真实性名
    email = CharField(default='y')  # 邮箱
    phone = CharField(default='z')  # 电话
    status = BooleanField(default=True)  # 生效失效标识

    def verify_password(self, raw_password):
        return check_password_hash(self.password, raw_password)
    


# 通知人配置
class CfgNotify(BaseModel):
    check_order = IntegerField()  # 排序
    notify_type = CharField()  # 通知类型：MAIL/SMS
    notify_name = CharField()  # 通知人姓名
    notify_number = CharField()  # 通知号码
    status = BooleanField(default=True)  # 生效失效标识

# class for aescu
class Client(BaseModel):
    pass

@login_manager.user_loader
def load_user(user_id):
    return User.get(User.id == int(user_id))


# 建表
def create_table():
    db.connect()
    db.create_tables([CfgNotify, User])
    db.close()

# 数据库初始化
def init_db():
    create_table()

# 数据库关闭
def close_db(e=None):
    db.close()

# app与数据库binding
def init_app(app):
    init_db()
    app.teardown_appcontext(close_db)


if __name__ == '__main__':
    create_table()
