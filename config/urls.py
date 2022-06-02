from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="BullKing",
        default_version='versão sigma',
        description="Calculadora de Macro",
        terms_of_service="Termos de servicço",
        contact=openapi.Contact(email="gabrielmorishita@hotmail.com"),
        license=openapi.License(name="License"),
        ),
    public=True,
    permission_classes=(permissions.BasePermission,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('nutri/', include('apps.food.urls')),
    path('user/', include('apps.user.urls')),
]
