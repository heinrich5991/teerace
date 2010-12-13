import re
from django import template

register = template.Library()

@register.simple_tag
def current(request, pattern):
	if pattern == "/":
		if request.path == pattern:
			return ' id="current"'
		else:
			return ''
	if re.search(pattern, request.path):
		return ' id="current"'
	return ''


@register.simple_tag
def current_unique(request, pattern, id):
	if re.search(pattern, request.path):
		return ' id="%s-current"' % id
	return ' id="%s"' % id