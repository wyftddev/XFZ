from django.http import JsonResponse

class HttpCode(object):
    SUCCESS = 200
    UNAUTH = 401
    SERVERERROR = 500
    METHODERROR = 405
    PARAMSERROR = 400

def result(code=200, message="", data=None, **kwargs):
    json_dict = {'code': code, 'message': message, 'data': data}
    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        json_dict.update(kwargs)
    return JsonResponse(json_dict)

def success():
    return result()

def server_error(message='', data=None, **kwargs):
    return result(code=HttpCode.SERVERERROR, message=message,data=data, **kwargs)

def unauth_error(message='', data=None, **kwargs):
    return result(code=HttpCode.UNAUTH, message=message,data=data, **kwargs)

def method_error(message='', data=None, **kwargs):
    return result(code=HttpCode.METHODERROR, message=message,data=data, **kwargs)

def parms_error(message='', data=None, **kwargs):
    return result(code=HttpCode.PARAMSERROR, message=message,data=data, **kwargs)