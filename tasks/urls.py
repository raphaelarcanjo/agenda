from django.urls import path
from .views import TaskView

urlpatterns = [
    path('', TaskView.list, name='list'),
    path('create', TaskView.create, name='create'),
    path('update/<int:id>', TaskView.update, name='update'),
    path('delete/<int:id>', TaskView.delete, name='delete'),
]
