# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from datetime import datetime


class NewsList(ListView):
    model = News  # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = News.objects.order_by('-id')


class NewsDetail(DetailView):
    model = News  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'OneNews.html'  # название шаблона будет product.html
    context_object_name = 'OneNews'  # название объекта

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
# Create your views here.
