from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from patients.views import UserViewSet, PatientViewSet
from submissions.views import SubmissionViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'submissions', SubmissionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
