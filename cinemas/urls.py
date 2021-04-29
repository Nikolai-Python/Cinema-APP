from django.urls import path

from . import views

urlpatterns = [
        path('', views.CinemaListView.as_view(), name='cinema_list'),
        path('new/', views.CinemaCreateView.as_view(), name='cinema_new'),
        path('<int:pk>/',
                views.CinemaDetailView.as_view(), name='cinema_detail'),
        path('<int:pk>/edit/',
                views.CinemaUpdateView.as_view(), name='cinema_edit'),
        path('<int:pk>/delete/',
                views.CinemaDeleteView.as_view(), name='cinema_delete'),
        path('seans/',
                views.SeansCreateView.as_view(), name='seans_new'),
        path('<int:pk>/seans/edit/',
                views.SeansUpdateView.as_view(), name='seans_edit'),
        path('<int:pk>/seans/delete/',
                views.SeansDeleteView.as_view(), name='seans_delete'),
]