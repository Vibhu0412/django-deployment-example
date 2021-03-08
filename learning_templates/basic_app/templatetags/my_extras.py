from django import template

register = template.Library()

#decorators
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from string
    """

    return value.replace(arg,'')

# register.filter('cut',cut)
