
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

# swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="My Project API",
        default_version='v1',
        description="API Documentation",
        terms_of_service="#",
        contact=openapi.Contact(email="myproject@gmail.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

admin.site.site_header = "My Project Admin"
admin.site.site_title = "My Project Inventory"
admin.site.index_title = "My Project Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),

    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc',
                                      cache_timeout=0), name='schema-redoc'),

    # '''app paths'''
    path('api/v1/myapp/', include('myapp.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
