from django.urls import path, include
from rest_framework import routers

from .views import CursosViewSet, AvaliacoesViewSet

router = routers.DefaultRouter()
router.register("cursos", CursosViewSet, basename="cursos")
router.register("avaliacoes", AvaliacoesViewSet, basename="avaliacoes")

urlpatterns = [path("", include(router.urls))]
