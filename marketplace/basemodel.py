from django.db import models
from django.utils.translation import ugettext as _


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=_('Дата создания'))
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name=_('Дата обновления'))

    objects = models.Manager()
