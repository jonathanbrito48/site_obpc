from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.site_obpc.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
