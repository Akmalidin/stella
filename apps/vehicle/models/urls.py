from django.urls import path
from .views import VehicleListCreateView, VehicleImageUploadView, VehicleDetail

urlpatterns = [
    path('', VehicleListCreateView.as_view(), name='vehicle-list-create'),
    path('<int:pk>/', VehicleDetail.as_view(), name='vehicle-detail'),
    path('image/', VehicleImageUploadView.as_view(), name='vehicle-image-upload'),
]
