#-*- encoding: utf-8 -*-
from django.contrib import sitemaps
from django.core.urlresolvers import reverse
from cic.apps.calendarium.models import Event
from cic.apps.homepage.models import conferenciaslista, cursoslista


class StaticViewSitemap(sitemaps.Sitemap):
	priority = 0.5
	changefreq = 'daily'

	def items(self):
		return [
				'homepageindex',
				'homepageaboutus',
				'aboutdirectorio',
				'aboutpaises',
				'aboutcodigo',
				'homepagerecursos',
				'homepagecertificaciones',
				'certificaciondetalle',
				'homepageregistro',
				'registrocic',
				'registroinvitado',
				'homepageservicios',
				'cursodetalle',
				'serviciosconferencias',
				'conferenciasdetalle',
				'serviciosasesorias',
				'homepagecontact',
				# colocar los nombre de las url en este lugar. ejemplo: 'homepageworks'
				]

	def location(self, item):
		return reverse(item)


class EventSitemap(sitemaps.Sitemap):
	changefreq = 'monthly'
	priority = 0.5

	def items(self):
		return Event.objects.all()


class ConferenciasSitemap(sitemaps.Sitemap):
	changefreq = 'monthly'
	priority = 0.6

	def items(self):
		return conferenciaslista.objects.all()


class CursosSitemap(sitemaps.Sitemap):
	changefreq = 'monthly'
	priority = 0.6

	def items(self):
		return cursoslista.objects.all()
