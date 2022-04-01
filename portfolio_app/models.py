from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Feedback(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name=_('name'))
    email = models.EmailField(max_length=100, null=True, verbose_name=_('email'))
    message = models.TextField(verbose_name=_('message'))
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
