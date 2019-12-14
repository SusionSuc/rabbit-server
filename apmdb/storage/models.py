from django.db import models


# Create your models here.

class PageSpeed(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    time = models.IntegerField(default=0)
    createStartTime = models.IntegerField(default=0)
    createEndTime = models.IntegerField(default=0)
    inflateFinishTime = models.IntegerField(default=0)
    fullDrawFinishTime = models.IntegerField(default=0)
    resumeEndTime = models.IntegerField(default=0)
    pageName = models.CharField(max_length=100)
    apiRequestCostStr = models.CharField(max_length=200)


class AppStartInfo(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    time = models.IntegerField(default=0)
    createStartTime = models.IntegerField(default=0)
    createEndTime = models.IntegerField(default=0)
    fullShowCostTime = models.IntegerField(default=0)


class MemoryInfo(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    time = models.IntegerField(default=0)
    totalSize = models.IntegerField(default=0)
    vmSize = models.IntegerField(default=0)
    nativeSize = models.IntegerField(default=0)
    otherSize = models.IntegerField(default=0)


class ExceptionInfo(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    time = models.IntegerField(default=0)
    crashTraceStr = models.CharField(max_length=10000)
    simpleMessage = models.CharField(max_length=1000)
    threadName = models.CharField(max_length=100)
    currentSystemName = models.CharField(max_length=100)
    exceptionName = models.CharField(max_length=200)


class BlockInfo(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    time = models.IntegerField(default=0)
    costTime = models.IntegerField(default=0)
    blockIdentifier = models.CharField(max_length=200)
    blockFrameStackTraceStrList = models.CharField(max_length=100000)
