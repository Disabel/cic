#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from .forms import *
from .models import *
from zinnia.models import Category
from django.template import RequestContext
from django.core.mail import send_mail
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
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
	textoshome = textosInicio.objects.get(pk=1)
	imgslider = sliderInicio.objects.all()
	videosinicio = videosInicio.objects.all()
	ctx = {'textoshome':textoshome,'imgslider':imgslider,'videosinicio': videosinicio}	
	return render_to_response('homepage/index.html', ctx, context_instance=RequestContext(request))
def recursos(request):
	categorias = Category.objects.all()
	ctx = {'categorias':categorias}	
	return render_to_response('homepage/recursos.html', ctx, context_instance=RequestContext(request))

def aboutus(request):
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
	ctx = {'quienesSomos':quienestext, 'directores':directores,'otrostextos':otrostextos, 'representantes_internacionales':representantes_internacionales}	
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
	if request.method == 'POST':
		form = solicitudForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
	else:
		form = solicitudForm()		
	curso = get_object_or_404(cursoslista, slugcurso=slugcurso)
	ctx = {'curso':curso,'form':form}
	return render_to_response('homepage/cursodetalle.html', ctx, context_instance=RequestContext(request))


def directorio(request):
	return render_to_response('homepage/directorio.html', context_instance=RequestContext(request))

def paises(request):
	try:
		quienestextos = seccionesQuienesSomos.objects.get(pk=1)
	except Exception:
		quienestextos = None
	try:
		paisesdelacic = paisesCic.objects.all()	
	except Exception:
		paisesdelacic = None	
	ctx = {'quienesSomos':quienestextos,'paisescic':paisesdelacic}			
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
	if request.method == 'POST':
		form = solicitudForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
	else:
		form = solicitudForm()		
	certificacion = get_object_or_404(certificacionesLista, slug=slug)
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
	if request.method == 'POST':
		form = solicitudForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
	else:
		form = solicitudForm()			
	conferencia = get_object_or_404(conferenciaslista, slugconf=slugconf)
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
		#	cd = form.cleaned_data
		#	asunto = u'[CONTACTO WEB] Por: %s email: %s ' % (cd['nombre'], cd['email'])
		#	content = u'Email contacto: %s \nAsunto: %s \nTelefono: %s \nDescripcion: %s' % (cd['email'], asunto, cd['telefono'], cd['texto'])
		#	send_mail(asunto, content, 'info@inverfanca.com', ['info@inverfanca.com'])
	else:
		form = contactForm()
	ctx = {'form': form, 'success': success}
	return render_to_response('homepage/contacto.html', ctx, context_instance=RequestContext(request))
