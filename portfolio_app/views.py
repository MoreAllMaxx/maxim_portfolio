from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.utils.translation import gettext as _
from .models import Feedback
from .forms import FeedbackForm


class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {'title': _('Home')}


class AboutView(TemplateView):
    template_name = 'about.html'
    extra_context = {'title': _('About')}


class FeedbackFormView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback.html'
    success_url = reverse_lazy('contact_success')
    extra_context = {'title': _('Feedback'), }


class FeedbackSuccessView(TemplateView):
    template_name = 'feedback_success.html'
    extra_context = {'title': _('Feedback success')}
