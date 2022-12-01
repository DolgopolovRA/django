# from django.shortcuts import render

# Create your views here.

from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, DetailView
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from mainapp.forms import CourseFeedbackForm
from django.template.loader import render_to_string


from mainapp.models import News, Course, Lesson, CourseTeacher, CourseFeedback


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'


class CoursesView(ListView):
    model = Course


class CoursesDetailView(TemplateView):
    template_name = "mainapp/courses_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super(CoursesDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(Course, pk=pk)
        context["lessons"] = Lesson.objects.filter(
            course=context["course_object"])
        context["teachers"] = CourseTeacher.objects.filter(
            course=context["course_object"])
        if not self.request.user.is_anonymous:
            if not CourseFeedback.objects.filter(course=context["course_object"], user=self.request.user).count():
                context["feedback_form"] = CourseFeedbackForm(
                    course=context["course_object"], user=self.request.user)
            context["feedback_list"] = CourseFeedback.objects.filter(
                course=context["course_object"]).order_by("-created", "-rating")[:5]
            return context


class CourseFeedbackFormProcessView(LoginRequiredMixin, CreateView):
    model = CourseFeedback
    form_class = CourseFeedbackForm

    def form_valid(self, form):
        self.object = form.save()
        rendered_card = render_to_string(
            "mainapp/includes/feedback_card.html", context={"item": self.object})

        return JsonResponse({"card": rendered_card})


class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsView(ListView):
    model = News
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class NewsCreateView(PermissionRequiredMixin, CreateView):
    model = News
    fields = "__all__"
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.add_news",)


class NewsDetailView(DetailView):
    model = News


class NewsUpdateView(PermissionRequiredMixin, UpdateView):

    model = News
    fields = "__all__"
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.change_news",)


class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    model = News
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.delete_news",)
