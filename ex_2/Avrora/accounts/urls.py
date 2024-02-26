from django.contrib.auth import views as auth_views
from django.urls import path
from accounts import views


urlpatterns = [
    path("", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("create-user/", views.UserCreateView.as_view(), name="user_create"),
]
