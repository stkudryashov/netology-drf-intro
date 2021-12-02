from django.contrib import admin
from django.urls import path, include
from measurements.views import ProjectViewSet, MeasurementViewSet

from rest_framework.routers import DefaultRouter

ProjectRouter = DefaultRouter()
ProjectRouter.register('', ProjectViewSet)

MeasurementRouter = DefaultRouter()
MeasurementRouter.register('', MeasurementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/project/', include(ProjectRouter.urls)),
    path('api/v1/measurement/', include(MeasurementRouter.urls))
]
