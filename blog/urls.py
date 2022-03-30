from django.urls import path
from . import views


urlpatterns = [
    path('search/<str:ct>/<str:q>/', views.PostSearch.as_view(), name="search"),
    path('delete_comment/<int:pk>/', views.delete_comment),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('delete_post/<int:pk>/', views.delete_post),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('create_post/', views.PostCreate.as_view(), name="create"),
    path('tag/<str:slug>/', views.tag_page),
    path('category/<str:slug>/', views.category_page),
    path('<int:pk>/new_comment/', views.new_comment),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('membership_page/', views.membership_page, name="membership_page"),
    path('', views.PostList.as_view(), name="news"),

]