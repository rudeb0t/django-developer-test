from roadmap.api.views import ProjectViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'projects', ProjectViewSet, base_name='projects')

urlpatterns = router.urls
