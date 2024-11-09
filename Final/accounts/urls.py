from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),  # Custom login view
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # Logout redirects to home
    path('user_home/', views.user_home, name='user_home'),  # User dashboard
]