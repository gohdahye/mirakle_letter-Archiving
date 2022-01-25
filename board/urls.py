from django.urls import path
from . import views

urlpatterns = [
    path('delete_board/<int:pk>/', views.BoardDelete.as_view()),
    path('update_board/<int:pk>/', views.BoardUpdate.as_view()),
    path('create/', views.BoardCreate.as_view(), name="board_create"),
    path('<int:pk>/', views.BoardDetail.as_view()),
    path('', views.BoardList.as_view(), name="boardList"),
]