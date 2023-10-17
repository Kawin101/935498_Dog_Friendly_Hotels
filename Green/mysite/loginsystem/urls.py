from django.urls import path
from .views import index, register

urlpatterns = [
    # /user/register
    path('member', index, name="member"),
    path('register/add', register, name="addUser"),
]

