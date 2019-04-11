from django.urls import path

from .views import MascotaViewPost
from .views import MascotaViewList
from .views import MascotaViewUpdate

urlpatterns = [
    path(
        'post/',
        MascotaViewPost.as_view(),
        name='mascota-view-post'
    ),
    path(
        'list/',
        MascotaViewList.as_view(),
        name='mascota-view-list'
    ),
    path(
        'votar/<int:pk>',
        MascotaViewUpdate.as_view(),
        name='mascota-view-update'
    ),
]
