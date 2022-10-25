# from django.shortcuts import render

# Create your views here.

from datetime import datetime
from django.http import HttpResponse
from django.views.generic import TemplateView
import json


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'


class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs): 
        
        context = super().get_context_data(**kwargs)
        with open("mainapp/news.json", 'r', encoding='utf-8') as rf:
            context['list_data'] = json.load(rf)
        context["datetime_obj"] = datetime.now()
        # context["news_title"] = "Громкий новостной заголовок" 
        # context[ "news_preview"] = "Предварительное описание, которое заинтересует каждого" 
        context["range"] = range(1, len(context['list_data'])+1)
        return context

