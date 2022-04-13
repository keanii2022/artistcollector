from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('about/', views.about, name = "about"),    
    path('artists/', views.artists_index, name = "index"),
    path('artists/<int:artist_id>', views.artists_detail, name='detail'),
    path('artists/create/', views.ArtistCreate.as_view(), name='artists_create'),
    path('artists/<int:pk>/update/', views.ArtistUpdate.as_view(), name='artists_update'),
    path('artists/<int:pk>/delete/', views.ArtistDelete.as_view(), name='artists_delete'),
    path('artists/<int:artist_id>/add_shows/', views.add_shows, name='add_shows')

]  