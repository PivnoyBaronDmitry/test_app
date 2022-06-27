from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics

from .serializers import NewsSerializer, PizzaSerializer
from .models import *


def index(request):
    return render(request, 'testapp/index.html')


class NewsAPIGenericView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsAPIUpdateView(generics.RetrieveUpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


# class NewsAPIView(viewsets.ModelViewSet):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer

# class ListNews(APIView):
#     def get(self, request):
#         cats = [news.category.id for news in News.objects.all()]
#         return Response(cats)
#
#     def post(self, request):
#         return Response({"message": "Got some data!", "data": request.data})

# class PizzaAPIView(generics.ListCreateAPIView):
#     queryset = Pizza.objects.all()
#     serializer_class = PizzaSerializer