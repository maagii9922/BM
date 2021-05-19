from django.http import HttpResponse
from .models import Hereglegch



def home(request):
    return HttpResponse("hello")