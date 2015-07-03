# -*- encoding: utf-8 -*-
import os
from django.template import Library
from urlparse import parse_qs
from django.template.defaultfilters import stringfilter
import re
register = Library()

@stringfilter
def youthumbnail(value, args):
	"""returns youtube thumb url
	args s, l (small, large)
	Example <img src="{{vide.url|youthumbnail:'s'}}"/>
	It supports 2 sizes small(s) and large (l)
	"""
	qs = value.split('?')
	video_id = parse_qs(qs[1])['v'][0]

	if args == 's':
		return "http://img.youtube.com/vi/%s/2.jpg" % video_id
	elif args == 'l':
		return "http://img.youtube.com/vi/%s/0.jpg" % video_id
	else:
		return None
register.filter('youthumbnail', youthumbnail)


@register.filter(name='youtube_embed_url')
def youtube_embed_url(value):
	""" # converts youtube URL into embed HTML
		# value is url """
	match = re.search(r'^(http|https)\:\/\/www\.youtube\.com\/watch\?v\=(\w*)(\&(.*))?$', value)
	if match:
		embed_url = 'http://www.youtube.com/embed/%s' %(match.group(2))
		res = "<iframe width=\"1280\" height=\"750\" src=\"%s\" frameborder=\"0\" allowfullscreen></iframe>" %(embed_url)
		return res
	return 'Enlace de video invalido.'


@register.filter
def filesize(value):
    """Returns the filesize of the filename given in value"""
    return os.path.getsize(value)