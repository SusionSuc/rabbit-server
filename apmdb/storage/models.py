from django.db import models


# Create your models here.

# 基本的设备信息
class DeviceInfo(models.Model):
    deviceName = models.CharField(max_length=100, default="")
    deviceId = models.CharField(max_length=100, default="")
    systemVersion = models.CharField(max_length=100, default="")
    appVersionCode = models.CharField(max_length=100, default="")
    memorySize = models.CharField(max_length=100, default="")
    rom = models.CharField(max_length=100, default="")
    supportAbi = models.CharField(max_length=100, default="")
    manufacturer = models.CharField(max_length=100, default="")
    isRoot = models.CharField(max_length=100, default="False")
    useTime = models.CharField(default=0, max_length=50)
    time = models.CharField(default=0, max_length=50)

    class Meta:
        abstract = True


class PageSpeed(DeviceInfo):
    createStartTime = models.CharField(default=0, max_length=50)
    createEndTime = models.CharField(default=0, max_length=50)
    inflateFinishTime = models.CharField(default=0, max_length=50)
    fullDrawFinishTime = models.CharField(default=0, max_length=50)
    resumeEndTime = models.CharField(default=0, max_length=50)
    pageName = models.CharField(max_length=100)
    apiRequestCostStr = models.CharField(max_length=200, null=True)


class AppStartInfo(DeviceInfo):
    createStartTime = models.CharField(default=0, max_length=50)
    createEndTime = models.CharField(default=0, max_length=50)
    fullShowCostTime = models.IntegerField(default=0)


class BlockInfo(DeviceInfo):
    blockTime = models.CharField(default=0, max_length=50)
    identifier = models.CharField(max_length=500)
    pageName = models.CharField(max_length=100, default="")


class FPSInfo(DeviceInfo):
    pageName = models.CharField(max_length=100, default="")
    minFps = models.IntegerField(default=0)
    maxFps = models.IntegerField(default=0)
    avgFps = models.IntegerField(default=0)


class ExceptionInfo(DeviceInfo):
    pageName = models.CharField(max_length=200, default="")
    exceptionName = models.CharField(max_length=200, default="")
    thread = models.CharField(max_length=100, default="")
    identifier = models.CharField(max_length=300, default="")


class MemoryInfo(DeviceInfo):
    totalSize = models.IntegerField(default=0)
    vmSize = models.IntegerField(default=0)
    nativeSize = models.IntegerField(default=0)
    otherSize = models.IntegerField(default=0)
