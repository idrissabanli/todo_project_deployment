from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TaskViewSetAPI

router = DefaultRouter()

router.register(r'api-users', UserViewSet)
router.register(r'api-tasks', TaskViewSetAPI)

