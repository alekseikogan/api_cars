from cars.views import CarAPIDestroy, CarAPIList, CarAPIUpdate
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/cars/', CarAPIList.as_view()),
    path('api/v1/cars/<int:pk>/', CarAPIUpdate.as_view()),
    path('api/v1/carsdelete/<int:pk>/', CarAPIDestroy.as_view()),
    path(
        'api/v1/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'),
    path(
        'api/v1/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'),
    path(
        'api/v1/token/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'),
]
