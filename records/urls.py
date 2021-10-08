from django.urls import path
from . import views

app_name = 'records'  # Для использования view с одним именем разных приложений(в ссылках писать {% urls records:home%})
urlpatterns = [
    path('', views.RecordsList.as_view(), name='home'),
    path('insert', views.insert_in_base, name='insert'),
    path('record/<slug:slug>/', views.RecordDetail.as_view(), name='record'),
]
