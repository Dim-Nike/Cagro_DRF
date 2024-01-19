from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

# urlpatterns = [
#     path('', show_index, name='index'),
#     path('home/', show_home, name='home'),
#
#
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('cars/', CarListCreateView.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', CarRetrieveDestroyView.as_view(), name='car-retrieve-destroy'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)