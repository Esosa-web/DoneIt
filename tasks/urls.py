from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TagViewSet, TaskViewSet, SubtaskViewSet, register_user, login_user, test_auth, simple_test

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'subtasks', SubtaskViewSet, basename='subtask')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('test-auth/', test_auth, name='test-auth'),
    path('simple-test/', simple_test, name='simple-test'),
]