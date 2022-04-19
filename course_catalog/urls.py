from django.urls import include, path
# from .views import slm_home_view, SignUpView
from django.views.generic import TemplateView
# from django.contrib.auth import views as auth_views
from .views import CatalogHomeView


urlpatterns = [
    path('', CatalogHomeView.as_view(), name='catalog_home'),
]