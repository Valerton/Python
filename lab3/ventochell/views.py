from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from . models import Event, Profile

### Pages
def start(request):
	return render(request, 'ventochell_app/startpage.html')

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			profile = Profile(name='',surname='',username = username,location='',age='',img='http://www.tsu.ru/upload/medialibrary/679/net-foto-m.png',hobbies='')
			profile.save()
			return redirect('index')
	else:
	    form = UserCreationForm()
	context = {'form':form}
	return render(request,'registration/register.html',context)

def index(request):
	events = Event.objects.all()
	context = {'events':events}
	return render(request, 'ventochell_app/index.html',context)

def myevents(request):
	events = Event.objects.all()
	context = {'events':events}
	return render(request, 'ventochell_app/myevents.html',context)

def createEvent(request):
	events = Event.objects.all()
	context = {'events':events}
	return render(request, 'ventochell_app/createEvent.html',context)

def profile(request):
	profiles = Profile.objects.all()
	context = {'profiles':profiles}
	return render(request, 'ventochell_app/profile.html',context)

### Profile
def editprofile(request, id):
	profile = Profile.objects.get(id=id)
	context = {"profile":profile}
	return render(request, 'ventochell_app/editprofile.html',context)

def updateprofile(request, id):
	profile = Profile.objects.get(id=id)
	profile.name = request.POST['name']
	profile.surname = request.POST['surname']
	profile.location = request.POST['location']
	profile.age = request.POST['age']
	profile.img = request.POST['img']
	profile.hobbies = request.POST['hobbies']
	profile.save()
	return redirect('profile')

### Event
def add(request):
    print(request.POST)
    event = Event(name = request.POST['name'],location = request.POST['location'],date = request.POST['date'],img = request.POST['img'],description = request.POST['description'],creator = request.user.username)
    event.save()
    return redirect('index')

def edit(request, id):
	event = Event.objects.get(id=id)
	context = {"event":event}
	return render(request, 'ventochell_app/edit.html',context)

def update(request, id):
	event = Event.objects.get(id=id)
	event.name = request.POST['name']
	event.location = request.POST['location']
	event.date = request.POST['location']
	event.img = request.POST['img']
	event.description = request.POST['description']
	event.save()
	return redirect('index')

def destroy(request, id):
	event = Event.objects.get(id=id)
	event.delete()
	return redirect('myevents')