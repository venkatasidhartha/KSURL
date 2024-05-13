from django.middleware.csrf import get_token
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
import json
from django.views.decorators.csrf import csrf_exempt


# importing request 
from user_management.request.signup import SignupRequest
from user_management.request.user import UserUpdateRequest

# importing common 
from KSURL.common.response import CommonResponse
from KSURL.error_capture import capture_error

# importing service
from user_management.service.user import UserService

@api_view(["GET"])
@csrf_exempt
def generate_csrfToken(request):
    token = get_token(request)
    return CommonResponse(message="success",data={"csrf_token":token},status_code=201).get_response()



@api_view(["POST"])
@csrf_exempt
@capture_error
def signup_view(request):
    request_data = SignupRequest(request.data)
    serice = UserService()
    service_response = serice.create(request_data)
    return CommonResponse(message="Signup successful",data=service_response.get_obj(),status_code=201).get_response()



@api_view(["POST"])
@csrf_exempt
def login_view(request):
    request_data = request.data
    email = request_data.get("email")
    password = request_data.get("password")
    user = authenticate(email=email, password=password)
    if user is not None:
        login(request,user)
        return CommonResponse(message="Login successful",status_code=200).get_response()
    else:
        return CommonResponse(message="invalid credentials",status_code=403).get_response()

@api_view(["POST"])
@csrf_exempt
def update(request):
    request_data = UserUpdateRequest(request.data)
    serice = UserService()
    service_response = serice.update(request,request_data)
    return CommonResponse(message="Updated successfully",data=service_response.get_obj(),status_code=200).get_response()


@api_view(['POST'])
@csrf_exempt
def logout_view(request):
    logout(request)
    return CommonResponse(message="Logout successful",status_code=200).get_response()

        