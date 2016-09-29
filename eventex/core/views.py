from django.shortcuts import render


def home(request):
    speakers = [
        {'nome': 'Grace Hopper', 'photo': 'http://hbn.link/hopper-pic'},
        {'nome': 'Alan Turing', 'photo': 'http://hbn.link/turing-pic'},

    ]
    return render(request, 'index.html', {'speakers': speakers})
