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
    path('api-auth/', include('rest_framework.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('submitData/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/submitData/', include(router.urls)),
    path('api/submitData/user__email=<str:email>', EmailAPIView.as_view(), name='email-pereval'),
    path('swagger-ui/', TemplateView.as_view(
       template_name='swagger-ui.html',
       extra_context={'schema_url':'openapi-schema'}
   ), name='swagger-ui'),
]
