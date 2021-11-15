from django.urls import path, include
from . import views

urlpatterns = [
    path('api', views.homepage, views.create),
    path('api/rapat', views.rapat_list.as_view()),
    path('api/absen', views.absensi_list.as_view()),
    path('api/asisten', views.asisten_list.as_view()),
    path('api/notulensi', views.notulensi_list.as_view()),
    path('api/detail-hadir/<int:pk>', views.hadir_list.as_view()),
    path('api/detail-absen/<int:pk>', views.tidak_hadir_list.as_view()),
    path('api/asisten/<str:nim>', views.detail_asisten.as_view()),
]