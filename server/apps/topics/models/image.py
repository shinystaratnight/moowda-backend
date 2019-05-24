from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.db.mixins import Timestamps
from apps.users.models import User


class Image(Timestamps):
    user = models.ForeignKey(
        User,
        models.CASCADE,
        related_name='images',
        verbose_name=_('VN__USER'),
        help_text=_('HT__USER')
    )

    data = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('VN__DATA'),
        help_text=_('HT__DATA')
    )

    class Meta:
        verbose_name = _('VN__IMAGE')
        verbose_name_plural = _('VN__IMAGES')
        ordering = ('-created_at',)

    def __str__(self):
        return '-'
