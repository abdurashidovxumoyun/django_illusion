from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('blog_classic_1/', Blog_classic_1_right.as_view(), name='blog_1_right'),
    path('')
]
