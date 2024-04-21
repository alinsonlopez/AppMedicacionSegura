from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Registrar las URLs de tu aplicación aquí
    path('', include('apps.medicines.urls')),
]

# Para servir archivos estáticos en desarrollo
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
