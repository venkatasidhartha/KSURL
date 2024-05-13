from django.urls import path
from url_shortner import views

urlpatterns = [
    path('short_it',views.create_url),
    path('<str:uuid>',views.redirect_url),
]