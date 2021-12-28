from django.http import HttpResponse, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from django.urls import reverse
from .models import Character
from .serializers import CharacterSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def signin(request):
    u = request.POST.get('username')
    p = request.POST.get('password')
    # if username is null check for JSON POST data
    if (u == None):
        j = JSONParser()
        data = j.parse(request)
        u = data['username']
        p = data['password']
    user = authenticate(request, username=u, password=p)
    if user is not None:
        login(request, user)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=200)

def LogoutPage(request):
    logout(request)
    return HttpResponse(status=200)

def register(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    # if username is null check for JSON POST data
    if (username == None):
        j = JSONParser()
        data = j.parse(request)
        username = data['username']
        password = data['password']
        email = data['email']
    u = User.objects.create_user(username,email,password)
    u.save()
    return HttpResponse(status=200)

def character_generate(request, name):
    character = Character()
    character.roll(name)
    if request.user.is_authenticated:
        character.user = request.user
    character.save()
    serializer = CharacterSerializer(character)
    return JsonResponse(serializer.data, status=201)

def character_list(request):
    if request.method == 'GET':
        characters = Character.objects.all()
        serializer = CharacterSerializer(characters, many=True)
        return JsonResponse(serializer.data, safe=False)

def my_character_list(request):
    if request.method == 'GET':
        characters = Character.objects.filter(user = request.user.id)
        serializer = CharacterSerializer(characters, many=True)
        return JsonResponse(serializer.data, safe=False)

def character_detail(request, pk):
    try:
        character = Character.objects.get(pk=pk)
    except Character.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CharacterSerializer(character)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        if request.user.is_authenticated and request.user == character.user:
            data = JSONParser().parse(request)
            c_role = data['c_role']
            s = data['strength']
            d = data['dexterity']
            co = data['constitution']
            i = data['intelligence']
            w = data['wisdom']
            ch = data['charisma']
            character.finalize(c_role, s, d, co, i, w, ch)
            character.save()
            serializer = CharacterSerializer(character)
            return JsonResponse(serializer.data)
        return HttpResponse(status=404)

    elif request.method == 'DELETE':
        if request.user.is_authenticated and request.user == character.user:
            character.delete()
        return HttpResponse(status=204)

#if client has a valid session, return their username
def get_username(request):
    data = {'username' : ''}
    if request.user.is_authenticated:
        data = {'username' : request.user.username}
    return JsonResponse(data)

def vue_test(request):
    return render(request, 'whitebox/vue_test.html')
