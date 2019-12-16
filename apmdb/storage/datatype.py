from enum import Enum


# 支持上报的数据类型

class ApmData(Enum):
    PageSpeed = 'RabbitPageSpeedInfo'
    AppStartInfo = 'RabbitAppStartSpeedInfo'
    BlockInfo = 'RabbitBlockFrameInfo'
    ExceptionInfo = 'RabbitExceptionInfo'
    MemoryInfo = 'RabbitMemoryInfo'
