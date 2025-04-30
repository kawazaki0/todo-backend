from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from todo_backend import views

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
                  path('', views.HomeView.as_view(), name='home_view'),
                  path('todo/api/v1/', include(router.urls)),
                  path('admin/', admin.site.urls),
                  path('test/', views.list_tasks, name='test_view'),
                  path('create_task/', views.create_task, name='create_task'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
