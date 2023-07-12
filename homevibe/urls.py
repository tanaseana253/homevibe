from django.urls import path
from homevibe import views
import django.contrib.auth.views as auth_views

from homevibe.forms import SigninForm
# from homevibe.views import photo_list

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='homepage'),
    path('login/', auth_views.LoginView.as_view(form_class=SigninForm), name='login'),
    path('sign_up/', views.SignupView.as_view(), name='sign_up'),
    path('inspiration/', views.InspirationTemplateView.as_view(), name='inspiration'),
    path('photo_list/', views.PhotoListView.as_view(), name='photo_list'),
    # path('photo_list/', photo_list, name='photo_list'),
]