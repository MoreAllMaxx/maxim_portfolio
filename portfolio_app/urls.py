from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about', views.AboutView.as_view(), name='about'),
    path('contact', views.FeedbackFormView.as_view(), name='contact'),
    path('contact_success', views.FeedbackSuccessView.as_view(), name='contact_success'),
    path('i18n', include('django.conf.urls.i18n')),
]
