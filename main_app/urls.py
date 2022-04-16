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
    path('artists/<int:artist_id>/add_shows/', views.add_shows, name='add_shows'),
    path('venue/', views.VenueList.as_view(), name='venue_index'),
    path('venue/<int:pk>/', views.VenueDetail.as_view(), name='venue_detail'),
    path('venue/create/', views.VenueCreate.as_view(), name='venue_create'),
    path('venue/<int:pk>/update', views.VenueUpdate.as_view(), name='venue_update'),
    path('venue/<int:pk>/delete', views.VenueDelete.as_view(), name='venue_delete'),
    path('artists/<int:artist_id>/assoc_venue/<int:venue_id>', views.assoc_venue, name='assoc_venue')
]  