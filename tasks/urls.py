from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.list, name='list'),
    path('create', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('register/', views.register, name="register"),
]
