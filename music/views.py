from django.http import HttpResponse
from .models import Album, Song
from django.http import Http404
#from django.template import loader
from django.shortcuts import render,get_object_or_404


def index(request):
    all_albums=Album.objects.all()
        #template=loader.get_template('music/index.html')
    #return HttpResponse(template.render(context,request))
    return render(request, 'music/index.html', {'all_albums':all_albums})


def details(request,album_id):
    #return HttpResponse("<h2> THE DETAILS FOR ALBUM ID:"+str(album_id)+" </h2>")
    '''try:
        album=Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exists")'''

    album=get_object_or_404(Album,pk=album_id)
    return render(request,'music/detail.html',{'album':album})

def favorite(request,album_id):
    album=get_object_or_404(Album, pk=album_id)
    try:
        selected_song=album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request,'music/detail.html',{
            'album':album,
            'error_message': "you did not select a valid song",
        })
    else:
        selected_song.is_favorite=True
        selected_song.save()
        return render(request, 'music/detail.html',{'album':album})
