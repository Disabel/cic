from django.conf.urls import patterns, include, url
from django.conf import settings
from django.http import HttpResponse
from sitemaps import StaticViewSitemap, EventSitemap, ConferenciasSitemap, CursosSitemap
from django.conf.urls.i18n import i18n_patterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
sitemaps = {
	'pages': StaticViewSitemap,
	'EventSitemap': EventSitemap,
	'ConferenciasSitemap': ConferenciasSitemap,
	'CursosSitemap': CursosSitemap,
}

urlpatterns = patterns(
	'',
	# Examples:
	# url(r'^$', 'basicoDuranjo.views.home', name='home'),
	url(r'^', include('cic.apps.homepage.urls')),
	url(r'^agenda/', include('cic.apps.calendarium.urls')),
	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	#url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
	#Google Web master Tool
	(r'^googlec34fe789f50fc843\.html$', lambda r: HttpResponse("google-site-verification: googlec34fe789f50fc843.html", mimetype="text/plain")),
	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/password_reset/$', 'django.contrib.auth.views.password_reset', name='admin_password_reset'),
	(r'^admin/password_reset/done/$', 'django.contrib.auth.views.password_reset_done'),
	(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
	(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
	#Zinnia Blog
	url(r'^blog/', include('zinnia.urls', namespace='zinnia')),
	url(r'^', include('zinnia.urls.capabilities')),
	url(r'^search/', include('zinnia.urls.search')),
	url(r'^sitemap/', include('zinnia.urls.sitemap')),
	url(r'^trackback/', include('zinnia.urls.trackback')),
	url(r'^blog/tags/', include('zinnia.urls.tags')),
	url(r'^blog/feeds/', include('zinnia.urls.feeds')),
	url(r'^blog/authors/', include('zinnia.urls.authors')),
	url(r'^blog/categories/', include('zinnia.urls.categories')),
	url(r'^comments/', include('django.contrib.comments.urls')),
	#url(r'^comments/', include('django_comments.urls')),
	url(r'^blog/', include('zinnia.urls.entries')),
	url(r'^blog/', include('zinnia.urls.archives')),
	url(r'^blog/', include('zinnia.urls.shortlink')),
	url(r'^blog/', include('zinnia.urls.quick_entry')),
	url(r'^blog/comments/', include('zinnia.urls.comments')),
	(r'^i18n/', include('django.conf.urls.i18n')),
	(r'^tinymce/', include('tinymce.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns(
		'',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	)
