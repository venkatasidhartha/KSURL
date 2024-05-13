from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from user_management import models
from user_management.response.signup import SignupResponse


class UserService:

    def read(self,request):
        pass

    def update(self,request,req_obj):
        user_obj = get_user_model().objects.get(pk=request.user.id)
        if req_obj.get_name():
            user_obj.name = req_obj.get_name()
        if req_obj.get_password():
            user_obj.password = make_password(req_obj.get_password())
        user_obj.save()
        response = SignupResponse()
        response.set_name(user_obj.name)
        response.set_email(user_obj.email)
        return response

    def create(self,req_obj):
        User = get_user_model()
        user = User.objects.create(email=req_obj.get_email(),name=req_obj.get_name())
        user.password = make_password(req_obj.get_password())
        user.save()
        response = SignupResponse()
        response.set_email(user.email)
        return response