from django.urls import path
from . import views


urlpatterns = [
    path('front', views.front,name = 'front'),
    path('register',views.register,name = 'register'), 
    path('registers',views.registers,name ='registers'),   
    path('registerss',views.registerss,name = 'registerss'),
    path('totals',views.totals,name = 'totals'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name="logout"),
]
