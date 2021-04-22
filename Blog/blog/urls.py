from django.urls import path
from .views import BlogListView, BlogDetailView, RegisterView, LoginView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path ('', BlogListView.as_view (), name='home'),
    path ('post/<int:pk>/', BlogDetailView.as_view (), name='post_detail'),
    path ('register/', RegisterView, name='register'),
    path ('login/', LoginView, name="login"),
    path ('logout/', LogoutView, name="logout"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"),  name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
         name="password_reset_complete"),
]
