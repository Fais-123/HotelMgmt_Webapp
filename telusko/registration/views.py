from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect("/")


def login(request):
    if request.method == "POST":
        username = request.POST['Username']
        password = request.POST['Password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid user')
            return redirect("login")
    else:
        return render(request,'login.html')



def register(request):
    if request.method == "POST":
        first_name = request.POST['First name']
        last_name = request.POST['last name']
        username = request.POST['Username']
        email = request.POST['email']
        Password1 = request.POST['Password1']
        Password2 = request.POST['Password2']

        if(Password1 == Password2):
            if(User.objects.filter(username=username).exists()):
                messages.info(request,'username taken')
                return redirect('register')

            elif(User.objects.filter(email = email).exists()):
                messages.info(request,'email taken')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=Password1, email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,'user created')
                return redirect("login")

        else:
                messages.info(request,'password not match')
        return redirect("/")
    else:
        return render(request,'register.html')