from cars.views import CarAPIView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/cars/', CarAPIView.as_view()),
    path('api/v1/cars/<int:pk>/', CarAPIView.as_view())
]
