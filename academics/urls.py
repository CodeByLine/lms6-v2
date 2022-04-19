from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="academics/academics_home.html"), name="academics_home"),
]