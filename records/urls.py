from django.conf.urls.static import static
from django.urls import path

from synology_video import settings
from . import views

app_name = 'records'  # Для использования view с одним именем разных приложений(в ссылках писать {% urls records:home%})
urlpatterns = [
    path('', views.RecordsList.as_view(), name='home'),
    path('insert', views.insert_in_base, name='insert'),
    path('video/', views.VideoList.as_view(), name='video'),
    path('files/', views.FilesList.as_view(), name='files'),
    path('record/<slug:slug>/', views.RecordDetail.as_view(), name='record'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
