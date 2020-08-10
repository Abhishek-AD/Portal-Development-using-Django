from django.conf.urls import url
from django.shortcuts import render,redirect
from basic_app import views

app_name = 'basic_app'

urlpatterns= [
	url(r'^contact_info/$',views.contact_info,name='contact_info'),
	url(r'^lectures/$',views.lectures,name='lectures'),
	url(r'^room_booking/$',views.room_booking,name='room_booking'),
	url(r'^thanks/$',views.thanks,name='thanks'),
	url(r'^login_view/$',views.login_view,name='login'),
	url(r'^signup_view/$',views.signup_view,name='signup'),
	url(r'^logout/$', views.logout_view, name="logout"),
	url(r'^expenses/$', views.expenses, name="expenses"),
	url(r'^event/(?P<eventID>\d+)/$', views.event, name="event"),

]
