from django.conf.urls import patterns, url
#from .views import application

urlpatterns = patterns(
	'cic.apps.homepage.views',
	url(r'^$', 'index', name="homepageindex"),
	url(r'^aboutus/$', 'aboutus', name="homepageaboutus"),
	#url(r'^directors/$', 'directors', name="homepagedirectors"),
	#url(r'^application/$', application.as_view(), name="homapageapplication"),
)
