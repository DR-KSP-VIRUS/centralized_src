from django.urls import path

from . import views as v

app_name = 'posts'


urlpatterns = [
    path('', v.index, name='home'),
    path('add-blog', v.add_blog, name='add-blog'),
    path('new-blogs', v.new_blogs, name='new-blogs'),
    path('blogs', v.blogs, name='blogs'),
    path('about-us', v.about_us, name='about-us'),
]