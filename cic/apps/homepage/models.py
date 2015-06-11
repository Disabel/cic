# -*- coding: utf-8 -*-
from django.db import models
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse

class quienesSomos(models.Model):
	que_es_cic = HTMLField()
	quienes_forman = HTMLField()
	por_que_nace = HTMLField()
	mision = HTMLField()
	vision = HTMLField()
	valores = HTMLField()
'''
def validate_url_video(value):
	match = re.search(r'^(http|https)\:\/\/www\.youtube\.com\/watch\?v\=(\w*)(\&(.*))?$', value)
	if not match:
		raise ValidationError(u'Enlace de video no valido debe tener el siguiente formato http://www.youtube.com/watch?v=IDVIDEO')


class sliderInicio(models.Model):
	titulo = models.CharField(max_length=70)
	texto_contenido = models.TextField()
	imagen = models.ImageField(upload_to='sliderItems')

class textosInicio(models.Model):
	eres_coach = models.TextField(max_length=140)
	certificaciones = models.TextField(max_length=140)
	recursos_informativos = models.TextField(max_length=140)

class videosInicio(models.Model):
	video_titulo = models.CharField(max_length=80, help_text="Título del video en homepage, hasta 80 caracteres")
	video_link = models.CharField(max_length=100, validators=[validate_url_video])

class paisesCic(models.Model):
	nombre = models.CharField(max_length=70)
	imagen_bandera = models.ImageField(upload_to='imgbanderas')

class miembros(models.Model):
	TIPO_DE_MIEMBRO = (('comun','Miembro común'),('directivo','Directivo'))
	numero_registro = models.CharField(max_length=70)
	nombre_completo = models.CharField(max_length=70)
	descripcion_breve = models.CharField(max_length=100, help_text="Hasta 100 caractares")
	pais = models.ForeignKey(paisCic)
	correo_electronico = models.EmailField(max_length=80)
	imagen = models.ImageField(upload_to='imgdirectorio', blank=True)
	tipo_de_miembro = models.CharField(max_length=20, choices=TIPO_DE_MIEMBRO)

class representantesInternacionales(models.Model):
	paises = models.CharField(max_length=150)
	nombre = models.CharField(max_length=150)
	
class certificacionesIntroduccion(models.Model):
	introduccion = HTMLField()
	por_que_certificarte = HTMLField()
	quienes_certifican = HTMLField()

class certificacionesLista(models.Model):
	titulo = models.CharField(max_length=200)
	cuerpo_general = HTMLField()

class cursoslista(models.Model):
	titulo = models.CharField(max_length=200)
	cuerpo_general = HTMLField()

class servicios(models.Model):
	asesoria_texto = HTMLField()
	cursos_texto = HTMLField()

class Directors(models.Model):
	TIPO = (('chairman', 'Chairman of the Board'), ('president', 'President'), ('vicepresident', 'Vice President'),('secretary', 'Secretary'), ('treasurer', 'Treasurer'), ('director', 'Director'))
	member_type =  models.CharField(max_length=60, choices=TIPO)
	nombre = models.CharField(max_length=45, help_text='Hasta 45 caracteres')
	def __unicode__(self):
		return self.nombre

class MembersApplication(models.Model):
	names = models.CharField(max_length=70)
	last_name = models.CharField(max_length=70)
	state = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	street_address = models.CharField(max_length=100)
	zip_code = models.IntegerField()
	personal_telephone = models.CharField(max_length=100)
	bussines_telephone = models.CharField(max_length=100,blank=True)
	celular = models.CharField(max_length=100,blank=True)
	fax = models.CharField(max_length=100,blank=True)
	email_address = models.EmailField(max_length=50)
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)

class BankingHistory(models.Model):
	financial_institution = models.CharField(max_length=100)
	position_or_title = models.CharField(max_length=100)
	from_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	to_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	member = models.ForeignKey(MembersApplication)

class Education(models.Model):
	GRADUATED = (('yes','Yes'),('no','No'))
	collage_or_university = models.CharField(max_length=100)
	type_of_degree = models.CharField(max_length=100)
	dates_attended = models.CharField(max_length=100)
	did_you_graduate = models.CharField(max_length=5, choices=GRADUATED)
	course_of_study = models.CharField(max_length=100)
	member = models.ForeignKey(MembersApplication)

'''

