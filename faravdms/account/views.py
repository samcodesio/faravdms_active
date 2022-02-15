from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # User is authenticated
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request, "invalid credentials")
            print("Error")
            return redirect("login")

    else:
        return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return redirect('login')


# ADD USERS
def add_users(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_users')
    else:
        form = CreateUserForm()
        
    return render(request,'add_users.html',{'form':form})