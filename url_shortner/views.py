from django.shortcuts import render
from django.http import HttpResponseNotFound
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect
from django_redis import get_redis_connection

# import request
from url_shortner.request.createurl import CreateUrlRequest

# import service
from url_shortner.service.url import UrlService

# import common stuff
from url_shortner.utility import capture_error
from url_shortner.common.response import CommonResponse

#  Create your views here.

def home(request):
    return HttpResponseNotFound(render(request, 'page_not_found.html'))


def redirect_url(request,uuid):
    try:
        redis_client = get_redis_connection()
        cached_url = redis_client.get(uuid)
        if cached_url:
            return redirect(cached_url.decode(), status=301)
        service = UrlService()
        url = service.read(uuid)
        redis_client.set(uuid, url)
        return redirect(url,status=301)
    except:
        return HttpResponseNotFound(render(request, 'page_not_found.html'))





@api_view(["POST"])
@permission_classes([IsAuthenticated])
@capture_error
def create_url(request):
    request_data = CreateUrlRequest(request.data)
    service = UrlService()
    service_response = service.create(request_data.get_url())
    return CommonResponse(message="successfully created",data=service_response.get_dict(),status_code=201).get_response()

