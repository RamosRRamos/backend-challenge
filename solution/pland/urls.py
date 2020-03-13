from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api.viewsets import PlaceViewSet

# Configuration for Django Rest Framework
router = routers.DefaultRouter()
router.register(r'place', PlaceViewSet)

# Urls
urlpatterns = [

    path('rest/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
