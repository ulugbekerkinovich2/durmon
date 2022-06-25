from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from basic_app import models, serializers




class ListContact(generics.ListCreateAPIView):

    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class DetailContact(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class ListBoglanish(generics.ListCreateAPIView):
    permission_classes = []
    authentication_classes = []


    queryset = models.Boglanish.objects.all()
    serializer_class = serializers.BoglanishSerializer


class DetailBoglanish(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Boglanish.objects.all()
    serializer_class = serializers.BoglanishSerializer