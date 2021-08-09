"""bookmarks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path , include
# from .account.views import user_page 
from .views import dashboard , register , edit
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeDoneView as pv


urlpatterns = [
    path('', dashboard, name="first_page"),
    path('edit/', edit, name='edit'),

    path('register/', register, name='register'),
    # path('register_done/', views.register, name='register_done'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


   path('password_change/',auth_views.PasswordChangeView.as_view(),
                name='password_change'),
    path('password-change-Done/',
                pv.as_view(template_name='registration/password_change_done.html'),
            name='password_change_done'),

    path('password_reset/',
auth_views.PasswordResetView.as_view(),
name='password_reset'),
path('password_reset/done/',
auth_views.PasswordResetDoneView.as_view(),
name='password_reset_done'),
path('reset/<uidb64>/<token>/',
auth_views.PasswordResetConfirmView.as_view(),
name='password_reset_confirm'),
path('reset/done/',
auth_views.PasswordResetCompleteView.as_view(),
name='password_reset_complete'),
]
