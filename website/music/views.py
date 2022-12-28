# for 404 error
#from django.shortcuts import get_object_or_404
from .models import Album, Song
# to work with tamplates aka html and css code 
# instead of using loader and shit, we using render (some other things are also auto-init)
from django.shortcuts import get_object_or_404, render

def index(request):
    all_albums = Album.objects.all()
    # information that your template needs
    context = {"all_albums" : all_albums}
    return render(request, "music/index.html", context)

def detail(request, album_id):
    #raise error if album = not exist 
    album = get_object_or_404(Album, pk=album_id)
    return render(request, "music/detail.html", {"album" : album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk = request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request,"music/detail.html",{
            'album':album,
            'error_message': "You did not select a valid song",
            })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, "music/detail.html", {"album" : album})
