from django import template

register = template.Library()


@register.filter()
def product_image(val):
    if val:
        return f'/media/{val}'

    return '#'
