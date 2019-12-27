from django.http import HttpResponse
from django.http import HttpRequest
from ..storage.models import PageSpeed
from django.db.models import QuerySet
from ..base.restfulapi import str_list_response
from ..base.restfulapi import json_response

TAG = "🐰-->page-list : "


def all_page(request: HttpRequest):
    """
    返回当前所有的测试页面
    :param request:
    :return:
    """

    distinct_pages: QuerySet = PageSpeed.objects.values("pageName").distinct()

    page_list = []
    for item in distinct_pages.iterator():
        page_list.append(item["pageName"])

    return str_list_response(page_list)


def speed_list(request: HttpRequest):
    page_name: str = request.GET.get("page_name")

    if len(page_name) == 0:
        return HttpResponse("please specify page name")

    query_list: QuerySet = PageSpeed.objects.filter(pageName=page_name)

    print(TAG, "page list size ", len(query_list))

    return json_response(query_list)
