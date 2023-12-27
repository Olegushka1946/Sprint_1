from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pereval import views
from pereval.views import EmailAPIView
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


router = routers.DefaultRouter()
router.register(r'users', views.UsersViewset)
router.register(r'coords', views.CoordsViewset)
router.register(r'level', views.LevelViewset)
router.register(r'images', views.ImagesViewset)
router.register(r'perevals', views.PerevalsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('submitData/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/submitData/user__email=<str:email>', EmailAPIView.as_view(), name='email-pereval')
]
