from bitfield import BitField
from bitfield.forms import BitFieldCheckboxSelectMultiple

from apps.core.admin.list_filters import AutocompleteChangeListFilter


class AdminFormFieldsOverridesMixin:
    formfield_overrides = {
        BitField: {'widget': BitFieldCheckboxSelectMultiple},
    }


class AdminAutocompleteListFilterMixin:
    def changelist_view(self, request, extra_context=None):
        changelist_view = super().changelist_view(request, extra_context=extra_context)
        self.update_media(changelist_view)

        return changelist_view

    @staticmethod
    def update_media(changelist):
        if not hasattr(changelist.context_data['cl'], 'filter_specs') or not changelist.context_data['cl'].filter_specs:
            return

        for list_filter in changelist.context_data['cl'].filter_specs:
            if not isinstance(list_filter, AutocompleteChangeListFilter):
                continue

            for js in list_filter.media._js_lists:
                if js:
                    changelist.context_data['media']._js_lists.append(js)

            for css in list_filter.media._css_lists:
                if css:
                    changelist.context_data['media']._css_lists.append(css)
