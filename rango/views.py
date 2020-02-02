from django.shortcuts import render

from django.shortcuts import HttpResponse

def index(request):
    # constructs a dictionary to pass the template engine as its context.
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    # returns a rendered response to the client
    # first parameter is the template that are going to use

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'authormessage': 'This tutorial has been put together by Hugh'}
    return render(request, 'rango/about.html', context=context_dict)
