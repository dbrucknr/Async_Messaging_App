from django.shortcuts import render

def index(request):
    return render(request, 'messaging_app/index.html', {})

def room(request, room_name):
    return render(request, 'messaging_app/room.html', {
        'room_name': room_name
    })