from django.template import Library
from ocp.courses.models import Enrollment, Category

# /Importante: Este template tag/arquivo foi construido pois uma mesma informação
# deveria que ser  gerada diversas vezes no view para ser mandada ao
# aos templates da app, para evitar gerar isso criamos uma tag
# que irá ser utilizada nos htmls/templates com a informação.
# Estas funcionalidades dão modularidade ao seu projeto.


register = Library()


# A tag inclusion converte uma função em uma tag
# que pode ser usada pelo django
# Quando eu chamar esta tag ela vai renderizar o
# template "my_courses.html"
@register.inclusion_tag('courses/templatetags/my_courses.html')
def my_courses(user):
    enrollments = Enrollment.objects.filter(user=user)
    context = {
        'enrollments': enrollments
    }
    return context


# a tag assigment é para adicionar algo no contexto para ser usado no htmal
@register.simple_tag
def load_my_courses(user):
    return Enrollment.objects.filter(user=user)
