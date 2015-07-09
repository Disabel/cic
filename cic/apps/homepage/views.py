#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from .forms import *
from .models import *
from django.utils.timezone import now, timedelta
from zinnia.models import Category
from django.template import RequestContext
from django.core.mail import send_mail
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from cic.apps.calendarium.models import Event
import datetime
import nltk


def index(request):	
#	entradas = Entry.objects.filter(status=2).order_by('-creation_date')
#	entradas = entradas.exclude(start_publication__gte=datetime.date.today())
#	entradas = entradas[:3]
#	titulos = []
#	for ent in entradas:
#		quitar_html = nltk.clean_html(ent.content) 
#		ent.content =  quitar_html[:200]
#		titulos.append(ent.title)	
	#eventos del calendario
	if Event.objects.get_occurrences(now(), now() + timedelta(days=356), None):
		nextEvent = True
	else:
		nextEvent = False
	textoshome = textosInicio.objects.get(pk=1)
	imgslider = sliderInicio.objects.all()
	videosinicio = videosInicio.objects.all()
	ctx = {'textoshome':textoshome,'imgslider':imgslider,'videosinicio': videosinicio,'nextEvent': nextEvent,}	
	return render_to_response('homepage/index.html', ctx, context_instance=RequestContext(request))
def recursos(request):
	categorias = Category.objects.all()
	ctx = {'categorias':categorias}	
	return render_to_response('homepage/recursos.html', ctx, context_instance=RequestContext(request))

def aboutus(request):
	title = "Quienes Somos"
	try:
		quienestext = quienesSomos.objects.get(pk=1)
	except Exception:
		quienestext = None
	try:
		directores = miembros.objects.filter(tipo_de_miembro='directivo')	
	except Exception:
		directores = None		
	try:
		representantes_internacionales = representantesInternacionales.objects.all()	
	except Exception:
		directores = None	
	try:
		otrostextos = quienesSomosOtros.objects.get(pk=1)	
	except Exception:
		otrostextos = None			
	ctx = {'title':title, 'quienesSomos':quienestext, 'directores':directores,'otrostextos':otrostextos, 'representantes_internacionales':representantes_internacionales}	
	return render_to_response('homepage/quienessomos.html',ctx, context_instance=RequestContext(request))

def serviciosCursos(request):
	try:
		servicios_textos = servicios.objects.get(pk=1)
	except Exception:
		servicios_textos = None	
	try:
		cursos_lista = cursoslista.objects.all()
	except Exception:
		cursos_lista = None		
	ctx = {'servicios_textos':servicios_textos, 'cursoscursos':cursos_lista,}	
	return render_to_response('homepage/servicios.html',ctx, context_instance=RequestContext(request))

def cursodetalle(request, slugcurso):
	curso = get_object_or_404(cursoslista, slugcurso=slugcurso)
	if request.method == 'POST':
		form = solicitudForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'[CONTACTO WEB] - Solicitud de Información sobre Curso: %s ' % (curso.titulo)
			content = u'Persona interesada en el curso: %s \n Nombre y Apellido: %s \n Pais: %s \n Código de área: %s \n Teléfono Móvil: %s \n Teléfono Fijo: %s \n Correo Electrónico Principal: %s \n Correo Electrónico Alterno: %s \n Nombre de la Empresa: %s \n Mensaje: %s \n' % (curso.titulo, cd['nombre_apellido'], cd['pais_origen'], cd['codigo_area'], cd['telefono_movil'], cd['telefono_fijo'], cd['correo_principal'], cd['correo_alterno'], cd['nombre_empresa'], cd['mensaje'])
			#send_mail(asunto, content, 'info@inverfanca.com', ['info@inverfanca.com'])						
	else:
		form = solicitudForm()		
	ctx = {'curso':curso,'form':form}
	return render_to_response('homepage/cursodetalle.html', ctx, context_instance=RequestContext(request))


def directorio(request):
	try:
		miembroslista = miembros.objects.all()
	except Exception:
		miembroslista = None	
	ctx = {'miembros':miembroslista,}
	return render_to_response('homepage/directorio.html',ctx, context_instance=RequestContext(request))

def paises(request):
	title = "directoriocic"
	try:
		quienestextos = seccionesQuienesSomos.objects.get(pk=1)
	except Exception:
		quienestextos = None
	try:
		paisesdelacic = paisesCic.objects.all()	
	except Exception:
		paisesdelacic = None	
	ctx = {'title':title,'quienesSomos':quienestextos,'paisescic':paisesdelacic}			
	return render_to_response('homepage/paises.html', ctx, context_instance=RequestContext(request))

def codigoetica(request):
	try:
		quienestextos = seccionesQuienesSomos.objects.get(pk=1)
	except Exception:
		quienestextos = None	
	ctx = {'quienesSomos':quienestextos}
	return render_to_response('homepage/codigoetica.html',ctx, context_instance=RequestContext(request))

def certificaciones(request):
	try:
		certificacionesintro = certificacionesIntroduccion.objects.get(pk=1)	
	except Exception:
		certificacionesintro = None
	try:
		certificaciones_lista = certificacionesLista.objects.filter(tipo="certificacion")
	except Exception:
		certificaciones_lista = None
	try:
		especializaciones_lista = certificacionesLista.objects.filter(tipo="especializacion")
	except Exception:
		especializaciones_lista = None			
	ctx = {'certificaciones':certificacionesintro,'certificaciones_lista':certificaciones_lista, 'especializaciones_lista':especializaciones_lista}			
	return render_to_response('homepage/certificaciones.html', ctx, context_instance=RequestContext(request))

def certificaciondetalle(request, slug):
	certificacion = get_object_or_404(certificacionesLista, slug=slug)
	if request.method == 'POST':
		form = solicitudForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'[CONTACTO WEB] - Solicitud de Información sobre Certificacion; %s ' % (certificacion.titulo)
			content = u'Persona interesada en la certificacion: %s \n Nombre y Apellido: %s \n Pais: %s \n Código de área: %s \n Teléfono Móvil: %s \n Teléfono Fijo: %s \n Correo Electrónico Principal: %s \n Correo Electrónico Alterno: %s \n Nombre de la Empresa: %s \n Mensaje: %s \n' % (certificacion.titulo, cd['nombre_apellido'], cd['pais_origen'], cd['codigo_area'], cd['telefono_movil'], cd['telefono_fijo'], cd['correo_principal'], cd['correo_alterno'], cd['nombre_empresa'], cd['mensaje'])
			#send_mail(asunto, content, 'info@inverfanca.com', ['info@inverfanca.com'])			
	else:
		form = solicitudForm()		
	ctx = {'certificacion':certificacion,'form':form}
	return render_to_response('homepage/certificaciondetalle.html', ctx, context_instance=RequestContext(request))

def conferencias(request):
	try:
		serviciostxt = servicios.objects.get(pk=1)
	except Exception:
		serviciostxt = None	
	print serviciostxt.conferencias
	try:
		conferenciaslist= conferenciaslista.objects.all()
	except Exception:
		conferenciaslist = None			
	ctx = {'servi':serviciostxt,'conferenciaslist':conferenciaslist}
	return render_to_response('homepage/conferencias.html', ctx, context_instance=RequestContext(request))

def conferenciasdetalle(request, slugconf):
	conferencia = get_object_or_404(conferenciaslista, slugconf=slugconf)
	if request.method == 'POST':
		form = solicitudForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'[CONTACTO WEB] - Solicitud de Información sobre Conferencia: %s ' % (conferencia.titulo)
			content = u'Persona interesada en la conferencia: %s \n Nombre y Apellido: %s \n Pais: %s \n Código de área: %s \n Teléfono Móvil: %s \n Teléfono Fijo: %s \n Correo Electrónico Principal: %s \n Correo Electrónico Alterno: %s \n Nombre de la Empresa: %s \n Mensaje: %s \n' % (conferencia.titulo, cd['nombre_apellido'], cd['pais_origen'], cd['codigo_area'], cd['telefono_movil'], cd['telefono_fijo'], cd['correo_principal'], cd['correo_alterno'], cd['nombre_empresa'], cd['mensaje'])
			#send_mail(asunto, content, 'info@inverfanca.com', ['info@inverfanca.com'])									
	else:
		form = solicitudForm()			
	ctx = {'conferencia':conferencia,'form':form}
	return render_to_response('homepage/conferenciadetalle.html', ctx, context_instance=RequestContext(request))


def asesorias(request):
	try:
		serviciostextos = servicios.objects.get(pk=1)
	except Exception:
		serviciostextos = None	
	ctx = {'serviciostextos':serviciostextos}
	return render_to_response('homepage/asesorias.html', ctx, context_instance=RequestContext(request))

def registro(request):
	return render_to_response('homepage/registro.html', context_instance=RequestContext(request))

def registrocic(request):
	success = False
	if request.method == 'POST':
		form = MemberForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			form.save()
	else:
		form = MemberForm()
	ctx = {'form': form, 'success': success}	
	return render_to_response('homepage/registrocic.html',ctx, context_instance=RequestContext(request))

def registroinvitado(request):
	success = False
	if request.method == 'POST':
		form = MiembroInvitadoForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			form.save()
	else:
		form = MiembroInvitadoForm()
	ctx = {'form': form, 'success': success}	
	return render_to_response('homepage/registroinvitado.html',ctx, context_instance=RequestContext(request))
 	
def contact(request):
	success = False
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'[CONTACTO WEB] - Formulario de Contacto por: %s ' % (cd['nombre_apellido'])
			content = u'Nombre y Apellido: %s \n Pais: %s \n Código de área: %s \n Teléfono Móvil: %s \n Teléfono Fijo: %s \n Correo Electrónico Principal: %s \n Correo Electrónico Alterno: %s \n Nombre de la Empresa: %s \n Mensaje: %s \n' % (cd['nombre_apellido'], cd['pais_origen'], cd['codigo_area'], cd['telefono_movil'], cd['telefono_fijo'], cd['correo_principal'], cd['correo_alterno'], cd['nombre_empresa'], cd['mensaje'])
		#	send_mail(asunto, content, 'info@inverfanca.com', ['info@inverfanca.com'])
	else:
		form = contactForm()
	ctx = {'form': form, 'success': success}
	return render_to_response('homepage/contacto.html', ctx, context_instance=RequestContext(request))
