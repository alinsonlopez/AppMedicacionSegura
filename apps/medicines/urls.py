from django.urls import path, include
from apps.medicines import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'medicines'

medicines_patterns = [
    path('', views.movie_list, name='home'),
    path('<int:pk>/', views.movie_detail, name='medicines-detail'),
    path('crear/', views.movie_create, name='medicines-create'),
    path('<int:pk>/editar/', views.movie_update, name='medicines-edit'),
    path('<int:pk>/eliminar/', views.movie_delete, name='medicines-delete')
]

urlpatterns = [
    path('', views.log_in, name='log-in'),
    path('log-out/', views.log_out, name='log-out'),
    path('categorias/', views.category_list, name='category-list'),
    path('medicamentos/', include(medicines_patterns))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
