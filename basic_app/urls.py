from django.urls import path

from basic_app import views

urlpatterns = [
    # path('', views.index),
    path('contact/', views.ListContact.as_view()),
    path('contact/<int:pk>', views.DetailContact.as_view()),
    path('contacts/', views.ListBoglanish.as_view()),
    path('contacts/<int:pk>', views.DetailBoglanish.as_view())
]
