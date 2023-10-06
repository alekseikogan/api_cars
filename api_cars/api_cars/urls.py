from cars.views import CarViewSet
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]

print(f'Все урлы = {router.urls}')