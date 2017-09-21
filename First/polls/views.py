from django.http import HttpResponse


def index(request):
    return HttpResponse("This page is in the middle of a quantum blur!")

