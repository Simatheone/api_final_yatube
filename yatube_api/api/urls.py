from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet

router_v1 = DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('v1/', include(router_v1.urls))
]
