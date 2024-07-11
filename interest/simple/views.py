from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(Request):
	temp=loader.get_template("home.html")
	return(HttpResponse(temp.render()))

def si2(Request):
	temp=loader.get_template("si2.html")
	return(HttpResponse(temp.render({},Request)))

def calc(Request):
	p=int(Request.POST["p"])
	r=int(Request.POST["r"])
	t=int(Request.POST["t"])
	if "interest" in Request.POST:
		if "simple_interest"==Request.POST["interest"]:
			si=(p*r*t)/100
			s=("the simple interst is :"+str(si))
		elif "compound_interest"==Request.POST["interest"]:
			a=p*(1+(r/100))**t
			ci=a-p
			s=("the compound interest is :"+str(ci))
	return(HttpResponse(s))