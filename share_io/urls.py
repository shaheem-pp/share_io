from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
        path('', include('home.urls', namespace = 'home')),
        path('user/', include('user.urls')),
        path('accounts/', include('django.contrib.auth.urls')),
        path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
