from django.shortcuts import render, redirect
from django.contrib import messages	
from . models import *
import bcrypt

# Create your views here.
def index(request):
	return render(request,'index.html')

def register(request):
	errorsFromValidator = User.objects.UserValidator(request.POST)
	if len(errorsFromValidator)>0:
		for key, value in errorsFromValidator.items():   messages.error(request, value)
		return redirect('/')
	encryptedPW = bcrypt.hashpw(request.POST['formPassword'].encode(), bcrypt.gensalt()).decode()
	newUser = User.objects.create(firstName = request.POST['formFirstName'], lastName = request.POST['formLastName'], email = request.POST['formEmail'], password = encryptedPW)
	request.session['loggedInUserID'] = newUser.id
	return redirect ('/')

def login(request):
	errorsFromValidator = User.objects.loginValidator(request.POST)
	if len(errorsFromValidator)>0:
		for key, value in errorsFromValidator.items():   messages.error(request, value)
		return redirect('/')
	matchingEmail = User.objects.filter(email = request.POST['emailLogin'])
	request.session['loggedInUserID'] = matchingEmail[0].id
	return redirect('/wall')

def logout(request):
	request.session.clear()    
	return redirect('/')

def viewWall (request):
	if 'loggedInUserID' not in request.session:
		messages.error(request, 'You must be logged in')
		return redirect('/')
	latest = Message.objects.all().order_by('-id')
	context = {
		'loggedInUser': User.objects.get(id = request.session['loggedInUserID']),
		'allUsers' : User.objects.all(), 
		'allMessage' : latest, 
		'allComment' : Comment.objects.all(),

	  }
	return render(request, 'wall.html', context)

def addMessage(request):
	Message.objects.create(message=request.POST["postMessage"], user = User.objects.get(id = request.session['loggedInUserID']))
	return redirect('/wall')

def likeMessage(request, messageID):
	this_user = User.objects.get(id=request.session['loggedInUserID'])
	this_message = Message.objects.get(id=messageID)
	
	this_message.users_who_like.add(this_user)
	
	return redirect('/wall')

def dislikeMessage(request, messageID):
	this_user = User.objects.get(id=request.session['loggedInUserID'])
	this_message = Message.objects.get(id=messageID)
	
	this_message.users_who_dislike.add(this_user)
	
	return redirect('/wall')

def addComment(request, messageID):
	Comment.objects.create(comment = request.POST['postComment'], poster = User.objects.get( id=request.session['loggedInUserID']), wallMessage = Message.objects.get(id = messageID))
	return redirect('/wall')

def deleteMessage(request, messageID):
	b = Message.objects.get(id = messageID)
	b.delete()
	return redirect('/wall')