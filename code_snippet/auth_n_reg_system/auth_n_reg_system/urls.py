
from django.contrib import admin
from django.urls import path
from login_n_logout import views
from reg.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.userlogin , name = 'login'),
    path('logout/',views.userlogout),
    path('home/',views.homepage ),
    path('register/',user_registeration)
]
