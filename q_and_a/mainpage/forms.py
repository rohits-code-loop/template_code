from django import forms

'''
def func(request,answer,question):
	class answer_form(forms.Form):
		name = forms.CharField(max_length=20)
		ans = forms.CharField(label = question , widget= forms.RadioSelect(choices = answer))
	form = answer_form()
	return form
'''
ques = " "
ans = " "

def func(request,question,answer):
	global ques , ans
	ques = question
	ans = answer
	

	class data_form(forms.Form):
		answer 	= 	forms.CharField(label = "",widget = forms.RadioSelect(choices = ans))

	form = data_form(initial = {'answer':1})
	return form