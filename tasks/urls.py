from django.urls import path
from .views import TaskView

urlpatterns = [
    path('', TaskView.list, name='list'),
    path('create', TaskView.create, name='create'),
    path('update/<int:id>', TaskView.update, name='update'),
    path('delete/<int:id>', TaskView.delete, name='delete'),
    path('css/<str:file>.css', TaskView.stylesheet, name='css'),
    path('js/<str:file>.js', TaskView.scripts, name='js'),
]
