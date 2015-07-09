#!/usr/local/bin/python
# -*- encoding: utf-8 -*-
from django import forms
from .models import miembrosRegistro, invitadoRegistro, CorreoBoletin

#from django.forms.models import inlineformset_factory


class HoneypotWidget(forms.TextInput):
	is_hidden = True

	def __init__(self, attrs=None, html_comment=False, *args, **kwargs):
		self.html_comment = html_comment
		super(HoneypotWidget, self).__init__(attrs, *args, **kwargs)
		#if not self.attrs.has_key('class'):
		if not 'class' in self.attrs:
			self.attrs['style'] = 'display:none'

	def render(self, *args, **kwargs):
		value = super(HoneypotWidget, self).render(*args, **kwargs)
		if self.html_comment:
			value = '<!-- %s -->' % value
		return value


class MemberForm(forms.ModelForm):
	class Meta:
		model = miembrosRegistro


class MiembroInvitadoForm(forms.ModelForm):
	class Meta:
		model = invitadoRegistro


class solicitudForm(forms.Form):
	nombre_apellido = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Su nombre y apellido'}))
	pais_origen = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Pais de Origen'}))
	codigo_area = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Código de área'}))
	telefono_movil = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Su Número de teléfono Móvil'}))
	telefono_fijo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Su Número de teléfono Fijo'}))
	correo_principal = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': ' nick@email.com'}), required=False)
	correo_alterno = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': ' nick@email.com'}), required=False)
	nombre_empresa = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Si la solicitud es institucional'}), required=False)
	mensaje = forms.CharField(widget=forms.Textarea)
	website = forms.CharField(widget=HoneypotWidget, required=False)

	def clean_asunto(self):
		cd = self.cleaned_data
		asunto = cd.get('asunto')
		if len(asunto) < 3:
			raise forms.ValidationError("El asunto debe tener mas de 2 letras")
		return asunto

	def clean_texto(self):
		cd = self.cleaned_data
		texto = cd.get('texto')
		if len(texto) < 4:
			raise forms.ValidationError("*")
		return texto

	def clean_website(self):
		cd = self.cleaned_data
		website = cd.get('website')
		if len(website) > 0:
			raise forms.ValidationError('Anti-spam field changed in value.')
		if website != '':
			raise forms.ValidationError('Anti-spam field changed in value.')


class boletinForm(forms.ModelForm):
	correo = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'user@domain.com'}))
	nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Su nombre'}))
	
	class Meta:
		model = CorreoBoletin
		fields = ['correo','nombre']	

class contactForm(forms.Form):
	nombre_apellido = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Su nombre y apellido'}))
	pais_origen = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Pais de Origen'}))
	codigo_area = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Código de área'}))
	telefono_fijo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Su Número de teléfono Fijo'}))
	telefono_movil = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Su Número de teléfono Móvil'}))
	correo_principal = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': ' nick@email.com'}), required=False)
	correo_alterno = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': ' nick@email.com'}), required=False)
	nombre_empresa = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Si la solicitud es institucional'}), required=False)
	mensaje = forms.CharField(widget=forms.Textarea)
	website = forms.CharField(widget=HoneypotWidget, required=False)

	def clean_asunto(self):
		cd = self.cleaned_data
		asunto = cd.get('asunto')
		if len(asunto) < 3:
			raise forms.ValidationError("El asunto debe tener mas de 2 letras")
		return asunto

	def clean_texto(self):
		cd = self.cleaned_data
		texto = cd.get('texto')
		if len(texto) < 4:
			raise forms.ValidationError("*")
		return texto

	def clean_website(self):
		cd = self.cleaned_data
		website = cd.get('website')
		if len(website) > 0:
			raise forms.ValidationError('Anti-spam field changed in value.')
		if website != '':
			raise forms.ValidationError('Anti-spam field changed in value.')


class peticionForm(forms.Form):
	nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Su nombre'}))
	empresa = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Empresa a la que pertenece'}))
	cargo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Cargo que ocupa en la empresa'}))
	email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'nick@email.com'}))
	telefono = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Su número de teléfono'}))
	pais = forms.CharField(max_length=100)
	comentario = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}), required=False)
	website = forms.CharField(widget=HoneypotWidget, required=False)

	def clean_asunto(self):
		cd = self.cleaned_data
		asunto = cd.get('asunto')
		if len(asunto) < 3:
			raise forms.ValidationError("El asunto debe tener mas de 2 letras")
		return asunto

	def clean_texto(self):
		cd = self.cleaned_data
		texto = cd.get('texto')
		if len(texto) < 4:
			raise forms.ValidationError("*")
		return texto

	def clean_website(self):
		cd = self.cleaned_data
		website = cd.get('website')
		if len(website) > 0:
			raise forms.ValidationError('Anti-spam field changed in value.')
		if website != '':
			raise forms.ValidationError('Anti-spam field changed in value.')