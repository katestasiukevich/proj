from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    content = {'title': "Home",
               'page_content': 'ti pidor'}

    return render(request, 'main/index.html', content)

def about(request):
    return HttpResponse("About page")
