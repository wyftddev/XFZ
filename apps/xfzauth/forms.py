from django import forms

from apps.forms import FormMixin


class LoginForm(forms.Form, FormMixin):
    telephone = forms.CharField(required=True, max_length=11, error_messages={
        'max_length': '电话必须是11位！',
        'require': '请输入telephone字段！'
    })
    password = forms.CharField(max_length=20, min_length=8, error_messages={
        'min_length': '密码不能少于8位！',
        'max_length': '密码不能多于20位！'
    })
    remember = forms.IntegerField(required=False)

