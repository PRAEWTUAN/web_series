
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name='logout'),
    path('addUser/', views.addUser, name="addUser"),
    path('loginForm/', views.loginForm, name="loginForm"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name='signup'),
    
    # URLs สำหรับ forgot password
    # เส้นทางสำหรับการรีเซ็ตรหัสผ่าน
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = "registration/password_reset_form.html"), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name = "registration/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = "registration/password_reset_complete.html"), name='password_reset_complete'),

]
