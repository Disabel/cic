from django.conf.urls import patterns, url
#from .views import application

urlpatterns = patterns(
	'cic.apps.homepage.views',
	url(r'^$', 'index', name="homepageindex"),
	url(r'^quienes-somos/$', 'aboutus', name="homepageaboutus"),
	url(r'^quienes-somos/directorio$', 'directorio', name="aboutdirectorio"),
	url(r'^quienes-somos/paises$', 'paises', name="aboutpaises"),
	url(r'^quienes-somos/codigo-etica$', 'codigoetica', name="aboutcodigo"),
	url(r'^recursos-informativos/$', 'recursos', name="homepagerecursos"),
	url(r'^certificaciones/$', 'certificaciones', name="homepagecertificaciones"),
	url(r'^certificaciones/(?P<slug>[-\w,]+)/$', 'certificaciondetalle', name="certificaciondetalle"),	
	url(r'^registro/$', 'registro', name="homepageregistro"),
	url(r'^registro/coachcic$', 'registrocic', name="registrocic"),
	url(r'^registro/coachinvitado$', 'registroinvitado', name="registroinvitado"),
	url(r'^servicios/$', 'serviciosCursos', name="homepageservicios"),
	url(r'^servicios/cursos/(?P<slugcurso>[-\w,]+)/$', 'cursodetalle', name="cursodetalle"),	
	url(r'^servicios/conferencias$', 'conferencias', name="serviciosconferencias"),
	url(r'^servicios/conferencias/(?P<slugconf>[-\w,]+)/$', 'conferenciasdetalle', name="conferenciasdetalle"),
	url(r'^servicios/asesorias$', 'asesorias', name="serviciosasesorias"),
	url(r'^contacto/$', 'contact', name="homepagecontact"),
	)
