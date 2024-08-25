from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from coreapi.views import index

urlpatterns = [
    path('',include('coreapi.urls')),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
