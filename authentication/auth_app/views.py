from django.shortcuts import render
from auth_app.forms import UserForm,UserProfileInfoFrom

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def index(request):

    return render(request, 'auth_app/index.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered =False

    if request.method == "POST":

        user_form = UserForm (data= request.POST)
        profile_form = UserProfileInfoFrom(data= request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES ['profile_pic']

            profile.save()
            lamine=None


            registered = True

        else: print(user_form.errors, profile_form.errors)

    else:
        user_form=UserForm()
        profile_form=UserProfileInfoFrom()
    return render(request,'auth_app/registration.html',
                        {'user_form': user_form,
                        'profile_form': profile_form,
                        'registered':registered})

def user_login(request):
    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')

        user=authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('account not active')
        else:
            print("someone tried to log in and failed")
            print ('username : {} and password {}'.format(username,password))
            return HttpResponse('Invalid login details supplied')
    else: render(request,'auth_app/;login.html',{})
