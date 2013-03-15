from django.conf.urls import patterns, include, url
from blogs.views import mainpage,newpost,createuser,login,logout,logincheck,guestpage

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',(r'^$', mainpage),
	(r'^visit$', guestpage),
	(r'^post/new', newpost),
    (r'^account/create$', createuser),
    (r'^account/login$',  login),
    (r'^account/logout$', logout),
	(r'^account/login/check$',logincheck),
 
)
