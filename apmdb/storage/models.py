from django.db import models


# Create your models here.

# 基本的设备信息
class DeviceInfo(models.Model):
    deviceName = models.CharField(max_length=100, default="")
    deviceId = models.CharField(max_length=100, default="")
    systemVersion = models.CharField(max_length=100, default="")
    appVersionCode = models.CharField(max_length=100, default="")

    class Meta:
        abstract = True


class PageSpeed(DeviceInfo):
    time = models.IntegerField(default=0)
    createStartTime = models.IntegerField(default=0)
    createEndTime = models.IntegerField(default=0)
    inflateFinishTime = models.IntegerField(default=0)
    fullDrawFinishTime = models.IntegerField(default=0)
    resumeEndTime = models.IntegerField(default=0)
    pageName = models.CharField(max_length=100)
    apiRequestCostStr = models.CharField(max_length=200, null=True)


class AppStartInfo(DeviceInfo):
    time = models.IntegerField(default=0)
    createStartTime = models.IntegerField(default=0)
    createEndTime = models.IntegerField(default=0)
    fullShowCostTime = models.IntegerField(default=0)


class BlockInfo(DeviceInfo):
    time = models.IntegerField(default=0)
    blockTime = models.IntegerField(default=0)
    identifier = models.CharField(max_length=500)
    pageName = models.CharField(max_length=100, default="")


class FPSInfo(DeviceInfo):
    time = models.IntegerField(default=0)
    pageName = models.CharField(max_length=100, default="")
    minFps = models.IntegerField(default=0)
    maxFps = models.IntegerField()
    avgFps = models.IntegerField


class MemoryInfo(DeviceInfo):
    time = models.IntegerField(default=0)
    totalSize = models.IntegerField(default=0)
    vmSize = models.IntegerField(default=0)
    nativeSize = models.IntegerField(default=0)
    otherSize = models.IntegerField(default=0)


class ExceptionInfo(DeviceInfo):
    time = models.IntegerField(default=0)
    crashTraceStr = models.CharField(max_length=10000)
    simpleMessage = models.CharField(max_length=1000)
    threadName = models.CharField(max_length=100)
    currentSystemName = models.CharField(max_length=100)
    exceptionName = models.CharField(max_length=200)
