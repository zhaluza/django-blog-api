from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from post.views import PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
