from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from todo_backend import views

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
                  path('todo/api/v1/', include(router.urls)),
                  path('admin/', admin.site.urls),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
