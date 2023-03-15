from django import template, forms
from ..models import *

register = template.Library()


@register.filter(name='censor') # не получается сделать цензор, удаляет целиком все заголовки не понимаю почему,
                                # подскажите как сделать пожлуйста
class ContactForm(forms.Form):
    def censor(self):
        STOP = ['mat', 'abc', 'def', 'no', 'filter']
        data = News.header.title()
        if STOP in data:
            raise ValueError("Вы позволили себе немного лишнего! Одумайтесь и исправьте текст!")
        return data
