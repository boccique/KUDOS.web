from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'let`s learn python'},
    {'id': 2, 'name': 'design with me'},
    {'id': 3, 'name': 'frontend developers'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    contex = {'room': room}
    return render(request, 'base/room.html', contex)
