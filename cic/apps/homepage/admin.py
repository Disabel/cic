# -*- coding: utf-8 -*-
from django.contrib import admin
from actions import export_as_csv_action
from .models import CorreoBoletin, miembros, textosInicio,sliderInicio,videosInicio, quienesSomos, conferenciaslista, quienesSomosOtros, seccionesQuienesSomos, servicios, cursoslista,certificacionesLista, paisesCic,certificacionesIntroduccion, representantesInternacionales

class emailsAdmin(admin.ModelAdmin):
	"""Admin del modelo de correos de suscripcion"""
	list_display = ('correo','nombre')
	search_fields= ['correo','nombre']
	actions = [export_as_csv_action("CSV Export", fields=['correo','nombre'])]

class certificacionesListaAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('titulo',)}
	list_display = ('titulo', 'cuerpo_general', 'tipo', 'imagen', 'slug')
	list_display_links = ('titulo',)
	search_fields = ['titulo', 'slug', 'cuerpo_general', 'tipo']

class conferenciaslistaAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slugconf': ('titulo',)}
	list_display = ('titulo', 'cuerpo_general', 'imagen', 'slugconf')
	list_display_links = ('titulo',)
	search_fields = ['titulo', 'slugconf', 'cuerpo_general']

class cursoslistaAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slugcurso': ('titulo',)}
	list_display = ('titulo', 'cuerpo_general', 'imagen', 'slugcurso')
	list_display_links = ('titulo',)
	search_fields = ['titulo', 'slugcurso', 'cuerpo_general']

admin.site.register(textosInicio)
admin.site.register(sliderInicio)
admin.site.register(quienesSomos)
admin.site.register(miembros)
admin.site.register(paisesCic)
admin.site.register(representantesInternacionales)
admin.site.register(certificacionesIntroduccion)
admin.site.register(certificacionesLista,certificacionesListaAdmin)
admin.site.register(servicios)
admin.site.register(cursoslista,cursoslistaAdmin)
admin.site.register(quienesSomosOtros)
admin.site.register(seccionesQuienesSomos)
admin.site.register(conferenciaslista,conferenciaslistaAdmin)
admin.site.register(videosInicio)
admin.site.register(CorreoBoletin, emailsAdmin)