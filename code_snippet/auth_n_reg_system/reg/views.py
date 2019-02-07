from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.models import User

def user_registeration(request):
    if (request.method == 'GET'):
        form = UserCreationForm()
        return render(request,'registeration.html',{'form':form})
    elif (request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            uid = request.POST['username']
            user = User.objects.get(username = uid)
            login(request,user)
            return redirect('/home')

        else:
            form = UserCreationForm(request.POST)
            return render(request,'registeration.html',{'form':form})