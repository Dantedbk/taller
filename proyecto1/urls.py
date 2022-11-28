
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from crud import urls, views
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),

    path('', include('crud.urls')),
    path('api/', include('api.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)


# http://127.0.0.1:8000/api/xxxxxxxxxx
