from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='backend/logout.html'), name='account_logout'),
    path('login/', auth_views.LoginView.as_view(template_name='backend/login.html'), name='account_login'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='backend/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='backend/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='backend/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='backend/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
