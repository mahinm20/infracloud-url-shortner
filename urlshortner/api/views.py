from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView
from .models import Link
from .serializer import LinkSerializer
from django.views import View
# Create your views here.

class ShortnerListAPIView(ListAPIView):
    queryset=Link.objects.all()
    serializer_class = LinkSerializer


class ShortnerCreateAPIview(CreateAPIView):
    serializer_class = LinkSerializer

class Redirect()    