from django.urls import path

from . import views as v

app_name = 'accounts'

urlpatterns = [
    path('login', v.user_login_form, name='login'),
    path('signup', v.signup, name='signup'),
    path('logout', v.user_logout, name='logout'),
    path('dashboard', v.user_dashboard, name='dashboard'),
    path('profile', v.profile, name='profile'),
    path('student-profile', v.student_profile, name='student-profile'),
    path('portfolio', v.portfolios, name="portfolios"),
    path('add-portfolio', v.add_portfolio, name="add-portfolio"),
    path('remove-portfolio/<int:id>', v.remove_portfoloio, name="remove-portfolio"),
    path('edit-portfolio/<int:id>', v.edit_portfolio, name="edit-portfolio"),
]