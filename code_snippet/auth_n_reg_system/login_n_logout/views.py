from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate ,login , logout
from django.contrib.auth.models import User


def userlogin(request):
    if (request.method == 'POST'):
        u_id               =   request.POST['username']
        password           =   request.POST['password']
        psuedo_user        =   authenticate(request,username= u_id, password = password)
        if (psuedo_user):
            login(request,psuedo_user)
            data = {'name':psuedo_user.username}
            return  render(request,'home.html',data)
        else:
            data = {'err':'login again'}
            return render(request,'login.html',data)
    else:
        if(request.user.is_authenticated):
            data = {'name':request.user.username}
            return  redirect('/home')
        else: 
            return render(request,'login.html')

#------------------------------------------------------------------------------------------------------------        
def userlogout(request):
    data = {'msg':'logged out successfully'}
    logout(request)
    return redirect('/home')


#-------------------------------------------------------------------------------------------------------------
def homepage(request):
    if (request.user.is_authenticated):
        data = {'name':request.user.username}
    else:
        data = {'msg':'anonymous user'}
    if (request.method =='GET'):
        return render(request,'home.html',data)


