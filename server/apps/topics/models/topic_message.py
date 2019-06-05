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
        null=True,
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


class TopicMessageRead(Timestamps):
    message = models.ForeignKey(
        TopicMessage,
        models.CASCADE,
        related_name='topic_messages_read',
        verbose_name=_('VN__MESSAGE'),
        help_text=_('HT__MESSAGE')
    )

    topic = models.ForeignKey(
        Topic,
        models.CASCADE,
        related_name='topic_messages_read',
        verbose_name=_('VN__TOPIC'),
        help_text=_('HT__TOPIC')
    )

    user = models.ForeignKey(
        User,
        models.CASCADE,
        related_name='topic_messages_read',
        verbose_name=_('VN__USER'),
        help_text=_('HT__USER')
    )

    class Meta:
        verbose_name = _('VN__TOPIC_MESSAGE_READ')
        verbose_name_plural = _('VN__TOPIC_MESSAGES_READ')
        ordering = ('-created_at',)
        unique_together = ('message', 'user')

    def __str__(self):
        return f'{self.content[:15]}'
