from django.urls import path, include
from rest_framework import routers
from libros import views

router = routers.DefaultRouter()
router.register(r'Libros', views.LibroViewSet)
router.register(r'Autores', views.AutorViewSet)
router.register(r'Temas', views.TemaViewSet)

urlpatterns = [
    path("", include(router.urls)),

]