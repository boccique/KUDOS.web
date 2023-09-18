from django.shortcuts import render
from .models import Room
from .forms import RoomForm


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


def createRoom(request):
    form = RoomForm()
    context = {'form': form}
    return render(request, 'base/room_form.html', context)