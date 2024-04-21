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

symptoms_patterns = [
    path('', views.symptom_list, name='symptoms-list'),
    path('<int:pk>/', views.symptom_detail, name='symptoms-detail'),
    path('crear/', views.symptom_create, name='symptoms-create'),
    path('<int:pk>/editar/', views.symptom_update, name='symptoms-edit'),
    path('<int:pk>/eliminar/', views.symptom_delete, name='symptoms-delete')
]

urlpatterns = [
    path('', views.log_in, name='log-in'),
    path('log-out/', views.log_out, name='log-out'),
    path('sintomas/', include(symptoms_patterns)),
    path('medicamentos/', include(medicines_patterns))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
