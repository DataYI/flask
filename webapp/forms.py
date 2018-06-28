# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 11:45:47 2018

@author: DataAnt
"""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    StringField, 
    TextAreaField, 
    PasswordField, 
    BooleanField
)
from wtforms.validators import (
    DataRequired, 
    Length,
    EqualTo, 
    URL
)

from .models import User

class PostForm(FlaskForm):
    title = StringField('标题', [DataRequired(), Length(max=255)])
    text = TextAreaField('正文', [DataRequired()])


class CommentForm(FlaskForm):
    name = StringField(
        '姓名',
        validators=[DataRequired(), Length(max=255)]
    )
    text = TextAreaField('评论', validators=[DataRequired()])
    

class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(max=255)])
    password = PasswordField('密码', validators=[DataRequired()])
    remember = BooleanField('记住密码')

    def validate(self):
        """
        重写表单验证方法，增加检查用户名是否存在和密码是否匹配的功能
        """
        check_validate = super().validate()
        # 如果验证没有通过
        if not check_validate:
            return False
        # 检查是否存在拥有该用户名的用户
        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            print('user empty')
            self.username.errors.append('用户名或密码无效')
            return False
        # 检查密码是否匹配
        if not user.check_password(self.password.data):
            print('密码错')
            self.username.errors.append('用户名或密码无效')
            return False
        return True


class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(max=255)])
    password = PasswordField('密码', validators=[DataRequired(), Length(min=8)])
    confirm = PasswordField('确认密码', [DataRequired(), EqualTo('password')])

    #recaptcha = RecaptchaField()


    def validate(self):
        check_validate = super().validate()

        # 如果验证没有通过
        if not check_validate:
            return False
        # 检查是否存在拥有该用户名的用户
        user = User.query.filter_by(username=self.username.data).first()
        # 如果该用户名已经被使用了
        if user:
            self.username.errors.append('用户名已经存在')
            return False
        return True