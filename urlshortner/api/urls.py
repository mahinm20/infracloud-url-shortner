from re import I
from django.urls import path
from .views import ShortnerCreateAPIview,ShortnerListAPIView

appname="api"



urlpatterns = [
    path('',ShortnerListAPIView.as_view(),name='links'),
    path('create/',ShortnerCreateAPIview.as_view(),name='create_link'),
]
