from django.urls import path
from mainapp import views
from mainapp.apps import MainappConfig
from django.views.decorators.cache import cache_page


app_name = MainappConfig.name


urlpatterns = [
    path("contacts/", views.ContactsView.as_view(), name='contacts'),
    path("docsite/", views.DocSiteView.as_view(), name='doc_site'),
    path("", views.IndexView.as_view(), name='main_page'),
    path("login/", views.LoginView.as_view(), name='login'),
    path("news/", views.NewsView.as_view(), name="news"),
    path("news/create/", views.NewsCreateView.as_view(), name="news_create"),
    path("news/<int:pk>/detail",
         views.NewsDetailView.as_view(), name="news_detail", ),
    path("news/<int:pk>/update",
         views.NewsUpdateView.as_view(), name="news_update", ),
    path("news/<int:pk>/delete",
         views.NewsDeleteView.as_view(), name="news_delete", ),
    path("courses/", cache_page(60*5) (views.CoursesView.as_view()), name="courses"),
    path("courses/<int:pk>/", views.CoursesDetailView.as_view(),
         name="courses_detail",),
    path("courses_feedback/", views.CourseFeedbackFormProcessView.as_view(),
         name="courses_feedback",),
     path("log_view/", views.LogView.as_view(), name="log_view"),
     path("log_download/", views.LogDownloadView.as_view(), name="log_download"),
]
