from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import NewUserForm


def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('account')
		else:
			messages.success(request, ("There was an error logging in!!!  Please try again!!!"))
			return redirect('login')


	else:
		return render(request, 'authenticate/login.html', {})



def register_user(request):
	if request.method == 'POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration Successful")
			return redirect('home')
		messages.error(request, "Unsuccessful registration. Invalid information")
	form = NewUserForm()
	return render(request, 'authenticate/register.html', {'register_form': form})


def log_out_user(request):
	logout(request)
	return redirect('home')
