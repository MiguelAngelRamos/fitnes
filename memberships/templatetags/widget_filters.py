# memberships/templatetags/widget_filters.py

from django import template
from django.forms.widgets import SelectDateWidget

register = template.Library()

@register.filter
def is_select(field):
    # Verificar si el widget es de tipo Select o SelectDateWidget
    return isinstance(field.field.widget, SelectDateWidget)