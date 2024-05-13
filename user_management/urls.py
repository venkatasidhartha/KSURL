from django.urls import path,include
from user_management import views

urlpatterns = [
    path('get_csrftoken',views.generate_csrfToken),
    path('signup',views.signup_view),
    path('login',views.login_view),
    path('logout',views.logout_view),
    path('update',views.update)

] 
