from django.urls import path
from .views import BlogListView, BlogCreateView, BlogDetailView, BlogDeleteView, RegisterView, LoginView, LogoutView, \
    BlogUpdateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path ('', BlogListView.as_view (), name='home'),
    path ('post/<int:pk>/', BlogDetailView, name='post_detail'),
    path ('post/new/', BlogCreateView.as_view (), name='post_new'),
    path ('register/', RegisterView, name='register'),
    path ('login/', LoginView, name="login"),
    path ('logout/', LogoutView, name="logout"),
    path ('post/<int:pk>/edit', BlogUpdateView.as_view (), name='post_edit'),
    path ('post/<int:pk>/delete', BlogDeleteView.as_view (), name='post_delete'),

    path ('reset_password/', auth_views.PasswordResetView.as_view (template_name="password_reset.html"),
          name="reset_password"),
    path ('reset_password_sent/', auth_views.PasswordResetDoneView.as_view (template_name="password_reset_sent.html"),
          name="password_reset_done"),
    path ('reset/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view (template_name="password_reset_form.html"),
          name="password_reset_confirm"),
    path ('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view (template_name="password_reset_done"
                                                                                                  ".html"),
          name="password_reset_complete"),
]
