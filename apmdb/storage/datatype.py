from enum import Enum


# 支持上报的数据类型
# value 是支持的 type
class ApmData(Enum):
    PageSpeed = 'page_speed'
    AppStartInfo = 'app_start'
    BlockInfo = 'block_info'
    FPSInfo = 'fps_info'
    ExceptionInfo = 'exception_info'
    MemoryInfo = 'RabbitMemoryInfo'
