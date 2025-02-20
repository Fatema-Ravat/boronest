from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('login/',views.user_login,name='user_login'),
    path('logout/', views.user_logout,name='user_logout'),
    path('register/', views.register_user,name='register_user'),
    path('edit_user/', views.edit_user,name='edit_user'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'),name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),name='password_change_done'),
]
