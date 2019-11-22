from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import doctor
from .models import event
from .models import patient
from .models import regis
from .models import ngo


# Create your views here.

def doc_login(request):
    return render(request,'camp/doc_login.html')

def org_login(request):
    return render(request,'camp/org_login.html')

def doc_sign(request):
    return render(request,'camp/doc_sign.html')

def org_sign(request):
    return render(request,'camp/org_sign.html')
    
def doc_logged(request):
	username = request.POST.get('username')
	pswrd = request.POST.get('password')
	try:
		doc = doctor.objects.filter(username = username)
		d = doc[0]
	except IndexError:
		return render(request, 'camp/doc_login.html')
	if pswrd == d.password :
		request.session['did'] = d.id
		#session.set..("name",username)
		return HttpResponseRedirect('/camp/register')
	else :
		return render(request, 'camp/doc_login.html')

def register(request):
	id = request.session['did']
	doc = doctor.objects.filter(id = id)
	D = {'doc':doc[0]}
	return render(request,'camp/register.html',D)


def org_logged(request):
	username = request.POST.get('username')
	pswrd = request.POST.get('password')
	try:
		ng = ngo.objects.filter(username = username)
		n = ng[0]
	except IndexError:
		return render(request, 'camp/org_login.html')
	if pswrd == n.password :
		request.session['nid'] = n.id
		#session.set..("name",username)
		return HttpResponseRedirect('/camp/nregister')
	else :
		return render(request, 'camp/org_login.html')



def nregister(request):
	id = request.session['nid']
	ng = ngo.objects.filter(id = id)
	N= {'ng':ng[0]}
	return render(request,'camp/nregister.html',N)


def doc_signed(request):
	name = request.POST.get('yourname')
	username = request.POST.get('username')
	pswrd = request.POST.get('password')
	phone = request.POST.get('phone')
	email = request.POST.get('email')
	city = request.POST.get('city')
	specialization = request.POST.get('specialization')
	doc = doctor(name=name,username = username ,password = pswrd, phone = phone, special = specialization , city = city, email = email )
	doc.save()
	request.session['did'] = doc.id
	return HttpResponseRedirect('/camp/register')


def org_signed(request):
	name = request.POST.get('NGOname')
	username = request.POST.get('username')
	pswrd = request.POST.get('password')
	phone = request.POST.get('phone')
	email = request.POST.get('email')
	text=request.POST.get('textbox')
	ng = ngo(name=name,username = username ,password = pswrd, phone = phone,email=email,text=text )
	ng.save()
	request.session['nid'] = ng.id
	return HttpResponseRedirect('/camp/nregister')

