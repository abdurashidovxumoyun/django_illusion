from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('blog_classic_1_right/', Blog_classic_1_right.as_view(), name='Blog_Classic_Right1'),
    path('Blog_classic_1/',Blog_classic_1.as_view(), name='Blog_Classic_1'),
    path('Blog_grid_2_left/', Blog_grid_2_left.as_view(), name='Blog_Grid_2'),
    path('Blog_grid_2_columns/', Blog_grid_2_columns.as_view(), name='Blog_Grid_2_Columns'),
    path('Blog_grid_3_columns_right/', Blog_grid_3_columns_right.as_view(), name='Blog_Grid_3_Columns_Right'),
    path('Blog_grid_3_columns/', Blog_grid_3_columns.as_view(), name='Blog_Grid_3_Columns')
]
