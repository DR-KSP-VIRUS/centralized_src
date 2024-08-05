from django.urls import path

from . import views as v

app_name = 'posts'


urlpatterns = [
    path('', v.index, name='home'),
    path('add-blog', v.add_blog, name='add-blog'),
    path('blogs', v.blogs, name='blogs'),
    path('blog-view/<int:id>', v.blog_details, name='blog_details'),
    path('edit-blog/<int:id>', v.edit_blog, name='edit-blog'),
    path('delete-blog/<int:id>', v.remove_blog, name='remove-blog'),
    path('about-us', v.about_us, name='about-us'),
]