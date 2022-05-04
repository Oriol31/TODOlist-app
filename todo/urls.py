from django.urls import include, path
from . import views


urlpatterns = [
    path('tasks/', views.TaskListView.as_view()),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view())
]
