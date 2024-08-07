from django import template
register = template.Library()

@register.filter(name='append_class')
def input_class(field, class_name):
    return field.as_widget(attrs={
        "class": " ".join((field.css_classes(), class_name))
    })