# _*_ coding: utf-8 _*_
__author__ = 'mtianyan'
__date__ = '2017/8/26 17:07'

from . import home
from flask import render_template, url_for, redirect


# 登录
@home.route("/login/")
def login():
    return render_template("home/login.html")


# 退出
@home.route("/logout/")
def logout():
    return redirect(url_for('home.login'))


# 重定向到home模块下的登录。

# 会员注册
@home.route("/regist/")
def regist():
    return render_template("home/register.html")


# 会员中心
@home.route("/user/")
def user():
    return render_template("home/user.html")


# 修改密码
@home.route("/pwd/")
def pwd():
    return render_template("home/pwd.html")


# 评论
@home.route("/comments/")
def comments():
    return render_template("home/comments.html")


# 登陆日志
@home.route("/loginlog/")
def loginlog():
    return render_template("home/loginlog.html")


# 电影收藏
@home.route("/moviecol/")
def moviecol():
    return render_template("home/moviecol.html")


# 首页
@home.route("/")
def index():
    return render_template("home/index.html")


# animation
@home.route("/")
def animation():
    return render_template("home/animation.html")
