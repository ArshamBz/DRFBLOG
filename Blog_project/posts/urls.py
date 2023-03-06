from .views import PostList, PostDetails
from django.urls import path

urlpatterns = [
    path('',PostList.as_view()),
    path('<int:pk>/',PostDetails.as_view()),
]