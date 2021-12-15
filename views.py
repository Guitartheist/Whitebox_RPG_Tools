from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse
from .models import Character
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    character_list = Character.objects.all()
    context = {'character_list': character_list}
    return render(request, 'whitebox/index.html', context)

def ViewAll(request):
    character_list = Character.objects.all()
    context = {'character_list': character_list}
    return render(request, 'whitebox/ViewAll.html', context)

def ViewDetail(request,character_id):
    try:
        character = Character.objects.get(pk=character_id)
    except Character.DoesNotExist:
        raise Http404("Character does not exist")
    return render (request, 'whitebox/ViewDetail.html', {'character': character})

def ViewMine(request):
    character_list = Character.objects.filter(user = request.user.id)
    context = {'character_list': character_list}
    return render(request, 'whitebox/ViewAll.html', context)

def GenerateForm(request):
    context = {}
    return render(request, 'whitebox/generate.html', context)

def generate(request):
    c = Character()
    if request.user.is_authenticated:
        c.user = request.user
    c.roll(request.POST['name'])
    c.save()
    return ViewDetail(request, c.id)

def LoginForm(request):
    context = {}
    return render(request, 'whitebox/login.html', context)

def signin(request):
    u = request.POST['username']
    p = request.POST['password']
    user = authenticate(request, username=u, password=p)
    if user is not None:
        login(request, user)
        return ViewAll(request)
    else:
        context = {}
        return render(request, 'whitebox/login.html', context)

def LogoutPage(request):
    logout(request)
    return index(request)

def RegisterForm(request):
    context = {}
    return render(request, 'whitebox/register.html', context)

def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    u = User.objects.create_user(username,email,password)
    u.save()
    return LoginForm(request)

def FinalizeForm(request, character_id):
    try:
        character = Character.objects.get(pk=character_id)
    except Character.DoesNotExist:
        raise Http404("Character does not exist")
    if (request.user.is_authenticated and character.user == request.user and not character.finalized):
        return render(request, 'whitebox/FinalizeForm.html', {'character': character})
    else:
        return render (request, 'whitebox/ViewDetail.html', {'character': character})

def finalize(request, character_id):
    try:
        character = Character.objects.get(pk=character_id)
    except Character.DoesNotExist:
        raise Http404("Character does not exist")
    # character role, strength, dexterity, intelligence, constitution, intelligence, wisdom, charisma
    c_role = int(request.POST['c_role'])
    s = int(request.POST['s'])
    d = int(request.POST['d'])
    co = int(request.POST['co'])
    i = int(request.POST['i'])
    w = int(request.POST['w'])
    ch = int(request.POST['ch'])
    character.finalize(c_role, s, d, co, i, w, ch)
    character.save()
    return render(request, 'whitebox/ViewDetail.html', {'character': character})

def delete(request, character_id):
    try:
        character = Character.objects.get(pk=character_id)
    except Character.DoesNotExist:
        raise Http404("Character does not exist")
    if request.user.is_authenticated and request.user == character.user:
        Character.objects.filter(pk=character_id).delete()
    character_list = Character.objects.all()
    context = {'character_list': character_list}
    return render(request, 'whitebox/ViewAll.html', context)
