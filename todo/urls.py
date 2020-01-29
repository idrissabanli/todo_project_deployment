from django.urls import path
from .views import TaskList, CreateTaskView, UserViewSet
from .routers import router

app_name = 'todo'

urlpatterns = [
    # path('content/', content, name='content')
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('create-task/', CreateTaskView.as_view(), name='create_task'),
]

urlpatterns += router.urls