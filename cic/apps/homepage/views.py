#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from .forms import *
from .models import *
from django.template import RequestContext
from django.core.mail import send_mail
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.forms.formsets import formset_factory
from zinnia.models import Entry
from django.http import HttpResponseRedirect
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
#	ctx = {'entradas':entradas,'titulos':titulos}	
	return render_to_response('homepage/index.html', context_instance=RequestContext(request))

def aboutus(request):
	return render_to_response('homepage/aboutus.html', context_instance=RequestContext(request))

'''
def directors(request):
	chairman = Directors.objects.filter(member_type='chairman')
	president = Directors.objects.filter(member_type='president')
	vicepresident = Directors.objects.filter(member_type='vicepresident')
	secretary = Directors.objects.filter(member_type='secretary')
	treasurer = Directors.objects.filter(member_type='treasurer')
	others = Directors.objects.filter(member_type='director')
	ctx = {'chairman': chairman, 'president':president, 'vicepresident':vicepresident, 'secretary':secretary,'treasurer':treasurer,'otros':others}
	return render_to_response('homepage/directors.html', ctx, context_instance=RequestContext(request))

class application(CreateView):
	template_name = 'homepage/application.html'
	form_class = MemberForm

	def get_context_data(self, **kwargs):
		context = super(application, self).get_context_data(**kwargs)
		if self.request.POST:
			context['formset'] = MemberFormSet(self.request.POST, prefix='banking')
			context['formset_education'] = MemberFormSet2(self.request.POST, prefix='education')
		else:
			context['formset'] = MemberFormSet(prefix='banking')
			context['formset_education'] = MemberFormSet2(prefix='education')

		return context

	def form_valid(self, form):
		context = self.get_context_data()
		formset = context['formset']
		formset_education = context['formset_education']
		if formset.is_valid() and formset_education.is_valid():
			self.object = form.save()
			formset.instance = self.object
			formset.save()
			formset_education.instance = self.object
			formset_education.save() 
			exito = True
			cd_general = form.cleaned_data
			asunto = u'By: %s %s - Application to join HABAI' % (cd_general['names'], cd_general['last_name'])
			content = u'General Information:\n\n Names: %s \n Last Name: %s \n State: %s \nCity: %s \n Street address: %s \n ZIP: %s \n Personal Phone: %s \n Bussines Phone: %s \n celular: %s \n Fax: %s \n Email: %s \n\n\n\n Banking History:\n\n' % (cd_general['names'], cd_general['last_name'], cd_general['state'], cd_general['city'], cd_general['street_address'], cd_general['zip_code'], cd_general['personal_telephone'], cd_general['bussines_telephone'], cd_general['celular'], cd_general['fax'], cd_general['email_address'])
			for form_banking in formset:
				cd = form_banking.cleaned_data
				banking = u'Financial Institution: %s \n Position or Title: %s \n From: %s \nTo: %s\n\n' % (cd['financial_institution'], cd['position_or_title'], cd['from_date'], cd['to_date'])
				content = content + banking
			mensaje_education = u'\n\n\nEducation:\n\n'
			content = content + mensaje_education
			for form_education in formset_education:
				cd = form_education.cleaned_data
				education = u'Collage or University: %s \n Type of degree: %s \n Dates Attended: %s \n Did you graduate?: %s\n Course of Study: %s \n\n' % (cd['collage_or_university'], cd['type_of_degree'], cd['dates_attended'], cd['did_you_graduate'], cd['course_of_study'])
				content = content + education
			send_mail(asunto, content, cd_general['email_address'], ['info@hababankers.com'])        	
			ctx = {'exito':exito}
			return render_to_response('homepage/application.html', ctx, context_instance=RequestContext(self.request))
		else:
			return self.render_to_response(self.get_context_data(form=form))
'''