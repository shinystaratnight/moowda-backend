from apps.core.admin.list_filters import AutocompleteChangeListFilter


class TopicAutocompleteFilter(AutocompleteChangeListFilter):
    title = 'Topic'
    parameter_name = 'topic'


class UserAutocompleteFilter(AutocompleteChangeListFilter):
    title = 'User'
    parameter_name = 'user'
