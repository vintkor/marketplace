from django.contrib import admin
from django.urls import path, include, re_path
from marketplace import settings
from django.conf.urls.static import static
from marketplace.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls'))
] + static(MEDIA_URL, document_root=MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
