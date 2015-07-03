# -*- coding: utf-8 -*-
from django.contrib import admin
#from django.contrib.contenttypes import generic
from .models import textosInicio,sliderInicio,videosInicio, quienesSomos, conferenciaslista, quienesSomosOtros, seccionesQuienesSomos, servicios, cursoslista, miembros,certificacionesLista, paisesCic,certificacionesIntroduccion, representantesInternacionales

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