"""
存储上报数据
"""

from .datatype import ApmData
import json
from .models import *

TAG = "🐰-->storage : "


def patch_device_info(device_info: DeviceInfo, device_info_str):
    print(device_info_str)
    device_dic: dict = json.loads(device_info_str)
    device_info.deviceName = device_dic.get('deviceName')
    device_info.appVersionCode = device_dic.get('appVersionCode')
    device_info.deviceId = device_dic.get('deviceId')
    device_info.systemVersion = device_dic.get('systemVersion')
    device_info.memorySize = device_dic.get('memorySize')
    device_info.rom = device_dic.get('rom')
    device_info.supportAbi = device_dic.get('supportAbi')
    device_info.manufacturer = device_dic.get('manufacturer')
    device_info.isRoot = device_dic.get('isRoot')
    pass


def save_page_speed(page_speed_str, device_info_str="", use_time=0):
    ps_json_dic: dict = json.loads(page_speed_str)
    page_speed = PageSpeed()
    page_speed.time = ps_json_dic.get('time')
    page_speed.pageName = ps_json_dic.get('pageName')
    page_speed.createStartTime = ps_json_dic.get('createStartTime')
    page_speed.createEndTime = ps_json_dic.get('createEndTime')
    page_speed.fullDrawFinishTime = ps_json_dic.get('fullDrawFinishTime')
    page_speed.resumeEndTime = ps_json_dic.get('resumeEndTime')
    page_speed.apiRequestCostStr = ps_json_dic.get('apiRequestCostStr')
    patch_device_info(page_speed, device_info_str)
    page_speed.useTime = use_time
    page_speed.save()
    print(TAG, "page_speed save ! time : ", page_speed.time, " use time: ", use_time)


def save_app_start(app_start_str, device_info_str="", use_time=0):
    as_json_dic: dict = json.loads(app_start_str)
    app_start = AppStartInfo()
    app_start.time = as_json_dic.get('time')
    app_start.createStartTime = as_json_dic.get('createStartTime')
    app_start.createEndTime = as_json_dic.get('createEndTime')
    app_start.fullShowCostTime = as_json_dic.get('fullShowCostTime')
    patch_device_info(app_start, device_info_str)
    app_start.useTime = use_time
    app_start.save()
    print(TAG, "app_start save ! time : ", app_start.time, " use time: ", use_time)


def save_block_info(block_info_str, device_info_str="", use_time=0):
    block_json_dic: dict = json.loads(block_info_str)
    block = BlockInfo()
    block.time = block_json_dic.get('time')
    block.pageName = block_json_dic.get('pageName')
    block.identifier = block_json_dic.get('identifier')
    block.blockTime = block_json_dic.get('blockTime')
    patch_device_info(block, device_info_str)
    block.useTime = use_time
    block.save()
    print(TAG, "block_info save ! time : ", block.time, " use time: ", use_time)
    pass


def save_fps_info(fps_info_str, device_info_str="", use_time=0):
    fps_json_dict: dict = json.loads(fps_info_str)
    fps = FPSInfo()
    fps.time = fps_json_dict.get('time')
    fps.pageName = fps_json_dict.get('pageName')
    fps.minFps = fps_json_dict.get('minFps')
    fps.maxFps = fps_json_dict.get('maxFps')
    fps.avgFps = fps_json_dict.get('avgFps')
    patch_device_info(fps, device_info_str)
    fps.useTime = use_time
    fps.save()
    print(TAG, "fps info save ! time : ", fps.time, " use time: ", use_time)


def save_exception_info(exception_info_str, device_info_str="", use_time=0):
    ei_dict = json.loads(exception_info_str)
    exception = ExceptionInfo()
    exception.time = ei_dict.get('time')
    exception.exceptionName = ei_dict.get('exceptionName')
    exception.identifier = ei_dict.get('identifier')
    exception.thread = ei_dict.get('thread')
    exception.pageName = ei_dict.get('pageName')
    patch_device_info(exception, device_info_str)
    exception.useTime = use_time
    exception.save()
    print(TAG, "exception info save ! time : ", exception.time, " use time: ", use_time)


def save_memory_info(memory_info_str, device_info_str="", use_time=0):
    print("store data save_memory_info :", memory_info_str)
    pass


data_storage_impl = {ApmData.PageSpeed.value: save_page_speed,
                     ApmData.AppStartInfo.value: save_app_start,
                     ApmData.BlockInfo.value: save_block_info,
                     ApmData.MemoryInfo.value: save_memory_info,
                     ApmData.FPSInfo.value: save_fps_info,
                     ApmData.ExceptionInfo.value: save_exception_info}

data_storage_types = list(data_storage_impl.keys())

# print(data_storage_types)
