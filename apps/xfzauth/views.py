from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.http import require_POST

from . import forms
from utils import restful

@require_POST
def login_view(request):
    form = forms.LoginForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get('telephone')
        password = form.cleaned_data.get('password')
        remember = form.cleaned_data.get('remember')
        user = authenticate(request, telephone=telephone, password=password)
        if user:
            if user.is_active:
                login(request, user)
                if remember:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                return restful.success()
                # return JsonResponse({'code': 200, 'message': '', 'data': {}})
            else:
                return restful.unauth_error(message='您的账号已被冻结！')
                # return JsonResponse({'code': 405, 'message': '您的账号已被冻结！', 'data':{}})
        else:
            return restful.parms_error(message='手机号或密码错误！')
            # return JsonResponse({'code': 400, 'message': '手机号或密码错误！', 'data':{}})
    else:
        return restful.parms_error(message=form.get_errors())
        # return JsonResponse({'code': 400, 'message': '参数输入错误！', 'data': form.get_errors()})