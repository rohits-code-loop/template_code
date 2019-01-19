from django.shortcuts import render ,redirect
from admin_rohit.models import *
from django.http import HttpResponse 
from mainpage.views import *
# Create your views here.
def adding_data(request):
	if (request.method == "GET"):
		return render(request,'add_data.html')
	else:
		content_obj = content()
		content_obj.content_type	 = 	request.POST.get("drop_down")
		content_obj.text_content 		 =  request.POST.get("main_content")
		content_obj.save()
		return redirect('/home')