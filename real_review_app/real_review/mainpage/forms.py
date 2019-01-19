from django import forms

class signupform(forms.Form):
	usrID 		= forms.CharField(max_length=30)
	#name 		= forms.CharField(max_length=30,required = False)
	#age 		= forms.CharField(max_length=10,required = False)
	email 		= forms.CharField(max_length =30)
	password 	= forms.CharField(max_length = 30)

class loginform(forms.Form):
	userid = forms.CharField(max_length=30)
	password = forms.CharField(max_length=30)