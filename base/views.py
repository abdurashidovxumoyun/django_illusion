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

class Blog_masonry_2_right(TemplateView):
    template_name='pages/blog_masonry_2_columns_right_sidebar.html'

class Blog_masonry_2(TemplateView):
    template_name='pages/blog_masonry_2_columns.html'

class Blog_masonry_3_left(TemplateView):
    template_name='pages/blog_masonry_3_columns_left_sidebar.html'

class Blog_masonry_3(TemplateView):
    template_name='pages/blog_masonry_3_columns'

class Blog_masonry_4(TemplateView):
    template_name='pages/blog_masonry_4_columns.html'

class Blog_single_audio_post(TemplateView):
    template_name='pages/blog_single_audio_post.html'

class Blog_single_blockquote(TemplateView):
    template_name='pages/blog_single_blockquote.html'

class Blog_single_full_width(TemplateView):
    template_name='pages/blog_single_full_width.html'

class Blog_single_image_slideshow_post(TemplateView):
    template_name='pages/blog_single_image_slideshow_post.html'

class Blog_single_link_post(TemplateView):
    template_name='pages/blog_single_link_post.html'

class Blog_single_right_sidebar(TemplateView):
    template_name='pages/blog_single_right_sidebar.html'

class Blog_single_video_post(TemplateView):
    template_name='pages/blog_single_video_post.html'

class index_agency(TemplateView):
    template_name='pages/index_agency.html'

class index_boxed_static_video(TemplateView):
    template_name='pages/index_boxed_static_video.html'

class index_landing(TemplateView):
    template_name='pages/index_landing.html'

class index_magazine(TemplateView):
    template_name='pages/index_magazine.html'

class index_other_head_static_content(TemplateView):
    template_name='pages/index_other_head_static_content.html'

class index_portfolio(TemplateView):
    template_name='pages/index_portfolio.html'

class index_side_menu(TemplateView):
    template_name='pages/index_side_menu.html'

class index_static_image(TemplateView):
    template_name='pages/index_static_image.html'

class index_text_and_form(TemplateView):
    template_name='pages/index_text_and_form.html'

class index_video_background(TemplateView):
    template_name='pages/index_video_background.html'

class index_video_in_popup(TemplateView):
    template_name='pages/index_video_in_popup.html'