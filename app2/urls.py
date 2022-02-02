from django.urls import path
from . import views

app_name='app2'

urlpatterns = [
   path('adminmain/',views.Admin,name='adminmain'),
   path('adminlogin',views.Admlog,name='adminlog'),
   path('adminhome',views.Admhome,name='adminhome'),
   path('adminupload',views.Admup,name='adminup'),
   path('usersprofile',views.Userpro,name='userpro'),
]