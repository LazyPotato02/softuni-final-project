from django.urls import path, reverse_lazy

from employee_management_sys.base.views import IndexView, UserEditView, UserDeleteView, UserCreateView, about
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('reset-password', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('index')),
         name='reset password'),
    path('login', auth_views.LoginView.as_view(template_name='base/login.html', success_url=reverse_lazy('index'),
                                               redirect_authenticated_user=True), name='login'),
    path('sign-up/', UserCreateView.as_view(), name='sign-up'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('user/edit/<int:pk>', UserEditView.as_view(), name='edit user'),
    path('user/delete/<int:pk>', UserDeleteView.as_view(), name='delete user'),
    path('about/', about, name='about')

]
