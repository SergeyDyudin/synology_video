from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('record/<slug:slug>', views.index, name='record'),
]
