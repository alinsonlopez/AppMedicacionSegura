from django.urls import path, include
from apps.medicines import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'medicines'

medicines_patterns = [
    path('', views.medicine_list, name='home'),
    path('<int:pk>/', views.medicine_detail, name='medicines-detail'),
    path('crear/', views.medicine_create, name='medicines-create'),
    path('<int:pk>/editar/', views.medicine_update, name='medicines-edit'),
    path('<int:pk>/eliminar/', views.medicine_delete, name='medicines-delete')
]

categories_patterns = [
    path('', views.category_list, name='category-list'),
    path('<int:pk>/', views.category_detail, name='category-detail'),
    path('crear/', views.category_create, name='category-create'),
    path('<int:pk>/editar/', views.category_update, name='category-edit'),
    path('<int:pk>/eliminar/', views.medicine_delete, name='category-delete')
]

urlpatterns = [
    path('', views.log_in, name='log-in'),
    path('log-out/', views.log_out, name='log-out'),
    path('categorias/', include(categories_patterns)),
    path('medicamentos/', include(medicines_patterns))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
