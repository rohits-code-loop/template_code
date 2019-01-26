from django.shortcuts import render
from .models import ProfilePhotos
from django.http import HttpResponse
# Create your views here.
def file(request):
	if(request.method=='POST'):
		q = ProfilePhotos()
		q.url=request.FILES.get('file')
		q.save()
	
	return render(request,'file.html',None)
def showdb(request):
	q = ProfilePhotos.objects.all()
	return HttpResponse(q[1].url.name)