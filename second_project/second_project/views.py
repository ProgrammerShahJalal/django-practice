from django.http import HttpResponse

def home(request):
    return HttpResponse("<h2> This is my home page</h2>")
