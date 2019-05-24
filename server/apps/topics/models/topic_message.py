from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.db.mixins import Timestamps
from apps.users.models import User
from .image import Image
from .topic import Topic


class TopicMessage(Timestamps):
    topic = models.ForeignKey(
        Topic,
        models.CASCADE,
        related_name='topic_messages',
        verbose_name=_('VN__TOPIC'),
        help_text=_('HT__TOPIC')
    )

    user = models.ForeignKey(
        User,
        models.CASCADE,
        related_name='topic_messages',
        verbose_name=_('VN__USER'),
        help_text=_('HT__USER')
    )

    content = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('VN__CONTENT'),
        help_text=_('HT__CONTENT')
    )

    images = models.ManyToManyField(
        Image,
        blank=True,
        related_name='topic_messages',
        verbose_name=_('VN__IMAGE'),
        help_text=_('HT__IMAGE')
    )

    class Meta:
        verbose_name = _('VN__TOPIC_MESSAGE')
        verbose_name_plural = _('VN__TOPIC_MESSAGES')
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.content[:15]}'
