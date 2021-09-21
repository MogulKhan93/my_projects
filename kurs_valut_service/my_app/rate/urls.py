from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', views.main_page, name='main'),
    path('rate-now/', RateList.as_view(), name='rate-list'),
    path('registration/', Registrator.as_view(), name='registration'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
