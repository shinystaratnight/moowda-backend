from django.contrib import admin

from apps.core.admin.base import BaseModelAdmin
from ..models import Image, Topic, TopicMessage


@admin.register(Image)
class ImageAdmin(BaseModelAdmin):
    list_display = ('user', 'url')


@admin.register(Topic)
class TopicAdmin(BaseModelAdmin):
    list_display = ('title', 'owner')
    search_fields = ('title',)


@admin.register(TopicMessage)
class TopicMessageAdmin(BaseModelAdmin):
    list_display = ('topic', 'user', 'content')
    list_filter = ('topic',)
    search_fields = ('content',)
