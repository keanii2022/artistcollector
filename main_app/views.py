from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Artist, Venue
from .forms import ShowsForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def artists_index(request):
    artists = Artist.objects.all()
    return render(request, 'artists/index.html', { 'artists': artists })

def artists_detail(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    id_list = artist.venue.all().values_list('id')
    venues_artist_doesnt_have = Venue.objects.exclude(id__in=id_list)
    shows_form = ShowsForm()
    return render(request, 'artists/detail.html', {'artist': artist, 'shows_form': shows_form,
        'venues': venues_artist_doesnt_have
    })

def assoc_venue(request, artist_id, venue_id):
    Artist.objects.get(id=artist_id).venue.add(venue_id)
    return redirect('detail', artist_id=artist_id)

class ArtistCreate(CreateView):
    model = Artist
    fields = ['name', 'age', 'genre', 'location']
    success_url = '/artists/'

class ArtistUpdate(UpdateView):
    model = Artist
    fields = ['age','genre','location']

class ArtistDelete(DeleteView):
    model = Artist
    success_url = '/artists/'


def add_shows(request, artist_id):
    form = ShowsForm(request.POST)
    if form.is_valid():
        new_shows = form.save(commit=False)
        new_shows.artist_id = artist_id
        new_shows.save()
        return redirect('detail', artist_id=artist_id)

class VenueList(ListView):
    model = Venue

class VenueDetail(DetailView):
    model = Venue

class VenueCreate(CreateView):
    model = Venue
    fields = '__all__'

class VenueUpdate(UpdateView):
    model = Venue
    fields = '__all__'

class VenueDelete(DeleteView):
    model = Venue
    success_url = '/venue/'


