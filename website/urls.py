from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="website/home.html"), name="home"),
    path("about/", TemplateView.as_view(template_name="website/about.html"), name="about"),
    path("method/", TemplateView.as_view(template_name="website/method.html"), name="method"),
    path("school/", TemplateView.as_view(template_name="website/school.html"), name="school"),
    path("contact/", TemplateView.as_view(template_name="website/contact.html"), name="contact"),
]
