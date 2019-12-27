"""
通用的数据bean
"""

from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

import json


def json_response(data, code="200", msg="success"):
    result = {"code": code, "msg": msg, "data": serializers.serialize('python', data)}
    return JsonResponse(result)


def obj_response(data: object, code="200", msg="success"):
    result = {"code": code, "msg": msg, "data": data.__dict__}
    return HttpResponse(json.dumps(result.__dict__))


def str_list_response(data: list, code="200", msg="success"):
    result = {"code": code, "msg": msg, "data": data}
    return JsonResponse(result, safe=False)
