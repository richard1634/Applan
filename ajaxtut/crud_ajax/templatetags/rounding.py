from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def round_down(value):
	if int(value) == 0:
		return "00"
	return int(value)

@register.filter
def my_mod(value):
	print(value)
	if value%60 == 0:
		return "00"
	return value % 60