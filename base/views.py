from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

class Home(TemplateView):
    template_name='pages/index.html'

class Blog_classic_1_right(TemplateView):
    template_name='pages/blog_classic_1_column_right_sidebar.html'