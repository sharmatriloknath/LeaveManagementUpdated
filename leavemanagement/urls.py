from django.contrib import admin
from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('auth-jwt/', obtain_jwt_token),
    # path('auth-jwt-refresh/', refresh_jwt_token),
    # path('auth-jwt-verify/', verify_jwt_token),
    path('', include('users.urls'))
]
