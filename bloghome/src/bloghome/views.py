from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html', {'about':about})

def contactRedirect(request):
    return render(request, 'contact_message_sent.html', {'contactRedirect':contactRedirect})
