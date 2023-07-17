from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path('', views.main, name='main'),
	path('members/', views.members, name='members'),
	path('members/details/<int:id>', views.details, name='details'),
	path('testing/', views.testing, name='testing'),
	path('about/', views.about, name='about'),
	path('form/', views.form_submit, name='form_submit'),
	path('contact/', views.contact, name='contact'),
] 