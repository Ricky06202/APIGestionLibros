from django.urls import path, include
from rest_framework import routers
from libros import views

router = routers.DefaultRouter()
router.register(r'Libro', views.LibroViewSet)

urlpatterns = [
    path("", include(router.urls)),
]