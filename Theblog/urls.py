from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView,CategoryListView,like_posts,AddCommentView,DeleteCommentView,LikeCommentView,download_word_document,follow_user,unfollow_user
from . import views
urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:category_title>/', CategoryView.as_view(), name='cat'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>/', like_posts, name='like_posts'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('comment/<int:pk>/delete/', DeleteCommentView.as_view(), name='delete_comment'),
    path('comment/<int:pk>/like/', LikeCommentView.as_view(), name='like_comment'),
    path('search/', views.Search , name='search'),
    path('download/<int:post_id>/', download_word_document, name='download_word_document'),
    path('follow/<int:pk>/', follow_user, name='follow_user'),
    path('unfollow/<int:pk>/', unfollow_user, name='unfollow_user'),
]

  

