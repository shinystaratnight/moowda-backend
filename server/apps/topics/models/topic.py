from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.db.mixins import Timestamps
from apps.users.models import User


class Topic(Timestamps):
    title = models.CharField(
        max_length=150,
        verbose_name=_('VN__TITLE'),
        help_text=_('HT__TITLE')
    )

    owner = models.ForeignKey(
        User,
        models.CASCADE,
        related_name='topics',
        verbose_name=_('VN__OWNER'),
        help_text=_('HT__OWNER')
    )

    class Meta:
        verbose_name = _('VN__TOPIC')
        verbose_name_plural = _('VN__TOPICS')
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
