from django.contrib import admin
from django.urls import path
#from . import views
from .views import HomeView, articledetailView, addpostView, UpdatePostView, DeletePostView, addCategoryView, CategoryView , LikeView

admin.site.site_header = 'Admin Panel!'
admin.site.index_title = 'Welcome!!'
admin.site.site_title = 'Portal!!!'

urlpatterns = [
   # path('', views.home, name="home"),
   path('', HomeView.as_view(), name="home"),
   path('article/<int:pk>', articledetailView.as_view(), name = "article_detail" ),
   path('add_post/', addpostView.as_view(), name ="addpost"),
   path('add_category/', addCategoryView.as_view(), name ="addcategory"),
   path('article/edit/<int:pk>', UpdatePostView.as_view(), name ="update_post"),
   path('article/<int:pk>/remove', DeletePostView.as_view(), name ="delete_post"),
   path('category/<str:cats>/', CategoryView, name='category'),
   path('like/<int:pk>', LikeView, name='like_post'),
]
