from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
