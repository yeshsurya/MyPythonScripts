from django.conf.urls import url 
from tutorial import views

app_name = 'tutorial'
urlpatterns= [
	url(r'^$', views.home, name='home'),
  # Explicit home ('/tutorial/home/')
	url(r'^home/$', views.home, name='home'),
]