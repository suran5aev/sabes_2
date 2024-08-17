from rest_framework.routers import DefaultRouter

from apps.todo.views import TaskAPI

router = DefaultRouter()
router.register('todo', TaskAPI, basename='todo_list')

urlpatterns = [
    
]


urlpatterns += router.urls