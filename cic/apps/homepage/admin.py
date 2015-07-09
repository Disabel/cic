# -*- coding: utf-8 -*-
from django.contrib import admin
from actions import export_as_csv_action
#from django.contrib.contenttypes import generic
from .models import CorreoBoletin, miembros, textosInicio,sliderInicio,videosInicio, quienesSomos, conferenciaslista, quienesSomosOtros, seccionesQuienesSomos, servicios, cursoslista,certificacionesLista, paisesCic,certificacionesIntroduccion, representantesInternacionales

class emailsAdmin(admin.ModelAdmin):
	"""Admin del modelo de correos de suscripcion"""
	list_display = ('correo','nombre')
	search_fields= ['correo','nombre']
	actions = [export_as_csv_action("CSV Export", fields=['correo','nombre'])]

admin.site.register(textosInicio)
admin.site.register(sliderInicio)
admin.site.register(quienesSomos)
admin.site.register(miembros)
admin.site.register(paisesCic)
admin.site.register(representantesInternacionales)
admin.site.register(certificacionesIntroduccion)
admin.site.register(certificacionesLista)
admin.site.register(servicios)
admin.site.register(cursoslista)
admin.site.register(quienesSomosOtros)
admin.site.register(seccionesQuienesSomos)
admin.site.register(conferenciaslista)
admin.site.register(videosInicio)
admin.site.register(CorreoBoletin, emailsAdmin)