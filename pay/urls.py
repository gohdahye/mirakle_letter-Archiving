from django.urls import path
from . import views


urlpatterns = [
    path('complete/', views.complete, name="complete"),
    path('', views.index, name="pay"),
]
