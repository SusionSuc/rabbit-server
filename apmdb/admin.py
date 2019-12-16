from django.contrib import admin
from apmdb.storage.models import *


admin.site.register(PageSpeed)
admin.site.register(AppStartInfo)
admin.site.register(MemoryInfo)
admin.site.register(ExceptionInfo)
admin.site.register(BlockInfo)
