from django.urls import include, path
from rest_framework import routers

from .views import PerevalsViewSet


router = routers.DefaultRouter()
router.register('submitData', PerevalsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]