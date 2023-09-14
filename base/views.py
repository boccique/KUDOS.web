from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'let`s learn python'},
    {'id': 1, 'name': 'design with me'},
    {'id': 1, 'name': 'frontend developers'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request):
    return render(request, 'base/room.html')
