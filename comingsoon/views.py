from django.shortcuts import render

# Create your views here.


def coming(request):
    ''' render comingsoon page'''
    return render(request, 'index.html')
