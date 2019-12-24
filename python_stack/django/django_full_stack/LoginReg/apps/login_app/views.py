from django.shortcuts import render, redirect
from django.contrib import messages

from apps.login_app.models import *
import bcrypt

def index(request): 
    return render(request, 'login_app/index.html')

def register(request):
    error = User.objects.basic_validator(request.POST)

    if len(error) > 0:
        for key, value in error.items():
            messages.error(request, value)
        print("DATA HAD ERRORS")
        return redirect('/')
    else:
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        pw_confirm = request.POST["pw_confirm"]
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        User.objects.create(first_name = first_name, last_name = last_name, email = email, password = hashed_pw)
        print("creatingUSER")
        logged_user = User.objects.get(email=request.POST['email'])
        request.session['user.id'] = logged_user.id
        request.session['logged_in'] = True
        return redirect('/success')

def login(request):
    user = User.objects.filter(email=request.POST['email']) 
    if user:
        logged_user = user[0]

        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            # request.session['user_id'] = User.objects.get(email = request.POST['email']).id
            request.session['logged_in'] = True
            request.session['first_name'] = logged_user.first_name
            return redirect('/success')
        else:
            messages.error(request, "Password is not correct")
            return redirect("/")

    messages.error(request, "The email was not found")
    return redirect("/")


# def login(request):
#     errors = {}
#     if request.method == "POST":
#         other_user = User.objects.filter(email = request.POST['email'])
#         try:
#             this_user = other_user[0]
#             print(this_user.first_name)
#             if request.POST['password'] == this_user.password:
#                 request.session['first_name'] = this_user.first_name
#                 user = User.objects.get(email = request.POST["email"]).id
#                 print(user)
#                 request.session['user_id'] = user
#                 return redirect("/success")
#             errors["password"] = "You forgot your password"
#         except:
#             errors['email']= "No user exists here, go ahead and register"
#     if len(errors)>0:
#         for key, value in errors.items():
#             messages.error(request, value)
#     return redirect("/")



    # error = User.objects.login_Validator(request.POST)
    # if error:
    #     for key, value in error. items():
    #         messages.error(request, value)
    #         return redirect('/')
    # else:
    #     user = User.objects.get(email = request.POST['email'])
    #     request.session['user.id'] = user.id
    #     return redirect('/success')

def success(request):
    if 'logged_in' in request.session:
        return render( request, "login_app/success.html")
    else:
        messages.error(request,"User not recognized")
        return redirect("/")

def logout(request): 
    request.session.clear()
    return redirect('/')