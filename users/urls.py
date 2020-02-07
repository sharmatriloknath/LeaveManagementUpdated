from rest_framework import routers

from .views import AuthViewSet, LeavesBalanceViewSet, LeavesRequestViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('api/auth', AuthViewSet, basename='auth')
router.register('api/leave_balance', LeavesBalanceViewSet, basename='balance')
router.register('api/leave_request', LeavesRequestViewSet, basename='request')

urlpatterns = router.urls

# The urls you need to hit to get result done
# /api/auth/login
# /api/auth/register
# /api/auth/logout
# /api/auth/password_change