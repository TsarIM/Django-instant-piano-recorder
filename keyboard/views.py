from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Song
import json
from django.shortcuts import render, get_object_or_404

def song_detail(request, id):
    song = get_object_or_404(Song, id=id)
    song_notes_json = json.dumps(song.notes,cls=DjangoJSONEncoder)
    return render(request, 'keyboard/index.html', {'song': song, 'song_notes_json': song_notes_json})

def index(request):
    return render(request,'keyboard/index.html')

@csrf_exempt
def create_song(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        song = Song.objects.create(notes=data['songNotes'])
        return JsonResponse({'id':song.id})
