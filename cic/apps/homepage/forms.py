#!/usr/local/bin/python
# -*- encoding: utf-8 -*-
from django import forms
from .models import miembrosRegistro, invitadoRegistro, CorreoBoletin

from django.forms.models import inlineformset_factory

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
	correo_principal = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': ' nick@email.com'}),required=False)
	correo_alterno = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': ' nick@email.com'}),required=False)
	nombre_empresa = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Si la solicitud es institucional'}),required=False)
	mensaje = forms.CharField(widget=forms.Textarea)

class contactForm(forms.Form):
	nombre_apellido = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Su nombre y apellido'}))
	telefono_fijo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Su Número de teléfono Fijo'}))
	telefono_movil = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Su Número de teléfono Móvil'}))
	correo_principal = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': ' nick@email.com'}),required=False)
	correo_alterno = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': ' nick@email.com'}),required=False)
	nombre_empresa = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Si la solicitud es institucional'}),required=False)
	mensaje = forms.CharField(widget=forms.Textarea)

class boletinForm(forms.ModelForm):
	correo = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'user@domain.com'}))

	class Meta:
		model = CorreoBoletin
		fields = ['correo']	