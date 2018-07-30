from django.contrib.auth.views import logout
from django.urls import path

from dashboard.views import HomeView, SignUpView, DashboardView, SignInView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('logout/', logout, {"next_page": "/home/"}, name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard')
]