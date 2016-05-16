from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from . import views 

urlpatterns = [
     url(r'^base/$', views.index, name='index'),
     url(r'^$', views.home, name='home'),
     url(r'^contact/$', views.contact, name='contact'),
     url(r'^about/$', views.about, name='about'),
     url(r'^dnarna/$', views.dnarna, name='dnarna'),
     url(r'^query/$', views.dnarna, name='query'),

]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#to use these urls 
           # <li><a href="{% url 'home' %}">Home</a></li>
           #  <li><a href="{% url 'about' %}">About</a></li>
           #  <li><a href="{% url 'contact' %}">Contact</a></li>