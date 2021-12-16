from django.urls import path
from . import views

app_name='app1'

urlpatterns = [
    path('',views.Hey,name='hello'),
    path('log',views.Log,name='loginpage'),
    path('sign',views.Sign,name='signup')
]