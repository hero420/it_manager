#coding=utf-8
from django import forms
class User_Login(forms.Form):
    username=forms.CharField(error_messages={'required':'用户名不能为空'})
    password=forms.CharField(error_messages={'required':'密码不能为空'})