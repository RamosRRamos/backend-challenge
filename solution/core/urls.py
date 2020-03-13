from django.urls import path

from core.views import (HomeView, DocumentationView, ReadMeView,BootstrapView,
                        PlaceList, PlaceCreate, PlaceUpdate, PlaceDetail, PlaceDelete)

app_name = 'core'

urlpatterns = [
    # Menu Urls
    path('', HomeView.as_view(), name='home'),
    path('documentation', DocumentationView.as_view(), name='doc'),
    path('read-me', ReadMeView.as_view(), name='read-me'),
    path('bootstrap', BootstrapView.as_view(), name='bootstrap'),

    # Place Bootstrap Urls
    path('place-list', PlaceList.as_view(), name='place-list'),
    path('place-create', PlaceCreate.as_view(), name='place-create'),
    path('place-detail/<int:pk>', PlaceDetail.as_view(), name='place-detail'),
    path('place-update/<int:pk>', PlaceUpdate.as_view(), name='place-update'),
    path('place-delete/<int:pk>', PlaceDelete.as_view(), name='place-delete'),

]
