from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dash/",views.dash_view, name="dash"),
    path("signup/",views.users_signup, name="signup"),
    path("logout/",views.logout_view, name="logout")
]
