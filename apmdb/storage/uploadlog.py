"""
数据上报接口
"""

from django.http import HttpResponse
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
import json
import base64
from .datastorage import data_storage_impl
from .datastorage import data_storage_types

TAG = "🐰-->upload : "


@csrf_exempt  # 解决 crsf(cross site request forgery 跨站域请求伪造) 验证的问题 : https://www.dazhuanlan.com/2019/10/10/5d9f44110d951/
def upload_log(request: HttpRequest):
    """
    :param request:
    :return:
    """

    # print(request.body)

    if request.method == 'POST':
        str_list = parse_to_json_str(json.loads(request.body.decode()))
        for json_str in str_list:
            store_point(json_str)

    return HttpResponse("upload success!")


def parse_to_json_str(json_body):
    """
    把上报的数据解析成json数组
    :param json_body:
    :return:
    """
    ret_str_list = []
    content: str = json_body['content']
    if content.find('&'):
        for point in content.split('&'):
            point_json = base64.b64decode(point)
            ret_str_list.append(point_json)
    else:
        point_json = base64.b64decode(content)
        ret_str_list.append(point_json)

    return ret_str_list


def store_point(json_str):
    json_dic = json.loads(json_str)
    data_type = json_dic['type']

    if data_type not in data_storage_types:
        print("unsupprot data type :", data_type)
        return

    print_report_info(json_dic)

    data_storage_impl[data_type](json_dic['infoStr'], json_dic['deviceInfoStr'])


def print_report_info(json_dic):
    print(TAG, "time : ", json_dic['time'], "; page_name : ", json_dic['pageName'], "; device_info_str : ",
          json_dic['deviceInfoStr'], "; infoStr :", json_dic['infoStr'])
