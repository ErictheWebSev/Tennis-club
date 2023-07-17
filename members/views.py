from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings

def members(request):
	mymembers = Member.objects.all().values()
	template = loader.get_template('all_members.html')
	context = {
		'mymembers': mymembers,
	}
	return HttpResponse(template.render(context, request))



def details(request, id):
	mymember = Member.objects.get(id=id)
	template = loader.get_template('details.html')
	context = {
		'mymember': mymember,
	}
	return HttpResponse(template.render(context, request))



def main(request):
	template = loader.get_template('main.html')
	return HttpResponse(template.render())


def testing(request):
	mydata = Member.objects.all().values()
	template = loader.get_template('template.html')
	context = {
		'mymembers': mydata,
	}
	return HttpResponse(template.render(context, request))



def about(request):
	template = loader.get_template('about.html')
	return HttpResponse(template.render())


@csrf_exempt
def form_submit(request):
	if request.method == 'POST':
		name = request.POST['name']
		lastname = request.POST['lastname']
		phone = request.POST['phone']
		date = request.POST['date']
		
		member = Member(name=name, lastname=lastname, phone=phone, joined_date=date)
		member.save()
		
		
		return render(request, 'success.html')
		
	return render(request, 'form.html')


def contact(request):
	if request.method == 'POST':
		subject = request.POST.get('subject')
		message = request.POST.get('message')
		recipient_list = [request.POST.get('recipient')]
		email_from = request.POST.get('email')
		
		send_mail(subject, message, email_from, recipient_list, fail_silently=False)
        
		
		return render(request, 'success1.html')
	return render(request, 'contact.html')
