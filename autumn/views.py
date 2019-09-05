import json

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from autumn import models
from django.core import serializers


def ctxWraped(ctx):
    response = JsonResponse(ctx)
    response["Access-Control-Allow-Headers"] = "content-type"
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    return response



def hello(request):
    return JsonResponse({'status': 1})


def addVerse(request):
    json_result = json.loads(request.body)
    obj = models.Verse()
    obj.user_no = 'qiu'
    obj.author=json_result.get('author')
    obj.content = json_result.get('content')
    obj.save()  # 修改单条数据
    return JsonResponse({'status': 1})


def addSkill(request):
    json_result = json.loads(request.body)
    obj = models.Skill()
    obj.user_no = 'qiu'
    obj.name=json_result.get('name')
    obj.score = json_result.get('score')
    obj.save()  # 修改单条数据
    return JsonResponse({'status': 1})


def addIntro(request):
    json_result = json.loads(request.body)
    obj = models.Intro.objects.get(user_no='qiu')
    obj.work = json_result.get('work')
    obj.word=json_result.get('word')
    obj.save()  # 修改单条数据
    return JsonResponse({'status': 1})

def addIntro2(request):
    json_result = json.loads(request.body)
    obj = models.Intro.objects.get(user_no='qiu')
    obj.name = json_result.get('name')
    obj.p_word=json_result.get('p_word')
    obj.city = json_result.get('city')
    obj.state = json_result.get('state')
    obj.street = json_result.get('street')
    obj.save()  # 修改单条数据
    return JsonResponse({'status': 1})


def getData(request):
    user = models.Intro.objects.filter(user_no='qiu')
    json_data = serializers.serialize('json', user)
    json_user = json.loads(json_data)

    skills = models.Skill.objects.filter(user_no='qiu')
    json_data = serializers.serialize('json', skills)
    json_skills = json.loads(json_data)

    verses = models.Verse.objects.filter(user_no='qiu')
    json_data = serializers.serialize('json', verses)
    json_verses = json.loads(json_data)

    return JsonResponse({'user': json_user, 'skills': json_skills, 'verses': json_verses})
