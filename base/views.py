from django.shortcuts import render
from .models import Room


# rooms = [
#    {'id': 1, 'name': 'let`s learn python'},
#    {'id': 2, 'name': 'design with me'},
#    {'id': 3, 'name': 'frontend developers'},
# ]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    contex = {'room': room}
    return render(request, 'base/room.html', contex)
