# -*- coding: utf-8 -*-
from django.db import models
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.template import defaultfilters
import re
import string
import random


class sliderInicio(models.Model):
	titulo = models.CharField(max_length=70)
	texto_contenido = models.TextField()
	imagen = models.ImageField(upload_to='sliderItems')


class quienesSomos(models.Model):
	que_es_cic = models.TextField()
	quienes_forman = models.TextField()
	por_que_nace = models.TextField()
	class Meta:
		verbose_name = ("Que es CIC, Quienes la forman")
		verbose_name_plural = ("Que es CIC, Quienes la forman")


class quienesSomosOtros(models.Model):
	mision = models.TextField()
	vision = models.TextField()
	valores = HTMLField()
	class Meta:
		verbose_name = ("Mision, visión y valores")
		verbose_name_plural = ("Mision, visión y valores")

class seccionesQuienesSomos(models.Model):
	paisesIntroduccion = models.TextField()
	codigo_etica = models.TextField()
	class Meta:
		verbose_name = ("Texto Paises, Codigo de Etica")
		verbose_name_plural = ("Texto Paises, Codigo de Etica")


class textosInicio(models.Model):
	eres_coach = models.CharField(max_length=140)
	certificaciones = models.CharField(max_length=140)
	recursos_informativos = models.CharField(max_length=140)


class paisesCic(models.Model):
	nombre = models.CharField(max_length=70)
	imagen_bandera = models.ImageField(upload_to='imgbanderas')

	class Meta:
		verbose_name = ("Pais CIC")
		verbose_name_plural = ("Paises de la CIC")


class miembrosRegistro(models.Model):
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)
	modificado_en = models.DateTimeField(auto_now=True)
	numero_registro= models.CharField(max_length=100, blank=True)
	nombre_completo = models.CharField(max_length=200)
	identificacion = models.CharField(max_length=50)
	fecha_nacimiento = models.CharField(max_length=50)
	nacionalidad = models.CharField(max_length=100)
	pais_recidencia = models.CharField(max_length=100)
	direccion = models.CharField(max_length=300)
	apartado_postal = models.CharField(max_length=50)
	codigo_area = models.CharField(max_length=50)
	telefono_habitacion = models.CharField(max_length=50)
	telefono_movil = models.CharField(max_length=50)
	otro_numero = models.CharField(max_length=50)
	correo = models.CharField(max_length=50)
	profesion = models.CharField(max_length=100)
	experiencia = models.CharField(max_length=100)
	pais_certificacion = models.CharField(max_length=100)
	ciudad_certificacion = models.CharField(max_length=100)
	institucion_certificacion = models.CharField(max_length=200)
	nombre_certificacion = models.CharField(max_length=200)
	trainer_certificacion = models.CharField(max_length=200)
	periodo_certificacion = models.CharField(max_length=200)
	horas_programa = models.CharField(max_length=100)
	fecha_certificacion = models.CharField(max_length=100)
	codigo_certificacion = models.CharField(max_length=100)
	nombre_certificacion_cic = models.CharField(max_length=200, blank=True)
	codigo_certificacion_cic = models.CharField(max_length=100, blank=True)
	fecha_certificacion_cic = models.CharField(max_length=100, blank=True)
	pais_certificacion_cic = models.CharField(max_length=100, blank=True)
	trainer_certificacion_cic = models.CharField(max_length=200, blank=True)
	nombre_otra_certificacion = models.CharField(max_length=200, blank=True)
	codigo_otra_certificacion = models.CharField(max_length=100, blank=True)
	fecha_otra_certificacion = models.CharField(max_length=100, blank=True)
	quiencertifica_otra_certificacion = models.CharField(max_length=200, blank=True)
	pais_otra_certificacion = models.CharField(max_length=100, blank=True)
	entidad_otra_certificacion = models.CharField(max_length=200, blank=True)
	coaching_profesion_principal = models.TextField()
	experiencia_ejerciendo_coaching = models.CharField(max_length=100)
	ejerce_coaching_como = models.TextField()
	coach_a_nivel_de = models.TextField()
	campo_especifico = models.TextField()
	coaching_de_manera = models.TextField()
	publicaciones_relacionadas = models.TextField(blank=True)
	descripcion_publicaciones = models.TextField(blank=True)
	eventos_internacionales = models.TextField(blank=True)
	areas_interes_personal = models.TextField()
	que_desea_delacic = models.TextField()
	def __unicode__(self):
		return self.nombre_completo
	class Meta:
		verbose_name = ("Registro de Coach certificado con la CIC")
		verbose_name_plural = ("Registros de Coaches certificados con la CIC")


class invitadoRegistro(models.Model):
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)
	numero_registro= models.CharField(max_length=100, blank=True)
	modificado_en = models.DateTimeField(auto_now=True)
	nombre_completo = models.CharField(max_length=200)
	identificacion = models.CharField(max_length=50)
	fecha_nacimiento = models.CharField(max_length=50)
	nacionalidad = models.CharField(max_length=100)
	pais_recidencia = models.CharField(max_length=100)
	direccion = models.CharField(max_length=300)
	apartado_postal = models.CharField(max_length=50)
	codigo_area = models.CharField(max_length=50)
	telefono_habitacion = models.CharField(max_length=50)
	telefono_movil = models.CharField(max_length=50)
	otro_numero = models.CharField(max_length=50)
	correo = models.CharField(max_length=50)
	profesion = models.CharField(max_length=100)
	experiencia = models.CharField(max_length=100)
	codigo_inscripcion = models.CharField(max_length=300)
	razon_de_registro = models.CharField(max_length=300)
	nombre_certificacion = models.CharField(max_length=300)
	codigo_certificacion = models.CharField(max_length=300)
	fecha_certificacion = models.CharField(max_length=300)
	quienes_certifican = models.CharField(max_length=300)
	pais_certificacion = models.CharField(max_length=300)
	entidad_certificacion = models.CharField(max_length=300)
	certificacion_dos = models.CharField(max_length=300,blank=True)
	avalada_por = models.CharField(max_length=300,blank=True)
	ano_dos = models.CharField(max_length=300,blank=True)
	pais_dos = models.CharField(max_length=300,blank=True)
	certificacion_tres = models.CharField(max_length=300,blank=True)
	avalada_por_tres = models.CharField(max_length=300,blank=True)
	ano_tres = models.CharField(max_length=300,blank=True)
	pais_tres = models.CharField(max_length=300,blank=True)
	coaching_profesion_principal = models.TextField()
	experiencia_ejerciendo_coaching = models.CharField(max_length=100)
	ejerce_coaching_como = models.TextField()
	coach_a_nivel_de = models.TextField()
	campo_especifico = models.TextField()
	coaching_de_manera = models.TextField()
	publicaciones_relacionadas = models.TextField(blank=True)
	descripcion_publicaciones = models.TextField(blank=True)
	eventos_internacionales = models.TextField(blank=True)
	que_desea_delacic = models.TextField()
	def __unicode__(self):
		return self.nombre_completo
	class Meta:
		verbose_name = ("Registro de Coach Invitado")
		verbose_name_plural = ("Registros de Coaches Invitados")

def _createcode(size=9, chars=string.ascii_uppercase + string.digits):
	    return ''.join(random.choice(chars) for _ in range(size))	

class miembros(models.Model):
	TIPO_DE_MIEMBRO = (('comun', 'Miembro común'), ('directivo', 'Directivo'))
	numero_registro = models.CharField(max_length=70)
	descripcion_breve = models.CharField(max_length=100, help_text="Hasta 100 caractares")
	imagen = models.ImageField(upload_to='imgdirectorio', blank=True)
	tipo_de_miembro = models.CharField(max_length=20, choices=TIPO_DE_MIEMBRO)
	registro_certificado_cic = models.ForeignKey(miembrosRegistro, blank=True, null=True)
	registro_invitado = models.ForeignKey(invitadoRegistro, blank=True, null=True)
	acceso_directorio = models.CharField(max_length=10, default=_createcode, help_text="No modificar.Auto-generado")
	class Meta:
		verbose_name = ("Miembro de la CIC")
		verbose_name_plural = ("Miembros de la CIC")
	def __unicode__(self):
		return self.numero_registro

class representantesInternacionales(models.Model):
	paises = models.CharField(max_length=150)
	nombre = models.CharField(max_length=150)

	class Meta:
		verbose_name = ("Representantes Internacionales")
		verbose_name_plural = ("Representantes Internacionales")


class certificacionesIntroduccion(models.Model):
	introduccion = models.TextField()
	por_que_certificarte = models.TextField()
	quienes_certifican = models.TextField()
	porque_uno = models.TextField()
	porque_dos = models.TextField()
	porque_tres = models.TextField()
	porque_cuatro = models.TextField()

	class Meta:
		verbose_name = ("Certificciones Texto General")
		verbose_name_plural = ("Certificciones Texto General")


class certificacionesLista(models.Model):
	TIPO = (('certificacion','Certificacion'),('especializacion','Especialización'))
	titulo = models.CharField(max_length=200)
	cuerpo_general = HTMLField()
	tipo = models.CharField(choices=TIPO, max_length=40)
	imagen = models.ImageField(upload_to='imgcursos', blank=True, help_text="Imagen sobre la certificación")
	slug = models.SlugField(max_length=50, verbose_name="Url", help_text="No modificar auto-generado")

	def __unicode__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.titulo)
		super(certificacionesLista, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('certificaciondetalle', kwargs={u'slug': self.slug})

	class Meta:
		verbose_name = ("Lista de Certificaciones y Especializaciones")
		verbose_name_plural = ("Lista de Certificaciones y Especializaciones")


class servicios(models.Model):
	asesoria_texto = HTMLField()
	cursos_texto = HTMLField()
	conferencias = HTMLField()
	class Meta:
		verbose_name = ("Asesorias, Texto Cursos, Texto Conferencias")
		verbose_name_plural = ("Asesorias, Texto Cursos, Texto Conferencias")


class conferenciaslista(models.Model):
	titulo = models.CharField(max_length=200)
	cuerpo_general = HTMLField()
	slugconf = models.SlugField(max_length=50, verbose_name="Url", help_text="No modificar auto-generado")
	imagen = models.ImageField(upload_to='imgconferences', blank=True, help_text="Imagen sobre la conferencia")

	def __unicode__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		self.slugcurso = defaultfilters.slugify(self.titulo)
		super(conferenciaslista, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('conferenciasdetalle', kwargs={u'slugconf': self.slugconf})

	class Meta:
		verbose_name = ("Lista de Conferencias")
		verbose_name_plural = ("Lista de Conferencias")


class cursoslista(models.Model):
	titulo = models.CharField(max_length=200)
	slugcurso = models.SlugField(max_length=50, verbose_name="Url", help_text="No modificar auto-generado")
	cuerpo_general = HTMLField()
	imagen = models.ImageField(upload_to='imgcursos', blank=True, help_text="Imagen sobre el curso")

	def __unicode__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		self.slugcurso = defaultfilters.slugify(self.titulo)
		super(cursoslista, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('cursodetalle', kwargs={u'slugcurso': self.slugcurso})

	class Meta:
		verbose_name = ("Lista de Cursos")
		verbose_name_plural = ("Lista de Cursos")


def validate_url_video(value):
	match = re.search(r'^(http|https)\:\/\/www\.youtube\.com\/watch\?v\=(\w*)(\&(.*))?$', value)
	if not match:
		raise ValidationError(u'Enlace de video no valido debe tener el siguiente formato http://www.youtube.com/watch?v=IDVIDEO')


class videosInicio(models.Model):
	video_titulo = models.CharField(max_length=80, help_text="Título del video en homepage, hasta 80 caracteres")
	video_link = models.CharField(max_length=100, validators=[validate_url_video])

	def __unicode__(self):
		return self.video_titulo

class CorreoBoletin(models.Model):
	""""Lista de correos ingresados por los clientes en la pagina de inicio para el boletin"""
	correo = models.EmailField(max_length=50)
	nombre = models.CharField(max_length=100)