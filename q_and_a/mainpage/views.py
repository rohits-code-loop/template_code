from django.shortcuts import render , redirect
from django.http import HttpResponse
from mainpage.forms import *
# Create your views here.
def homepage(request):
	if (request.method == 'GET'):
		return render(request,'home.html',None)
	else:
		choice = request.POST.get('dropdown')
		if (choice == 'technology'):
			data = {
						'q0':"What is the full form of OS in computer science",
						'ans0':[
								(1, 'Operating System'),
								(2, 'Operating Server'),
								(3, 'Operating Service')
								],
						
						'q1':"What is the full form of SMPS in computer science" ,
						'ans1':[
								('1', 'System Mode Power supply'),
								('2', 'Switch Mode Power supply'),
								('3', 'Simple Mail Protocol Standard')
								] ,
						
						'q2':"What is TCP computer science" ,
						'ans2':[
								('1', 'Transmission Control Power'),
								('2', 'Transmission Control Protocol'),
								('3', 'Transfer Control Protocol')
								]
					}
			request.session['data'] = data
			request.session['index'] = 0
			request.session['total'] = 2
			
			form = func(request, data['q0'] ,list(data['ans0']))
			dictonary = {'ques':data['q0'],'ans':data['ans0'] , 'index':1 , 'finish':0 , 'form':form}
			return	render(request,'q_and_a.html',dictonary)
		elif (choice == 'political'):
			pass
		elif (choice == 'maths'):
			pass
		

def prev_question(request):
	index = request.session.get('index') 
	if (index>0):
		print(index,"before")
		index= index-1
		print(index)
		request.session['index'] = index
		data = request.session.get('data')
		ques = data['q'+str(index)]
		answer = data['ans'+str(index)]
		form = func(request, ques ,list(answer))
		dictonary = { 'index':index+1 , 'ques':ques ,'ans':answer ,'finish':0 ,'form':form}
		
	else :
		request.session['index'] = 0
		return redirect('home/')
	return render(request,'q_and_a.html' , dictonary)

finish = 0
def next_question(request):
	global finish
	index = request.session.get('index') + 1
	total = request.session.get('total')
	if (index<total):
		data 		= 		request.session.get('data')
		ques 		=	 	data['q'+str(index)]
		answer 		= 		data['ans'+str(index)]
		form = func(request, ques,answer)
		dictonary 	= 		{ 'index':index+1 , 'ques':ques ,'ans':answer,'finish':0 ,'form':form}
		request.session['index'] = index
	elif(index==total):
		index 		=	total
		data  		= 	request.session.get('data')
		ques 		= 	data['q'+str(index)]
		answer  	= 	data['ans'+str(index)]
		form = func(request, ques ,answer)
		dictonary  	= 	{ 'index':index+1 , 'ques':ques ,'ans':answer , 'finish':1,'form':form}
		request.session['index'] = index
	elif(index>total):
		
		return HttpResponse("<h1>Game has Ended</h1")
	else:
		return redirect('home/')
	return render(request,'q_and_a.html' , dictonary)

