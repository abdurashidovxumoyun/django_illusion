from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

class Home(TemplateView):
    template_name='pages/index.html'

class Blog_classic_1_right(TemplateView):
    template_name='pages/blog_classic_1_column_right_sidebar.html'

class Blog_classic_1(TemplateView):
    template_name='pages/blog_classic_1_column.html'

class Blog_grid_2_left(TemplateView):
    template_name='pages/blog_grid_2_columns_left_sidebar.html'

class Blog_grid_2_columns(TemplateView):
    template_name='pages/blog_grid_2_columns.html'

class Blog_grid_3_columns_right(TemplateView):
    template_name='pages/blog_grid_3_columns_right_sidebar.html'

class Blog_grid_3_columns(TemplateView):
    template_name='pages/blog_grid_3_columns.html'

class Blog_grid_4(TemplateView):
    template_name='pages/blog_grid_4_columns.html'