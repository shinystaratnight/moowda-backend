from django.contrib import admin

from apps.core.admin.base import BaseModelAdmin
from .filters import TopicAutocompleteFilter, UserAutocompleteFilter
from ..models import Image, Topic, TopicMessage


@admin.register(Image)
class ImageAdmin(BaseModelAdmin):
    list_display = ('user', 'url')
    search_fields = ('user',)


@admin.register(Topic)
class TopicAdmin(BaseModelAdmin):
    list_display = ('title', 'owner')
    search_fields = ('title',)


@admin.register(TopicMessage)
class TopicMessageAdmin(BaseModelAdmin):
    list_display = ('topic', 'user', 'content')
    list_filter = (TopicAutocompleteFilter, UserAutocompleteFilter)
    search_fields = ('content',)
    autocomplete_fields = ('topic', 'user', 'images')
