from modeltranslation.translator import translator, TranslationOptions
from .models import textosInicio, videosInicio, quienesSomos, quienesSomosOtros, sliderInicio, conferenciaslista, seccionesQuienesSomos, miembros, paisesCic, certificacionesLista, certificacionesIntroduccion, representantesInternacionales, servicios, cursoslista


class sliderInicioTranslationOptions(TranslationOptions):
	fields = ('titulo', 'texto_contenido')


class videosInicioTranslationOptions(TranslationOptions):
	fields = ('video_titulo',)


class textosInicioTranslationOptions(TranslationOptions):
	fields = ('eres_coach', 'certificaciones', 'recursos_informativos')


class quienesSomosTranslationOptions(TranslationOptions):
	fields = ('que_es_cic', 'quienes_forman', 'por_que_nace',)


class quienesSomosOtrosTranslationOptions(TranslationOptions):
	fields = ('mision', 'vision', 'valores',)


class seccionesQuienesSomosTranslationOptions(TranslationOptions):
	fields = ('paisesIntroduccion', 'codigo_etica',)
#quienesSomosOtros,'mision','vision','valores','paisesIntroduccion','codigo_etica'


class paisesCicTranslationOptions(TranslationOptions):
	fields = ('nombre',)


class representantesInternacionalesTranslationOptions(TranslationOptions):
	fields = ('paises',)


class certificacionesIntroduccionTranslationOptions(TranslationOptions):
	fields = ('introduccion', 'por_que_certificarte', 'quienes_certifican', 'porque_uno', 'porque_dos', 'porque_tres', 'porque_cuatro',)


class certificacionesListaTranslationOptions(TranslationOptions):
	fields = ('titulo', 'cuerpo_general')


class serviciosTranslationOptions(TranslationOptions):
	fields = ('asesoria_texto', 'cursos_texto', 'conferencias')


class cursoslistaTranslationOptions(TranslationOptions):
	fields = ('titulo', 'cuerpo_general')


class conferenciaslistaTranslationOptions(TranslationOptions):
	fields = ('titulo', 'cuerpo_general')


translator.register(textosInicio, textosInicioTranslationOptions)
translator.register(quienesSomos, quienesSomosTranslationOptions)
translator.register(paisesCic, paisesCicTranslationOptions)
translator.register(certificacionesIntroduccion, certificacionesIntroduccionTranslationOptions)
translator.register(representantesInternacionales, representantesInternacionalesTranslationOptions)
translator.register(certificacionesLista, certificacionesListaTranslationOptions)
translator.register(servicios, serviciosTranslationOptions)
translator.register(cursoslista, cursoslistaTranslationOptions)
translator.register(quienesSomosOtros, quienesSomosOtrosTranslationOptions)
translator.register(seccionesQuienesSomos, seccionesQuienesSomosTranslationOptions)
translator.register(conferenciaslista, conferenciaslistaTranslationOptions)
translator.register(videosInicio, videosInicioTranslationOptions)
