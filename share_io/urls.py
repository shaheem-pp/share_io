from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('', include('home.urls', namespace = 'home')),
        # url('', include(('home.urls', 'home'), namespace = 'home')),
        path('user/', include('user.urls')),
        # path('', include('home.urls', 'home'), namespace = 'home'),
        # url(r'^reviews/', include(('reviews.urls', 'reviews'), namespace='reviews')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
