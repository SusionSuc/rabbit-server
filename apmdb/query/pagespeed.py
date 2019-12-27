from django.http import HttpResponse
from django.http import HttpRequest
from ..storage.models import PageSpeed
TAG = "🐰-->page-list : "


def all_page(request: HttpRequest):

    print(TAG, "params :", request.content_params)

    print(TAG, PageSpeed.objects.all())

    return HttpResponse("query success!")