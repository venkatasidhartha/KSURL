from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import redirect

# import request
from url_shortner.request.createurl import CreateUrlRequest

# import service
from url_shortner.service.url import UrlService

# import common stuff
from url_shortner.utility import capture_error
from url_shortner.common.response import CommonResponse

#  Create your views here.


def redirect_url(request,uuid):
    service = UrlService()
    url = service.read(uuid)
    return redirect(url,status=301)




@api_view(["POST"])
@capture_error
def create_url(request):
    request_data = CreateUrlRequest(request.data)
    service = UrlService()
    service_response = service.create(request_data.get_url())
    return CommonResponse(message="successfully created",data=service_response.get_dict(),status_code=201).get_response()

