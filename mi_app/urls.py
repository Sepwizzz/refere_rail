from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArbitrosViewSet, OrganizadorViewSet,EventoViewSet

router = DefaultRouter()
router.register(r'arbitros', ArbitrosViewSet)
router.register(r'organizadores', OrganizadorViewSet)
router.register(r'evento', EventoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
