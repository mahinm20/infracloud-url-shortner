from django import views
from django.shortcuts import render, redirect
from rest_framework.generics import ListAPIView,CreateAPIView
from .models import Link
from .serializer import LinkSerializer
from django.views import View
from django.conf import settings
# Create your views here.

class ShortnerListAPIView(ListAPIView):
    queryset=Link.objects.all()
    serializer_class = LinkSerializer


class ShortnerCreateAPIview(CreateAPIView):
    serializer_class = LinkSerializer

class Redirect(View):
    def get(self,request,shortener_link,*args, **kwargs):
        shortener_link=settings.HOST_URL+'/'+self.kwargs['shortener_link']
        redirect_link = Link.objects.filter(short_url=shortener_link).first().original_url
        return redirect(redirect_link)
