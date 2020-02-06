from rest_framework import routers

from .views import AuthViewSet, LeavesViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('api/auth', AuthViewSet, basename='auth')
router.register('api/leaves', LeavesViewSet, basename='leaves')

urlpatterns = router.urls

# The urls you need to hit to get result done
# /api/auth/login
# /api/auth/register
# /api/auth/logout
# /api/auth/password_change