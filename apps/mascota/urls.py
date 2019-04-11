from django.urls import path

from .views import MascotaViewPost

urlpatterns = [
    path(
        'post/',
        MascotaViewPost.as_view(),
        name='mascota-view-post'
    ),
]
