from django.shortcuts import render, redirect

from Posts.forms import PostCreationForm
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

def sign_up(request):
    form = UserRegistrationForm()
    if request.method == "POST":
       form = UserRegistrationForm(request.POST)
       
       if form.is_valid():
           form.save()
           
           messages.success(request,"User Created Sucessfully")
           
           return redirect('login')
    context ={
        'form': form
    }
    return render(request, 'users/signup.html', context)


def login_user(request):
    form = LoginForm()
    
    if request.method =='POST':
        username =request.POST["username"]
        password =request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user) 
            return redirect('post_home')
            
    context ={"form": form}
    return render(request, 'users/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('post_home')







'''Basic way to create a signup form in django'''
# def sign_up(request):
#     form = UserRegistrationForm()
#     if request.method == "POST":
#         username = request.POST["username"]
#         email = request.POST["email"]
#         password = request.POST["password"]
#         confirm = request.POST["confirm"]
        
#         if password == confirm:
#             new_user = User.objects.create_user(
#                 username=username,
#                 email=email,
#             )
#             new_user.set_password(password)
            
#             new_user.save()
            
#             return redirect('post_home')
    
#     context ={
#         'form': form
#     }
#     return render(request, 'users/signup.html', context)



