from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index,name='index'),
    path('new_listing/', views.new_listing,name='new_listing'),
    path('borrow_product/<int:pk>/',views.borrow_product,name='borrow_product'),
    path('approve_request/<int:pk>/',views.approve_request,name='approve_request'),
    path('return_request/<int:pk>/',views.return_request,name='return_request'),
    path('search/',views.search,name='search'),
]
