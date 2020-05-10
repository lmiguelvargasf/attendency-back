from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from .attendance.urls import urlpatterns as attendance_urls

urlpatterns = attendance_urls
urlpatterns += [
    path('token-auth/', obtain_jwt_token),
]
