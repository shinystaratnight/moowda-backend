from django.contrib import admin

from apps.core.admin.base import BaseModelAdmin
from ..models import Image, Topic, TopicMessage


@admin.register(Image)
class ImageAdmin(BaseModelAdmin):
    list_display = ('user', 'data')


@admin.register(Topic)
class TopicAdmin(BaseModelAdmin):
    list_display = ('title', 'owner')


@admin.register(TopicMessage)
class TopicMessageAdmin(BaseModelAdmin):
    list_display = ('topic', 'user', 'content')
