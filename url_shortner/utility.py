import traceback
from django.http import JsonResponse
from django.conf import settings


def capture_error(function):
    def executor(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            print(e.__str__())
            response = {
                "error":e.__str__(),
                "message":"failed",
                "status_code":500
            }
            if settings.DEBUG:
                response["exception"] = traceback.format_exc()
            return JsonResponse(response,status=500,safe=False)
    return executor