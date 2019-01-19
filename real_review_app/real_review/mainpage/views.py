from django.shortcuts import render
from django.http import HttpResponse 
from mainpage.forms import *
from mainpage.models import *
import hashlib as hasher 		# to get the real time time form the operating system
import re
from admin_rohit.models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def homepage(request):
	content_obj = content.objects.filter()
	content_alias  = []
	data = {}
	for obj in content_obj:
		text = str(obj.text_content)+' - '+str(obj.content_type)
		content_alias.append(text)
	return render(request,'home.html',{'contents':content_obj})



#u_id and Pass bhanuisbhanu bhanuis

count = 0
def loginpage(request):
	global count 											# using global variable to count the number of logins but it will not work 
															#because it will stop the user if he has given wrong details more than 5 in his entire past which we never want
	
	if(request.method == 'GET'):
		form = loginform() 									# object of the login form which is passed to a html page 
		return render(request,'login.html',{'form':form})
	elif(request.method == 'POST'):
		uid = request.POST.get('userid') 					# fetching userid given by the user in the login form
		password = request.POST.get('password')
		encoded_password = hasher.sha256(password.encode()) 
		hashed_password = encoded_password.hexdigest()
		users = user.objects.filter() 						# getting all the data present in the database
		flag = 0
		for u in users:
			if (u.usrID == uid and u.password == hashed_password):	#checking the login creditionals 
				flag = 1
				count = 0
		if (flag == 1):
			return HttpResponse('successfully logged in ') 	# if flag is 1 then it means that every detail has been matched 
		else: 
			count+=0										#This counter does not works , here i am trying to count the numberof false logins
			if (count<=5):									# if they exceed more than 5 then they should be blocked for some amount of the time
				form = loginform()
				data = {'form':form , 'message':"wrong creditional login again"}
				return render(request,'login.html',data)
			else:
				return HttpResponse("Limit exceeded	")



def checking_for_special_charcter (userid):
    flag = 0
    for charater in userid :
        if (re.search(r'\w' , charater)):
            flag = 1
        else:
            flag = 0
            break
            
    if flag == 1 :
        return 1
    else :
        return 0


def signuppage(request):


	if (request.method=='GET'):
		form = signupform()			# creating a form object 
		return render(request,"signup.html",{'form':form})	

	else : 
		usr = user()
		form = signupform()	
		u_id  = request.POST.get('usrID')				# Getting id from the user which is in the form
		all_id_s = user.objects.values_list('usrID') 	# Getting userid from the database for checking for previous userids
		checker = checking_for_special_charcter(u_id)
		if checker == 1:								# if checker is 1 then it means that there are no special charcters in the user id note (underscor)
		
			for users in all_id_s:
				print(users[0])
				if (users[0] == u_id):
					data = {
							'form':form,
							'message':'invalid userid'
						}
					return render(request,'login.html',data)
				else :
					usr = user()
					usr.usrID 		=   request.POST.get('usrID')	
					#usr.name 		=	request.POST.get('name')
					usr.email 		=	request.POST.get('email')
					#usr.age 		= 	request.POST.get('age')
					password 		= 	request.POST.get('password')
					encoded_password=	hasher.sha256(password.encode())		#encoding the password
					hashed_password = 	encoded_password.hexdigest()			#hashing the password
					usr.password 	= 	hashed_password							#saving the hashed password
					usr.save()
					return HttpResponse(user.objects.values_list())




		else:
			form = signupform()
			return render(request,'signup.html',{'message':"Special charater are there so try again" , "form":form} )
																				#if checker is anything else then there is atleast 1 special charcter 

def forgot_uid(request):
	
	return render(request,'forgot.html',None)


@csrf_exempt
def verifyuserid(request):
	if(request.method=='POST'):
		requestdata=str(request.body).split("=")[1]
		usrID=requestdata[:len(requestdata)-1]
		try:
			u=user.objects.get(usrID=usrID)
			return HttpResponse('True')
		except:
			return HttpResponse('False')

	return HttpResponse('False')