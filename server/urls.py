from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.utils.translation import gettext_lazy as _
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import authentication, permissions

from apps.core.utils.modules import get_module_url_patterns

admin.site.site_header = _('VN__ADMIN_DASHBOARD')

schema_view = get_schema_view(
    openapi.Info(
        title='Moowda API',
        default_version='v1',
        description='Moowda API',
    ),
    public=True,
    authentication_classes=(authentication.SessionAuthentication,),
    permission_classes=(permissions.IsAdminUser,),
)

urlpatterns = [
    path('ht/', include('health_check.urls')),

    path('api/', include((get_module_url_patterns(
        'apps.users.rest.urls',
    ), 'urls'), namespace='api')),
    re_path(r'^api/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='swagger-json'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin_tools/', include('admin_tools.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
