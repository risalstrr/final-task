from distutils.util import split_quoted
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def home(request):
    return render(request, "authentication/index_anonymous.html")
    # return render(request, "authentication/signin.html"

def user(request):
    return render(request, "authentication/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")

        count = 0

        if username.isdigit():
            for i in username[0:3]:
                count += int(i)
            print(count)
            slicing = username[3:5]
            slicing1 = int(slicing)
            print(slicing1)
            try: 
                if (slicing1 == count):
                    myUser = User.objects.create_user(username, email, password1)
                    myUser.first_name = fname
                    myUser.last_name = lname
                    myUser.save()

                    messages.success(request, "Success Created your account!")
                    return redirect("signin")
            except:
                messages.error(request, "User already exist. Make sure the ID is not registered yet")
                return redirect("signup")
        else:
            messages.error(request, "An ID should consist of a 5 digits number from 0-9. Two last digits is the sum of three first digits")
            return redirect("signup")
    return render(request, "authentication/signup.html")

def signin(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password1")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html",{"fname":fname})
        else:
            messages.error(request, "You are wrong")
            return redirect('home')
    return render(request, 'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "You're logout")
    return redirect("home")