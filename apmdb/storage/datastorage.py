"""
存储上报数据
"""

from .datatype import ApmData
import json
from .models import *

TAG = "🐰-->storage : "


def save_page_speed(page_speed_str):
    ps_json_dic: dict = json.loads(page_speed_str)
    page_speed = PageSpeed()
    page_speed.time = ps_json_dic.get('time')
    page_speed.pageName = ps_json_dic.get('pageName')
    page_speed.createStartTime = ps_json_dic.get('createStartTime')
    page_speed.createEndTime = ps_json_dic.get('createEndTime')
    page_speed.fullDrawFinishTime = ps_json_dic.get('fullDrawFinishTime')
    page_speed.resumeEndTime = ps_json_dic.get('resumeEndTime')
    page_speed.apiRequestCostStr = ps_json_dic.get('apiRequestCostStr')
    page_speed.save()
    print(TAG, "page_speed save ! time : ", page_speed.time)


def save_app_start(app_start_str):
    as_json_dic: dict = json.loads(app_start_str)
    app_start = AppStartInfo()
    app_start.time = as_json_dic.get('time')
    app_start.createStartTime = as_json_dic.get('createStartTime')
    app_start.createEndTime = as_json_dic.get('createEndTime')
    app_start.fullShowCostTime = as_json_dic.get('fullShowCostTime')
    app_start.save()
    print(TAG, "app_start save ! time : ", app_start.time)


def save_block_info(block_info_str):
    print("store data save_block_info :", block_info_str)
    pass


def save_memory_info(memory_info_str):
    print("store data save_memory_info :", memory_info_str)
    pass


data_storage_impl = {ApmData.PageSpeed.value: save_page_speed,
                     ApmData.AppStartInfo.value: save_app_start,
                     ApmData.BlockInfo.value: save_block_info,
                     ApmData.MemoryInfo.value: save_memory_info}

data_storage_types = list(data_storage_impl.keys())

# print(data_storage_types)
