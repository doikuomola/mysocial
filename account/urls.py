from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register', views.register, name='register'),
    path('edit/', views.edit, name='edit'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)