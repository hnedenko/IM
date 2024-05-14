from django.urls import path, include
from exercise.views import ChapterViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'chapter', ChapterViewSet)

print(router.urls)

urlpatterns = [
    path('', include(router.urls)),
]
