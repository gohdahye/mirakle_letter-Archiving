from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.signup, name="signup"),
    path('agreement/', views.agreement, name="agreement"),
   # path('profile/', views.profile, name='profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    re_path(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,40})/$', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
