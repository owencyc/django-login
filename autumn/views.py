from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


def hello(request):
    return JsonResponse({'status': 1})