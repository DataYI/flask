# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 11:46:07 2018

@author: DataAnt
"""
from flask_sqlalchemy import SQLAlchemy

from .extensions import bcrypt

db = SQLAlchemy()

# 创建关联表,两个字段的外键是另两个表
# post表中一篇文章对应关联表tags中多篇文章
# 一个tag表中标签对应关联表tags中多个标签
tags = db.Table(
    'post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    # 创建一个虚拟的posts列
    posts = db.relationship(
        'Post',
        backref='user', # 让Post对象可以通过Post.user来访问User对象
        lazy='dynamic'
    )


    def __init__(self, username):
        self.username = username


    def __repr__(self):
        return "<User '{}'>".format(self.username)


    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)


    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)


    def is_active(self):
        return True


    def get_id(self):
        return self.id


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    # 一对多，一篇文章对应多条评论
    comments = db.relationship(
        'Comment',
        backref='post',
        lazy='dynamic'
    )
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    # 多对多，文章与标签的对应
    tags = db.relationship(
        'Tag',
        secondary=tags,
        backref=db.backref('post', lazy='dynamic')
    )


    def __init__(self, title):
        self.title = title


    def __repr__(self):
        return "<Post '{}'>".format(self.title)


class Tag(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))


    def __init__(self, title):
        self.title = title


    def __repr__(self):
        return "<Tag '{}'>".format(self.title)


class Comment(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))


    def __repr__(self):
        return "<Comment '{}'>".format(self.text[:15])



