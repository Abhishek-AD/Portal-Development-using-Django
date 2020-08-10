from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from basic_app.models import ResourcePerson,MemberInfo,Event,Expenses

# for login and signup page
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
#send Email
from django.core.mail import send_mail
# from django.conf import settings
import datetime

# Create your views here.




def thanks(request):
	return render(request,'basic_app/thanks.html')

def index(request):
	return render(request,'basic_app/index.html')

def expenses(request):

	item_list = Event.objects.order_by('eventID')

	# expense_list = Expenses.objects.all()
	if request.method == 'POST':
		query = request.POST.get('event')
		expense_list = Expenses.objects.filter(expenditure__topic= query)
		expense_dict = {'expense_records':expense_list, 'item_records':item_list, 'expenditure_topic':query}
		return render(request,'basic_app/expenses.html',context = expense_dict)

	else:
		expense_dict = {'item_records':item_list}
		return render(request,'basic_app/expenses.html',context = expense_dict)

def contact_info(request):
	member_list = MemberInfo.objects.order_by('rank')
	member_dict = {'member_records':member_list}
	return render(request,'basic_app/contact_info.html',context= member_dict)

def room_booking(request):

	if request.method == 'POST':
		subject = 'BITS Embryo - Request for Room Booking '
		event_info = request.POST.get('event')
		time_info = request.POST.get('time')
		room_info = request.POST.get('room')
		date_info = request.POST.get('date')
		from_email = 'xyz@gmail.com'

		if event_info and room_info and time_info and date_info:
			message = 'Dear Sir\n\nPlease confirm room availability for the following Embryo Event\n' + '\nEvent:   ' + event_info + '\nTime:    ' + time_info + '\nRoom:   ' + room_info + '\nDate:    ' + date_info + '\n\nThank You'
			send_mail(subject,message,from_email,['abhishekad.atg@gmail.com'])
			return HttpResponseRedirect('/basic_app/thanks/')
	else:
		return render(request,'basic_app/room_booking.html')

def lectures(request):
	if request.method == 'POST':
		query = request.POST.get('yearstart')
		# lecture_list = Event.objects.filter(date__contains=query)
		
		
		if query == 'All':
			lecture_list = Event.objects.all()
		else:
			query2 = request.POST.get('year')
			q1=query+'-1-1'
			q2=query2+'-12-31'
			lecture_list = Event.objects.filter(date__range=(q1,q2))

		

	else:
		lecture_list = Event.objects.all()

	lecture_dict = {'lecture_records':lecture_list }
	return render(request,'basic_app/lectures.html',context = lecture_dict)

def index(request):
	q1 = Event.objects.order_by('eventID')
	index_list = q1.filter(date__gte=datetime.date.today())
	index_dict = {'index_records':index_list}
	return render(request,'basic_app/index.html',context= index_dict)

def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			 #  log the user in
			login(request, user)
			return render(request,'basic_app/index.html')
	else:
		form = UserCreationForm()
	return render(request, 'basic_app/signup.html', { 'form': form })

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			# log the user in
			user = form.get_user()
			login(request, user)
			q1 = Event.objects.order_by('eventID')
			index_list = q1.filter(date__gte=datetime.date.today())
			index_dict = {'index_records':index_list}
			return render(request,'basic_app/index.html',context= index_dict)
	else:
		form = AuthenticationForm()
	return render(request, 'basic_app/login.html', { 'form': form })


def logout_view(request):
	logout(request)
	q1 = Event.objects.order_by('eventID')
	index_list = q1.filter(date__gte=datetime.date.today())
	index_dict = {'index_records':index_list}
	return render(request,'basic_app/index.html',context= index_dict)

def event(request,eventID):
	event_list = Event.objects.filter(eventID=eventID)
	event_dict = {'event_records':event_list}
	return render(request,'basic_app/event.html',context = event_dict)
