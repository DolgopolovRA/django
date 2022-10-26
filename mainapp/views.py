# from django.shortcuts import render

# Create your views here.

from datetime import datetime
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from mainapp.models import News


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

        context['list_data'] = News.objects.filter(deleted=False)
        context["datetime_obj"] = datetime.now()
        context["range"] = range(1, len(context['list_data'])+1)
        return context


class NewsDetail(TemplateView):
    template_name = 'mainapp/news_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = get_object_or_404(News, pk=self.kwargs.get('pk'))
        return context
        
    
